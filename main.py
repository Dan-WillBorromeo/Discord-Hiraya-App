import discord, os, logging, asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content=True

bot = commands.Bot(command_prefix="!", intents=intents, log_handler=handler, log_level=logging.DEBUG)
init_ext = ["cogs.dice", "cogs.shiver"]

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to go in, boss!")

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     await bot.process_commands(message)

async def load_extensions():
    for ext in init_ext:
        try:
            await bot.load_extension(ext)
            print(f"Loaded {ext}")
        except Exception as exception:
            print(f"Failed to load {ext}: {exception}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

if __name__=="__main__":
    asyncio.run(main())