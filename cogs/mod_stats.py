import discord
from discord.ext import commands
from discord.ext.commands import Cog
from helpers.checks import check_if_staff
from helpers.userlogs import get_userlog, userlog_event_types


class ModStats(Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_stats_for_id(self, uid: int, events: list):
        userlog = get_userlog()

        results = { "warns": None,
                    "mutes": None,
                    "kicks": None,
                    "bans": None,
                    "notes": None }

        for event in events:
            results[event] = 0

        if len(userlog.values()) == 0:
            return results

        for logs in userlog.values():
            for event in events:
                if event not in logs:
                    continue

                for loggedEvent in logs[event]:
                    if uid == loggedEvent["issuer_id"]:
                        results[event] += 1

        return results

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["modstats"])
    async def modcounts(self, ctx, user: discord.Member = None):
        """Get a count of different mod related actions a user has made."""
        if user is None:
            user = ctx.author

        event_types = ["bans", "kicks", "mutes", "notes", "warns"]
        stats = self.get_stats_for_id(user.id, event_types)

        embed = discord.Embed(
            colour = 0xF92672,
            title = f"🔨 {user.name} Moderation Stats")
        for event_type in event_types:
          embed.add_field(
              name = userlog_event_types[event_type],
              value = stats[event_type])

        await ctx.send(embed = embed)

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["warnscount"])
    async def warncount(self, ctx, user: discord.Member = None):
        """Get a count of how many warns a user has made."""
        if user is None:
            user = ctx.author

        event_type = "warns"
        stats = self.get_stats_for_id(user.id, [event_type])

        embed = discord.Embed(
            colour = 0xF92672,
            title = f"🔨 {user.name} {userlog_event_types[event_type]} Stats")
        embed.add_field(
            name = userlog_event_types[event_type],
            value = stats[event_type])

        await ctx.send(embed = embed)

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["mutescount"])
    async def mutecount(self, ctx, user: discord.Member = None):
        """Get a count of how many mutes a user has made."""
        if user is None:
            user = ctx.author

        event_type = "mutes"
        stats = self.get_stats_for_id(user.id, [event_type])

        embed = discord.Embed(
            colour = 0xF92672,
            title = f"🔨 {user.name} {userlog_event_types[event_type]} Stats")
        embed.add_field(
            name = userlog_event_types[event_type],
            value = stats[event_type])

        await ctx.send(embed = embed)

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["kickscount"])
    async def kickcount(self, ctx, user: discord.Member = None):
        """Get a count of how many kicks a user has made."""
        if user is None:
            user = ctx.author

        event_type = "kicks"
        stats = self.get_stats_for_id(user.id, [event_type])

        embed = discord.Embed(
            colour = 0xF92672,
            title = f"🔨 {user.name} {userlog_event_types[event_type]} Stats")
        embed.add_field(
            name = userlog_event_types[event_type],
            value = stats[event_type])

        await ctx.send(embed = embed)

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["banscount"])
    async def bancount(self, ctx, user: discord.Member = None):
        """Get a count of how many bans a user has made."""
        if user is None:
            user = ctx.author

        event_type = "bans"
        stats = self.get_stats_for_id(user.id, [event_type])

        embed = discord.Embed(
            colour = 0xF92672,
            title = f"🔨 {user.name} {userlog_event_types[event_type]} Stats")
        embed.add_field(
            name = userlog_event_types[event_type],
            value = stats[event_type])

        await ctx.send(embed = embed)

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["notescount"])
    async def notecount(self, ctx, user: discord.Member = None):
        """Get a count of how many notes a user has made."""
        if user is None:
            user = ctx.author

        event_type = "notes"
        stats = self.get_stats_for_id(user.id, [event_type])

        embed = discord.Embed(
            colour = 0xF92672,
            title = f"🔨 {user.name} {userlog_event_types[event_type]} Stats")
        embed.add_field(
            name = userlog_event_types[event_type],
            value = stats[event_type])

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(ModStats(bot))
