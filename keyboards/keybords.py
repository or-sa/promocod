from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

kb = [
    [KeyboardButton(text="Создать"),
     KeyboardButton(text="Изменить"),
     KeyboardButton(text="Удалить ")],
    [KeyboardButton(text="Список промокодов")]
    ]
keyboard = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
    )
