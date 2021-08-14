"""
MIT License

Copyright (c) 2021 lucaso60
Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import discord
from discord.ext import commands
from discord import *
from datetime import datetime
from time import sleep

from extensions import on_start_screen

def time_now():
    time = datetime.now()
    current_time = time.strftime("%y-%m-%d %H:%M:%S")
    now = current_time + " >"
    return now

bot = commands.Bot(command_prefix=".")

TOKEN = input(f"{time_now()} Token: ")
ID = input(f"{time_now()} Channel id: ")
MESSAGE = input(f"{time_now()} Spam Message: ")

@bot.event
async def on_ready():
    print(f"{time_now()} Logged in as {bot.user}")
    id = int(ID)
    channel = bot.get_channel(id)
    while True:
        await channel.send(MESSAGE)
        print(f"{time_now()} Spamming {MESSAGE} to channel {ID}")
        sleep(0.8)

bot.run(TOKEN)


