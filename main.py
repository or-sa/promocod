import asyncio
import logging
import os
from dotenv import load_dotenv, find_dotenv
from keyboards.keybords import keyboard
from db.engine import test
# from db.engine import test, create_as_engine, get_session_maker
from pprint import pprint

import mysql.connector

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message


# user = 'prigodpa_kupon'
# host = 'prigodpa.beget.tech'
# password = 'm&*3VPtf'
# port = '3306'
# database = 'prigodpa_kupon'

load_dotenv(find_dotenv())

user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
database = os.getenv('database')

connection_string = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'
# All handlers should be attached to the Router (or Dispatcher)
router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    f_kup = '\n'.join(test(con=connection_string))
    # f_kup = '\n'.join(test(sm=get_session_maker(engine=create_as_engine(url=connection_string))))
    await message.answer(text=f_kup, parse_mode="html")
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>", reply_markup=keyboard)


@router.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward received message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker and etc.)
    """
    try:
        # Send copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(os.getenv('TOKEN_API'), parse_mode="HTML")

    # async_engine = create_as_engine(url=connection_string)
    # session_maker = get_session_maker(async_engine)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
