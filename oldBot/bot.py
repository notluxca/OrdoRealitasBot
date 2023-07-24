import discord
import responses


# Send messages
async def send_message(userName,message, user_message, is_private):
    try:
        response = responses.handle_response(user_message, userName)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


    
    


def run_discord_bot():
    TOKEN = 'MTEyMDE4NTc3MzE4Mjk1OTY3OA.G_swzY.ZQbjbUk7O3TW4dtSFi2oV_0pM7Ay5eBgRspJ9s'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username}: ")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(username ,message, user_message, is_private=False)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)
