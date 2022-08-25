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


def main():
    load_dotenv()
    
    print(bad_words)

    intents = discord.Intents.default()

    client = PMO(intents=intents)
    client.run(os.getenv('BOT_TOKEN'))


if __name__ == '__main__':
    main()
