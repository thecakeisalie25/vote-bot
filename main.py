import discord
from discord import TextChannel, Message, User, Guild
from textwrap import dedent
import typing
from discord.ext.commands import Bot, Context
with open("token.txt") as file:
	TOKEN = file.read().strip()

bot = Bot(command_prefix="v-", case_insensitive = True)

@bot.event
async def on_ready():
	owner = (await bot.application_info()).owner
	print(dedent("""\
		--- We're online and running! ---
		Logged in as {}
		User ID: {}
		Owner: {}
		---------------------------------\
		""".format(
			bot.user, bot.user.id, owner
		)))

async def ask(
	context: Context,
	question: str, 
	validator = lambda response: True,
	invalid_string = "Sorry, that's not a valid response. "
	) -> str:
	
	user = await context.author()
	
	


@bot.command(aliases = ["mkch", "mkchannel"], brief = "Nope, not yet.")
async def addChannel(context: Context):
	context.send("Sorry, placeholder.")
	pass;


@bot.command(brief = "hello my friend")
async def ping(context: Context):
	await context.channel.send("i am going to yeet")





bot.run(TOKEN)