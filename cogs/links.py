import discord
import config
from discord.ext import commands
from discord.ext.commands import Cog

class Links(Cog):
    """
    Commands for easily linking to projects.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def pegaswitch(self, ctx):
        """Link to the Pegaswitch repo"""
        await ctx.send("https://github.com/reswitched/pegaswitch")

    @commands.command(hidden=True, aliases=["atmos", "ams"])
    async def atmosphere(self, ctx):
        """Link to the Atmosphere repo"""
        await ctx.send("https://github.com/atmosphere-nx/atmosphere")

<<<<<<< HEAD
    @commands.command(hidden=True)
=======
    @commands.command(hidden=True, aliases=["bootloader"])
>>>>>>> 7bc3ae71eba91c813ef089c8ad7c1ea95289ce3f
    async def hekate(self, ctx):
        """Link to the Hekate repo"""
        await ctx.send("https://github.com/CTCaer/hekate") 

    @commands.command(hidden=True, aliases=["xyproblem"])
    async def xy(self, ctx):
        """Link to the "What is the XY problem?" post from SE"""
        await ctx.send("<https://meta.stackexchange.com/q/66377/285481>\n\n"
                       "TL;DR: It's asking about your attempted solution "
                       "rather than your actual problem.\n"
                       "It's perfectly okay to want to learn about a "
                       "solution, but please be clear about your intentions "
                       "if you're not actually trying to solve a problem.")

    @commands.command(hidden=True, aliases=["guides", "link"])
    async def guide(self, ctx):
        """Link to the guide(s)"""

        message_text=("**Generic starter guides:**\n"
                      "AtlasNX's Guide: "
                      "<https://switch.homebrew.guide>\n"
                      "\n"
                      "**Specific guides:**\n"
                      "Manually Updating/Downgrading (with HOS): "
                      "<https://switch.homebrew.guide/usingcfw/manualupgrade>\n"
                      "Manually Repairing/Downgrading (without HOS): "
                      "<https://switch.homebrew.guide/usingcfw/manualchoiupgrade>\n"
                      "Setting up EmuMMC (Windows): "
                      "<https://switch.homebrew.guide/emummc/windows>\n"
                      "Setting up EmuMMC (Linux): "
                      "<https://switch.homebrew.guide/emummc/linux>\n"
                      "Setting up EmuMMC (Mac): "
                      "<https://switch.homebrew.guide/emummc/mac>\n"
                      "How to get started developing Homebrew: "
                      "<https://switch.homebrew.guide/homebrew_dev/introduction>\n"
                      "\n")

        try:
            support_faq_channel = self.bot.get_channel(config.support_faq_channel)
            if support_faq_channel is None:
                message_text += "Check out #support-faq for additional help."
            else:
                message_text += f"Check out {support_faq_channel.mention} for additional help."
        except AttributeError:
            message_text += "Check out #support-faq for additional help."
        
        await ctx.send(message_text)

    @commands.command(hidden=True, aliases=["patron"])
    async def patreon(self, ctx):
        """Link to the patreon"""
        await ctx.send("https://patreon.teamatlasnx.com")

    @commands.command(hidden=True, aliases=["coffee"])
    async def kofi(self, ctx):
        """Link to Ko-fi"""
        await ctx.send("https://kofi.teamatlasnx.com")

    @commands.command(hidden=True, aliases=["sdfiles"])
    async def kosmos(self, ctx):
        """Link to the latest Kosmos release"""
        await ctx.send("https://github.com/AtlasNX/Kosmos/releases/latest")

    @commands.command(hidden=True, aliases=["sd"])
    async def sdsetup(self, ctx):
        """Link to SD Setup"""
        await ctx.send("https://sdsetup.com")

    @commands.command()
    async def source(self, ctx):
        """Gives link to source code."""
        await ctx.send(f"You can find my source at {config.source_url}. "
                       "Serious PRs and issues welcome!")

def setup(bot):
    bot.add_cog(Links(bot))
