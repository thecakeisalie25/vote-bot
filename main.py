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
	validator = lambda message : True, # f(str) -> bool """Returns True if this message is a valid response"""
	author_only = True,
	) -> str:
	
	# user = await context.author()
	def check(author):
		def trueCheck(message):
			return (message.author == author or not author_only) and validator(str(message.content))
		return trueCheck
	ping: str = ""
	if context.channel.type == discord.ChannelType.private:
		ping += "<@{}> ".format(context.author.id)
	await context.send((ping if ping else "") + question)
	try:
		return await bot.wait_for("message", check = check(context.author), timeout=5)
	except:
		await context.send("Sorry, you've timed out.")
	
@bot.command(aliases = ["mkch", "mkchannel"], brief = "Nope, not yet.")
async def addChannel(context: Context):
	await context.send("Sorry, placeholder.")
	pass;


@bot.command(aliases = ["tAsk"], brief = "Test of the ask parameters function.",
	description = " --- testAsk - Just a simple test command, for asking questions ---",
	help = dedent("""\
		Tests the ask() function, which asks the user a question and validates the response."""))
async def testAsk(context: Context):
	def testInt(msg): 
		try:
			int(msg)
			return True
		except:
			return False
	tempInt = await ask(context, "Please enter a number, anything else will be ignored.", validator=testInt)
	if tempInt:
		await context.send("You entered: " + tempInt.content)

@bot.command(brief = "hello my friend")
async def ping(context: Context):
	await context.channel.send("i am going to yeet")





bot.run(TOKEN)