import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '*', intents=intents)

#Load the cogs to the main file
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

#Start the bot
async def main():
    async with client:
        await load()
        await client.start(os.getenv("tokenbot"))

@client.event
async def on_ready():
    print('Levi is online')

asyncio.run(main())