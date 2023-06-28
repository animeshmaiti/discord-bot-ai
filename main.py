# This example requires the 'message_content' intent.
# PERMISSIONS INTEGER=534723950656
from dotenv import load_dotenv
import discord
import os
import openai

openai.api_key = os.getenv(OPENAI_API_KEY)

def configure():
    load_dotenv()


configure()
TOKEN = os.getenv('DISCORD_BOT_API_KEY')
print(TOKEN)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        chanel = message.channel
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.content,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        messageToSend = response.choices[0].text
        await chanel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
