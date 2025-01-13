from typing import List, Dict
from application.services.base import Service

# временное хранилище
users = [
    {
        "id": 1,
        "username": "test",
        "password": "test",
        "email": "test@gmail.com",
    },
    {
        "id": 2,
        "username": "demo",
        "password": "demo",
        "email": "demo@gmail.com",
    },
    {
        "id": 3,
        "username": "admin",
        "password": "admin",
        "email": "admin@gmail.com",
    }
]

class UserService(Service):
    async def get_all(self,) -> List[Dict[str, int | str]]:
        return users
    
    async def delete_user(self, user_id: int) -> Dict[str, int]:
        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                return {"success": 200}
        return {"error": 404}
    
    async def create_user(self, data: Dict[str, int | str]) -> Dict[str, int | str]:
        users.append(data)
        return data