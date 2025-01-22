from typing import List, Dict
from application.services.base import Service
import sqlite3

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

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
)
"""
)
cursor.execute(
    "INSERT INTO users (username, password, email) VALUES (?, ?, ?)", ('Alice', 'qwerty', 'alice@gmail.com')
)

cursor.execute(
    "INSERT INTO users (username, password, email) VALUES (?, ?, ?)", ('Bob', 'bob2007', 'bob2007@gmail.com')
)
conn.commit()

class UserService(Service):
    async def get_all(self,) -> List[Dict[str, int | str]]:
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()
    
    async def delete_user(self, user_id: int) -> Dict[str, int]:
        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                return {"success": 200}
        return {"error": 404}
    
    async def create_user(self, data: Dict[str, int | str]) -> Dict[str, int | str]:
        users.append(data)
        return data
    
    async def update_user(self, data: Dict[str, int | str]) -> Dict[str, int | str]:
        result = await self.delete_user(user_id=data["id"])
        if not result.get("error"):
            users.append(data)
        return result
