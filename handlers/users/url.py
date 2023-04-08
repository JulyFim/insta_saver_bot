import requests
import json
import asyncio
from aiogram import types
from aiogram.types import ChatActions
from loader import dp, bot


@dp.message_handler()
async def insta(message: types.Message):
    try:
        url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
        link = message.text
        querystring = {"url": link}

        headers = {
            "X-RapidAPI-Key": "b0365f596dmsh0e936643154e47ep1ef356jsn6de5cd0b0793",
            "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response)
        # print(response.content)
        result = response.json()
        # print(result)
        title = result.get('title')
        if title is None:
            await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
            await message.answer_video(video=result.get('media'))
        await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        await message.answer_video(video=result.get('media'))
        await message.answer(title)
    except (Exception, ExceptionGroup, BaseException, BaseExceptionGroup):
        await message.answer(
            f"Please make sure the link is correct and try again!\n\n"
            f"Убедитесь, что ссылка указаны правильно, и повторите попытку!")
