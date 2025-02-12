from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    
    try:
        # Ma'lumotlar bazasini yaratamiz:
        await db.create()
        # await db.drop_users()
        await db.create_table_users()
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
