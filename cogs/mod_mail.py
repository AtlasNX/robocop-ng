import config
import discord
from discord.ext import commands
from discord.ext.commands import Cog
from helpers.checks import check_if_verified_or_dms
from helpers.userlogs import get_blank_userlog, get_userlog, set_userlog
import json
import time


class ModMail(Cog):
    def __init__(self, bot):
        self.bot = bot

    def add_mail_log(self, uid, message):
        userlogs = get_userlog()
        uid = str(uid)

        if uid not in userlogs:
            userlogs[uid] = get_blank_userlog()

        userlogs[uid]["mail"].append(message)
        set_userlog(json.dumps(userlogs))

    def build_embed(self, author, message):
        embed = discord.Embed(description=message["body"],)
        embed.set_author(
            name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url
        )
        embed.colour = self.get_message_color(message)
        embed.set_footer(text=f"{self.get_message_icon(message)} - {author.id}")
        return embed

    def get_message_color(self, message):
        if message["resolved"] == True:
            return 0x4CAF50
        elif message["replier_id"] != 0:
            return 0x2196F3
        else:
            return 0xE91E63

    def get_message_icon(self, message):
        if message["resolved"] == True:
            return "✔️"
        elif message["replier_id"] != 0:
            return "↩️"
        else:
            return "✉️"

    # Commands

    @commands.check(check_if_verified_or_dms)
    @commands.command(aliases=["creport"])
    async def modmail(self, ctx, *, body: str = ""):
        """Sends a mod mail message"""

        # We should probably delete the message for privacy.
        if ctx.guild:
            await ctx.message.delete()

        # Prevent sending of blank messages.
        if len(body.strip()) == 0:
            await ctx.send("A message can not be empty.")
            return
        # Limit message to 2048 characters to not go over the embed limit.
        if len(body.strip()) > 2048:
            await ctx.send("A message can not be longer than 2048 characters.")
            return

        logs = get_userlog()
        uid = str(ctx.author.id)

        # Get the timeout from the config and default it to 15 seconds.
        timeout = getattr(config, "modmail_timeout", 15)

        # Make sure our user exists in the userlog, and they've sent a message before.
        if uid in logs and "mail" in logs[uid] and len(logs[uid]["mail"]) != 0:
            last_message = logs[uid]["mail"][-1]

            # Prevents sending the same message.
            if last_message["body"].strip() == body.strip():
                await ctx.send("Unable to send message.")
                return

            # Rate limit messages.
            delta_time = int(time.time()) - last_message["timestamp"]
            if delta_time < timeout:
                await ctx.send(
                    f"Please wait {timeout - delta_time} seconds before sending another message."
                )
                return

        message = {
            "body": body.strip(),
            "timestamp": int(time.time()),
            "resolved": False,
            "replier_id": 0,
            "replier_name": "",
            "message_id": 0,
        }

        # Send message
        modmail_channel = self.bot.get_channel(config.modmail_channel)
        message["message_id"] = (
            await modmail_channel.send(embed=self.build_embed(ctx.author, message))
        ).id

        # Log messages to the userlog.
        self.add_mail_log(uid, message)

        await ctx.send(f"{ctx.author.mention} - Message sent.")

    @commands.check(check_if_verified_or_dms)
    @commands.command(aliases=["solved", "completed"])
    async def resolved(self, ctx):
        """Marks your last mod mail message as resolved"""

        # We should probably delete the message for privacy.
        await ctx.message.delete()

        logs = get_userlog()
        uid = str(ctx.author.id)

        if uid not in logs or "mail" not in logs[uid] or len(logs[uid]["mail"]) == 0:
            await ctx.send("No mod mail message to mark as resolved.")
            return

        if logs[uid]["mail"][-1]["resolved"]:
            await ctx.send("Last mod mail message is already marked as resolved.")
            return

        logs[uid]["mail"][-1]["resolved"] = True
        set_userlog(json.dumps(logs))

        modmail_channel = self.bot.get_channel(config.modmail_channel)
        message = await modmail_channel.fetch_message(logs[uid]["mail"][-1]["message_id"])
        await message.edit(embed=self.build_embed(ctx.author, logs[uid]["mail"][-1]))

        await ctx.send(f"{ctx.author.mention} - Message marked as resolved.")


def setup(bot):
    bot.add_cog(ModMail(bot))
