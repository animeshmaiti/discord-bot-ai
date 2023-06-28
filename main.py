from dotenv import load_dotenv
import discord
import os
import openai

chat = ""
def configure():
    load_dotenv()


configure()
openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("DISCORD_BOT_API_KEY")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        try:
            chat += f"{message.author}: {message.content}\n"
            print(f'Message from {message.author}: {message.content}')
            if self.user != message.author:
                if self.user in message.mentions:
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"{chat}\nAiChat: ",
                        temperature=1,
                        max_tokens=256,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    channel = message.channel
                    messageToSend = response.choices[0].text
                    await channel.send(messageToSend)
        except Exception as e:
            print(e)
            chat = ""

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
