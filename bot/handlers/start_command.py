import json

from aiogram.filters import CommandStart
from aiogram.types import Message
from loguru import logger

from enums import PATH
from bot.keyboards.reply_kbs import start_keyboard
from bot.loader import dp


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer('Привет. Вот тебе клава для управления', reply_markup=start_keyboard)

    with open(PATH.USERS.value, 'r') as file:
        text = file.read()
        if text != "":
            data = json.loads(text)
            if isinstance(data, dict):
                data = [data]
        else:
            data = []

    print(data, type(data))

    data.append(
        {
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        }
    )
    users_json = json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8').decode()

    with open(PATH.USERS.value, encoding='utf-8', mode='w') as file:
        file.write(users_json)

    logger.success(f'Пользователь {message.from_user.username} | {message.from_user.first_name} Добавлен в список')

    logger.debug(f'Пользователь: '
                 f'id={message.from_user.id} | '
                 f'username={message.from_user.username} | '
                 f'first_name={message.from_user.first_name} начал работу с ботом')
