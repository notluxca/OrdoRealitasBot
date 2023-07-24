import os
import discord
import responses






def run_discord_bot():
    TOKEN = 'MTEyMDE4NTc3MzE4Mjk1OTY3OA.GLtPyp.NCmsImVagA79vcofxl33kwvHyed0D5T44-vtbE'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    # Assim que o bot iniciar
    @client.event
    async def on_ready():
        os.system("cls")
        print(""" _____           _         ___                  _       _                         _             _   
(  _  )         ( )       |  _`\               (_ )  _ ( )_                      ( )           ( )_ 
| ( ) | _ __   _| |   _   | (_) )   __     _ _  | | (_)| ,_)   _ _   ___  ______ | |_      _   | ,_)
| | | |( '__)/'_` | /'_`\ | ,  /  /'__`\ /'_` ) | | | || |   /'_` )/',__)(______)| '_`\  /'_`\ | |  
| (_) || |  ( (_| |( (_) )| |\ \ (  ___/( (_| | | | | || |_ ( (_| |\__, \        | |_) )( (_) )| |_ 
(_____)(_)  `\__,_)`\___/'(_) (_)`\____)`\__,_)(___)(_)`\__)`\__,_)(____/        (_,__/'`\___/'`\__)
                                                                                                    
                                                                                                    """)
        print(f'{client.user} está online!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return
        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        response = responses.handle_response(message)

        # ignora mensagens inuteis
        if response == "":
            return
        # Identifica se a mensagem é um Embed pra enviar ela da forma correta
        if type(response) == discord.Embed:
            await message.channel.send(embed=response)
        else:
            await message.channel.send(response)
        #await message.channel.send(response)
    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)


    

run_discord_bot()
