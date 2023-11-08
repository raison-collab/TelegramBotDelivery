import json

from aiogram.filters import CommandStart
from aiogram.types import Message
from loguru import logger

from enums import Users
from keyboards.reply_kbs import start_keyboard
from loader import dp


@dp.message(CommandStart())
async def start_command(m: Message):
    await m.answer('Привет. Вот тебе клава для управления', reply_markup=start_keyboard)

    with open(Users.users.value, 'r') as file:
        data = json.loads(file.read())

    print(data, type(data))

    data.append({'id': m.from_user.id, 'username': m.from_user.username, 'first_name': m.from_user.first_name})
    users_json = json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8').decode()

    with open(Users.users.value, encoding='utf-8', mode='w') as file:
        file.write(users_json)

    logger.success(f'Пользователь f{m.from_user.username} | {m.from_user.first_name} Добавлен в список')

    logger.debug(f'Пользователь: id={m.from_user.id} | username={m.from_user.username} | first_name={m.from_user.first_name} начал работу с ботом')