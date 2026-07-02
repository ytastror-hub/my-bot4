import discord
from discord.ext import commands
import os

# أرقام القنوات
SOURCE_CHANNEL_ID = 1436351424999985162
TARGET_CHANNEL_ID = 1522282082900901890

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'البوت {bot.user} جاهز للعمل!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == SOURCE_CHANNEL_ID:
        target_channel = bot.get_channel(TARGET_CHANNEL_ID)
        if target_channel:
            if message.embeds:
                await target_channel.send(embed=message.embeds[0])
            elif message.content:
                await target_channel.send(f"**{message.author.name}**: {message.content}")

    await bot.process_commands(message)

# تشغيل البوت
bot.run(os.environ['TOKEN'])