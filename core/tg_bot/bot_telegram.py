from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from tg_config import TOKEN
import sqlite3



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def db_table_val(user_id: str):
    conn = sqlite3.connect('../../db.sqlite3', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO core_users(user) VALUES (?)', [user_id])
    conn.commit()
    conn.close()

def search_id_telegram_in_core_user(id_telegram):
    conn = sqlite3.connect('../../db.sqlite3', check_same_thread=False)
    cursor = conn.execute("SELECT user FROM core_users WHERE user=?", [id_telegram]).fetchone()
    if cursor is None:
        conn.close()
        return False
    else:
        conn.close()
        return True


@dp.message_handler(commands=['start'])
async def get_user_id(message: types.message):
    us_id = str(message.from_user.id)
    if search_id_telegram_in_core_user(us_id) == False:
        db_table_val(user_id=us_id)
        print(f'добавлен новый пользователь {us_id} в таблицу core_user')
    else:
        print(f'пользователь {us_id} ранее уже создан в таблице core_user')



executor.start_polling(dp, skip_updates=True)
