import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["مودي","المبرمج مودي","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𐇮 Z3EIM 𐇮](https://t.me/Syri20)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @elhyba ❫
◉ 𝙸𝙳      : ❪ `6992029895` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@Syri20) my world (@SYS90k - @Syri20) my bro (@Syri20) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Z3EIM V1", url=f"https://t.me/syri20"), 
                 ],[
                   InlineKeyboardButton(
                        "🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙3EIM 🔱", url=f"https://t.me/SYS90k"),
                ],

            ]

        ),

    )
