from typing import List, Dict
from sqlalchemy import select, delete, update
from application.models.user_model import User
from application.services.base import Service


class UserService(Service):
    async def get_all(
        self,
    ) -> List[Dict[str, int | str]]:
        users = await self.session.scalars(select(User))
        result_users = []
        for user in users.all():
            result_users.append(
                {"id": user.id, "username": user.username, "email": user.email}
            )
        return result_users

    async def delete_user(self, user_id: str) -> Dict[str, int]:
        deleted_user = await self.session.execute(
            delete(User).where(User.id == user_id).returning(User)
        )
        deleted_user = deleted_user.scalar()
        if not deleted_user:
            return {"error": 404}

        deleted_user = {
            "id": deleted_user.id,
            "username": deleted_user.username,
            "email": deleted_user.email,
        }
        await self.session.commit()
        return deleted_user

    async def create_user(self, data: Dict[str, int | str]) -> Dict[str, int | str]:
        new_user = User(**data)
        self.session.add(new_user)
        await self.session.commit()
        return data

    async def update_user(self, data: Dict[str, int | str]) -> Dict[str, int | str]:
        updated_user = await self.session.execute(
            update(User).where(User.id == data["id"]).values(data).returning(User)
        )
        updated_user = updated_user.scalar()
        if not updated_user:
            return {"error": 404}

        return {
            "id": updated_user.id,
            "username": updated_user.username,
            "email": updated_user.email,
        }
