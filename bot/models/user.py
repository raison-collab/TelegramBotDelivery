from dataclasses import dataclass

from aiogram.types import Message


@dataclass
class User:
    id: int
    username: str
    first_name: str

    @staticmethod
    def from_dict(data: dict):
        return User(
            id=data["id"],
            username=data["username"],
            first_name=data["first_name"]
        )

    @staticmethod
    def from_message(message: Message):
        return User(
            id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.username
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name
        }

    def __str__(self):
        return (f"id={self.id} | "
                f"username={self.username} | "
                f"first_name={self.first_name}")