import discord
from discord.ext import commands
import responses
import bot_token



async def send_message(message, user_message, is_private):
    try:

        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as err:
        print(err)


def run_bot():

    TOKEN = bot_token.TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)




    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str (message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if(user_message[0] == '?'):
            user_message = user_message[1:]
            await send_message(message,user_message, is_private=True)
        else:
            await send_message(message,user_message, is_private=False)




    client.run(TOKEN)


def voice_bot():

    TOKEN = bot_token.TOKEN
    intents = discord.Intents.all()
    client = commands.Bot(command_prefix = '!', intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.command(pass_context=True)
    async def join(ctx):
        if(ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("Join a voice channel to run this command")

    @client.command(pass_context = True)
    async def leave(ctx):
        if(ctx.voice_client):
            channel = ctx.guild.voice_client
            await channel.disconnect()
            await ctx.send("left voice channel")
        else:
            await ctx.send("Oops, I am not in a voice channel")
    


    client.run(TOKEN)