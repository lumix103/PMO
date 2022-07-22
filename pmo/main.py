import discord
import os
from dotenv import load_dotenv


class PMO(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


def main():
    load_dotenv()

    intents = discord.Intents.default()

    client = PMO(intents=intents)
    client.run(os.getenv('BOT_TOKEN'))


if __name__ == '__main__':
    main()
