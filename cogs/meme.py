import random
import discord
from discord.ext import commands
from discord.ext.commands import Cog
import math
import platform
from helpers.checks import check_if_staff_or_ot
from helpers.checks import check_if_staff


class Meme(Cog):
    """
    Meme commands.
    """

    def __init__(self, bot):
        self.bot = bot

    def c_to_f(self, c):
        """this is where we take memes too far"""
        return math.floor(9.0 / 5.0 * c + 32)

    def c_to_k(self, c):
        """this is where we take memes REALLY far"""
        return math.floor(c + 273.15)

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, name="warm")
    async def warm_member(self, ctx, user: discord.Member):
        """Warms a user :3"""
        celsius = random.randint(15, 100)
        fahrenheit = self.c_to_f(celsius)
        kelvin = self.c_to_k(celsius)
        await ctx.send(f"{user.mention} warmed."
                       f" User is now {celsius}°C "
                       f"({fahrenheit}°F, {kelvin}K).")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, name="chill", aliases=["cold", "cool"])
    async def chill_member(self, ctx, user: discord.Member):
        """Chills a user >:3"""
        celsius = random.randint(-50, 15)
        fahrenheit = self.c_to_f(celsius)
        kelvin = self.c_to_k(celsius)
        await ctx.send(f"{user.mention} chilled."
                       f" User is now {celsius}°C "
                       f"({fahrenheit}°F, {kelvin}K).")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, aliases=["thank", "reswitchedgold"])
    async def gild(self, ctx, user: discord.Member):
        """Gives a star to a user"""
        await ctx.send(f"{user.mention} gets a :star:, yay!")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, aliases=["atlassilver", "silv3r",
                                            "atlassilv3r"])
    async def silver(self, ctx, user: discord.Member):
        """Gives a user AtlasNX Silver™"""
        embed = discord.Embed(title="AtlasNX Silver™!",
                              description=f"Here's your AtlasNX Silver™,"
                                          f"{user.mention}!")
        embed.set_image(url="https://cdn.discordapp.com/emojis/629188608732954635.png?v=1")
        await ctx.send(embed=embed)

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True)
    async def btwiuse(self, ctx):
        """btw i use arch"""
        uname = platform.uname()
        await ctx.send(f"BTW I use {platform.python_implementation()} "
                       f"{platform.python_version()} on {uname.system} "
                       f"{uname.release}")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True)
    async def yahaha(self, ctx):
        """secret command"""
        await ctx.send(f"🍂 you found me 🍂")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True)
    async def peng(self, ctx):
        """heck tomger"""
        await ctx.send(f"🐧")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, aliases=["outstanding"])
    async def outstandingmove(self, ctx):
        """Posts the outstanding move meme"""
        await ctx.send("https://cdn.discordapp.com/attachments"
                       "/371047036348268545/528413677007929344"
                       "/image0-5.jpg")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True)
    async def bones(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/"
                       "443501365843591169.png?v=1")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True)
    async def headpat(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/"
                       "465650811909701642.png?v=1")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, aliases=["when", "etawhen",
                                            "emunand", "thermosphere", "emummc"])
    async def eta(self, ctx):
        await ctx.send(random.choice(["15th June", "June 15th", "Wednesday.", "Tuesday."]))

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, name="bam", aliases=["boom"])
    async def bam_member(self, ctx, target: discord.Member):
        """Bams a user owo"""
        safe_name = await commands.clean_content().convert(ctx, str(target))
        await ctx.send(f"{safe_name} is ̶n͢ow b̕&̡.̷ 👍̡")

    @commands.command(hidden=True)
    async def memebercount(self, ctx):
        """Checks memeber count, as requested by dvdfreitag"""
        await ctx.send("There's like, uhhhhh a bunch")

    @commands.command(hidden=True)
    async def frolics(self, ctx):
        """test"""
        await ctx.send("https://www.youtube.com/watch?v=VmarNEsjpDI")
    
    @commands.check(check_if_staff)
    @commands.command(hidden=True, aliases=['bs', "biracy", ":b:iracy", "🅱iracy"])
    async def batches(self, ctx):
        """Yeet"""
        await ctx.send("🅱or 🅱irated 🅱shop-🅱ames 🅱ou 🅱eed 🅱S 🅱ignature 🅱atches. 🅱s 🅱heir 🅱nly 🅱urpose 🅱s 🅱o 🅱llow 🅱iracy 🅱e\'re 🅱ot 🅱roviding 🅱ny 🅱elp 🅱ith 🅱nstallation 🅱f 🅱aid 🅱atches 🅱r 🅱irated 🅱ames 🅱fterwards")
        
    @commands.check(check_if_staff)
    @commands.command(hidden=True, aliases=['bxfat', "bsfat"])
    async def bat32(self, ctx):
        """Epic"""
        await ctx.send("🅱he 🅱xFAT 🅱rivers 🅱uilt 🅱nto 🅱he 🅱witch 🅱as 🅱een 🅱nown "
                      "🅱o 🅱orrupt 🅱D 🅱ards 🅱nd 🅱omebrew 🅱nly 🅱akes 🅱his 🅱orse. "
                      "🅱ackup 🅱verything 🅱n 🅱our 🅱D 🅱ard 🅱s 🅱oon 🅱s 🅱ossible "
                      "🅱nd 🅱ormat 🅱t 🅱o 🅱AT32. 🅱n 🅱indows, 🅱f 🅱our 🅱D 🅱ard 🅱s "
                      "🅱ver 🅱2GB 🅱hen 🅱t 🅱ill 🅱ot 🅱et 🅱ou 🅱elect 🅱AT32 🅱rom "
                      "🅱he 🅱uilt-🅱n 🅱ormat 🅱ool, 🅱owever 🅱ou 🅱an 🅱se 🅱 🅱ool "
                      "🅱ike 🅱UIFormat 🅱o 🅱ormat 🅱t.")
        
    @commands.check(check_if_staff)
    @commands.command(hidden=True, aliases=['toilet'])
    async def flush(self, ctx, target: discord.Member):
        """Flushes Lucy uwu"""
        safe_name = target.display_name
        await ctx.send(random.choice([f"thats a bit rude, {safe_name}", f"wait no, dont shower {safe_name}. youll die", "i think i might have done that drug before, not sure tho"]))


def setup(bot):
    bot.add_cog(Meme(bot))
