import discord
from discord.ext import tasks
from datetime import datetime
import pytz

# PST timezone
pst_timezone = pytz.timezone("US/Pacific")

# channel int
channel_id = 1403213173875806370

# seth id
user_id = 753004547248619532
mention = f"<@{user_id}>"

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.check_time.start()
        
    async def on_message(self, message):
        if message.author == self.user:
            return
        elif message.lower == 'house':
            await message.channel.send(f'More mouse bites, {message.author}!')
            
    @tasks.loop(seconds=30) # check twice per min
    async def check_time(self):
        now = datetime.now(pst_timezone)
        
        if now.hour == 19 and now.minute == 00:
            channel = self.get_channel(channel_id)
            if channel:
             await channel.send(
                f"{mention} You know what's funnier than one seizure? go take your meds"
             )

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
import os
TOKEN = os.getenv("DISCORD_TOKEN") # gets the token from Railway
client.run(TOKEN)
