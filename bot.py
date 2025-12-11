import os
import discord
from discord.ext import tasks
from datetime import datetime
import random
import pytz

# parsing in DMS Disorders for !Diagnose CMD
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "DSM_Disorders.txt")
print("File path:", file_path)
print("File exists:", os.path.exists(file_path)) # outputs if we see the disorder file

def parse_file(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line:
                parts = cleaned_line.split(',')
                disorder = parts[0].strip()
                data.append(disorder)
    
    return data
disorder_array = parse_file(file_path)
index = random.randint(0,145)
# PST timezone
pst_timezone = pytz.timezone("US/Pacific")

# channel int
channel_id = 1403213173875806370

# seth id
user_id = 753004547248619532
mention = f"<@{user_id}>"

# keywords
help_keyword = 'words'
keyword_house = 'house'
keyword_doctor = 'doctor'
keyword_dr = 'dr'
keyword_doctuh = 'doctuh'
keyword_housenberg = "you're housenberg"
keyword_lupus = 'lupus'
keyword_diagnose = '!diagnose'

# insult generator
insult_array = []
insult_array.append(', ARE YOU BEING INTENTIONALLY DENSE?')
insult_array.append(", I'm sorry, I'm about to lose you because I'm about to drive into a tunnel in a canyon on an airplane while hanging up on you.")
insult_array.append(', I hate tea.')
insult_array.append(', sometimes the best gift is the gift of never seeing you again.')
insult_array.append(', gotta go! Building full of sick people, if I hurry, maybe I can avoid them.')
insult_array.append(', you are turning white.')
insult_array.append(', you must be full of bologna. Lot of it.')
insult_array.append(', if your DNA was off by one percentage point, you would be a dolphin.')
insult_array.append(', good news is, you are running out of organs to fail.')
insult_array.append(', speaking of which, if you are particularly annoying, you may see me reach for this - this is Vicodin. Its mine.')
insult_array.append(', you think your dad wants to kill you because youre so ugly? Be grateful, anywhere else in the animal kingdom, your parents wouldve eaten you at birth.')
insult_array.append(', good thing I brought my Axe-Cane.')

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.last_sent_date = None
        self.check_time.start()
        
    async def on_message(self, message):
        if message.author == self.user:
            return
            
            # HELP CMD
        elif message.content.lower() == help_keyword:
            await message.channel.send("Doctor House Commands\n_________________\n1.) words\n2.) house/doctor/dr\n3.) lupus\n4.)!Diagnose")

            # DR HOUSES NAME CMD
        elif keyword_housenberg.lower() in message.content.lower():
            await message.channel.send("You're goddamn right")

        elif keyword_doctor.lower() in message.content.lower():
            await message.channel.send(f'{message.author}. You have herpes')

        elif keyword_dr.lower() in message.content.lower():
            await message.channel.send(f'{message.author}, somewhere out there, there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology.')

        elif keyword_doctuh.lower() in message.content.lower():
            await message.channel.send('Say my name')
            
        elif keyword_house.lower() in message.content.lower():
            await message.channel.send(f'More mouse bites, {message.author}!')

            
            # LUPUS CMD && !Diagnose CMD
        if keyword_lupus.lower() in message.content.lower():
            await message.channel.send('It is NEVER lupus.')

        if keyword_diagnose.lower() in message.content.lower():
            index = random.randint(0,145)
            mean_index = random.randint(0, 11)
            await message.channel.send(f'You have {disorder_array[index]}{insult_array[mean_index]}')
            
    @tasks.loop(seconds=30) # check twice per min
    async def check_time(self):
        now = datetime.now(pst_timezone)
        if now.hour == 19 and now.minute == 0:
            if self.last_sent_date != now.date():
                channel = self.get_channel(channel_id)
                if channel:
                    await channel.send(f"{mention} You know what's funnier than one seizure? go take your meds")
                self.last_sent_date = now.date()

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN") # gets the token from Railway
client.run(TOKEN)
