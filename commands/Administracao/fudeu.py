from discord import Invite, Role, Member
from discord.ext import commands
from datetime import datetime, timedelta
from checks.cargos import has_roles
from db.invites import insert_invite_reward
from utils.loader import configData


class Fudeu(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    async def fudeu(self,ctx, member: Member, role: Role):

        await member.add_roles(role)

        await ctx.reply("foi")
        
def setup(bot: commands.Bot):
    bot.add_cog(Fudeu(bot))
