import discord
import os
import requests
import json


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_Joke():
  response = requests.get("https://api.chucknorris.io/jokes/random")
  json_data = json.loads(response.text)
  joke = json_data['value']
  return joke

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$chuck'):
    await message.channel.send(get_Joke())


try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e



