from discord.ext import commands
from utils.roller import rollDice

class Dice (commands.Cog):
    def __init__(self, bot):
        self.bot = bot # type: ignore
    
    @commands.command(name="roll")
    async def roll(self, ctx, expression: str):
        rolls, total = result = rollDice(expression)

        if result is None:
            await ctx.send("Invalid dice expression.")
            return
        
        await ctx.send(f"Rolls: {rolls}\nTotal: {total}")

async def setup(bot):
    await bot.add_cog(Dice(bot))