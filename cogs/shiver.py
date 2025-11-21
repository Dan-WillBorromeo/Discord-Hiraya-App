import discord
from discord.ext import commands
from utils.shiverDice import rollShiver
from utils.imageTools import mergeImagesHorizontal

class ShiverCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shiver")
    async def shiver(self, ctx, *, expression: str):
        results = rollShiver(expression)
        if results is None:
            await ctx.send("Invalid expression.")
            return
        
        await ctx.message.delete()

        names = [name for name, path in results]
        paths = [path for name, path in results]

        merged = mergeImagesHorizontal(paths, "merged.png")
        file = discord.File(merged, filename="merged.png")

        await ctx.send(content=ctx.author.mention,file=file)

async def setup(bot):
    await bot.add_cog(ShiverCog(bot))
