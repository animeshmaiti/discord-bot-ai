from dotenv import load_dotenv
import discord
import os
import openai


def configure():
    load_dotenv()


configure()
openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("DISCORD_BOT_API_KEY")

# def test_openai_api():
#     try:
#         response = openai.Completion.create(
#             engine="davinci",
#             prompt="Hello, OpenAI!",
#             max_tokens=10
#         )
#         completion_text = response.choices[0].text.strip()
#         print(f"OpenAI API test successful. Response: {completion_text}")
#     except Exception as e:
#         print(f"OpenAI API test failed. Error: {str(e)}")

# test_openai_api()



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if self.user != message.author:
            if self.user in message.mentions:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=message.content,
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                channel = message.channel
                messageToSend = response.choices[0].text
                await channel.send(messageToSend)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
