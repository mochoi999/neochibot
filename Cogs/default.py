from discord.ext import commands
import discord
import asyncio


class Default(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('--------------------')
        print('起動中...')
        print('BOT NAME : ' + self.bot.user.name)
        print('BOT ID : ' + str(self.bot.user.id))
        print('--------------------')

def setup(bot):
    return bot.add_cog(Default(bot))