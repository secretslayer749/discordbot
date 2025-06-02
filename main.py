import discord
import os

TOKEN = os.getenv("TOKEN")  # Railway environment variable

OWNER_ID = 984152481225404467
GUILD_ID = 1032670610372968529
CHANNEL_ID = 1108669775099461633

client = discord.Client()

@client.event
async def on_ready():
    print(f"Selfbot logged in as {client.user} (ID: {client.user.id})")

@client.event
async def on_message(message):
    if message.author.id != OWNER_ID:
        return

    if (
        message.content.startswith('$trep')
        and message.guild
        and message.guild.id == GUILD_ID
        and message.channel.id == CHANNEL_ID
    ):
        if message.mentions:
            mentioned_user = message.mentions[0]
            await message.channel.send(f"t!rep {mentioned_user.mention}")
        else:
            await message.channel.send("Please mention a user to rep.")

client.run(TOKEN, bot=False)  # Important for selfbot
