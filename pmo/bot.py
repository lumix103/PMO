import discord
import os
from dotenv import load_dotenv

bad_words = []

with open('pmo\\bad_words.txt') as file:
    bad_words = file.readlines()
    bad_words = [word.strip() for word in bad_words]

class PMO(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        msg_ctx = message.content.strip().lower()
        if [i for i in bad_words if i in msg_ctx]:
            await message.delete()
            await message.channel.send(
                    "That's a bad word. Please dont say more bad words"
                    )
    async def on_member_join(self, member):
        welcome_channel = next(( 
            chan for chan in member.guild.channels if chan.name == "welcome"))
        if not welcome_channel is None:
            await welcome_channel.send(f'Welcome to the server {member.display_name}')


def main():
    load_dotenv()
    
    print(bad_words)

    intents = discord.Intents(messages=True, guilds=True, members=True)

    client = PMO(intents=intents)
    client.run(os.getenv('BOT_TOKEN'))


if __name__ == '__main__':
    main()
