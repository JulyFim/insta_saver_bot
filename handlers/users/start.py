from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    username = message.from_user.username
    user = await db.select_user(telegram_id=message.from_user.id)

    if user is None:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
        # ADMINGA xabar beramiz
        count = await db.count_users()
        msg = f"@{user[2]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    # user = await db.select_user(telegram_id=message.from_user.id)
    name = message.from_user.full_name
    if username is None:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Hi! This bot helps you to save photos, videos, carousels and many more from Instagram. To get photo/video/carousel/reels/IGTV send URL of the post to the bot. \n\nПривет! Бот позволяет сохранять фото, все типы видео, галереи и прочее из Instagram. Чтобы скачать фото/видео/галерею/рилз/IGTV просто пришлите ссылку на пост. ", reply_markup=ReplyKeyboardRemove())
    else:
        await bot.send_message(chat_id=ADMINS[0], text=f"@{username} bazaga oldin qo'shilgan")
        await message.answer(f"Hi! This bot helps you to save photos, videos, carousels and many more from Instagram. To get photo/video/carousel/reels/IGTV send URL of the post to the bot. \n\nПривет! Бот позволяет сохранять фото, все типы видео, галереи и прочее из Instagram. Чтобы скачать фото/видео/галерею/рилз/IGTV просто пришлите ссылку на пост.", reply_markup=ReplyKeyboardRemove())