import requests
import json
import asyncio
from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(startswith=("@",)))
async def insta(message: types.Message):
    try:
        url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post.php"

        link = message.text

        querystring = {"url": link}

        headers = {
            "X-RapidAPI-Key": "10219f068dmshf19b8b217d5d372p18fdc3jsnf9d614b1f853",
            "X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response)
        # print(response.content)
        result = response.json()
        # print(result)
        await message.answer_photo(photo=result.get('image'))
        await message.answer(result.get('caption'))
    except (Exception, ExceptionGroup, BaseException, BaseExceptionGroup):
        await message.answer(
            f"Please make sure the username is correct and try again!\n\n"
            f"Убедитесь, что имя пользователя указано правильно, и повторите попытку.!")
