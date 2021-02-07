from discord.ext import commands
import discord
import asyncio

import setting

intents = discord.Intents.all()
TOKEN = setting.dToken
prefix = "¥"

bot = commands.Bot(command_prefix=prefix,help_command=None,intents=intents)

bot.load_extension("Cogs.default")

bot.load_extension("Cogs.afk.afk")
bot.load_extension("Cogs.afk.unmute")


bot.run(TOKEN)
