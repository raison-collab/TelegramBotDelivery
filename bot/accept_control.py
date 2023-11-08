import json
from enums import PATH
from . import logger
from .models import User


def __parse_users_from_file() -> list[User]:
    with open(PATH.USERS.value, 'r') as file:
        text = file.read()
        if text != "":
            data = json.loads(text)
            if isinstance(data, dict):
                return [User.from_dict(data)]
            return [User.from_dict(i) for i in data]
        else:
            return []


def append_user(user: User):
    users.append(user)
    data = [i.to_dict() for i in users]
    users_json = json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8').decode()
    with open(PATH.USERS.value, encoding='utf-8', mode='w') as file:
        file.write(users_json)
    logger.success(f'Пользователь {user.username} | {user.first_name} Добавлен в список')


users = __parse_users_from_file()
