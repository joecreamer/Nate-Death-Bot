import discord
from dotenv import load_dotenv
import time

import web

load_dotenv()
TOKEN = "ODkyOTQ2Nzk0ODM5OTUzNDEw.YVUTgg.LiG_DvWHuJMUH_QMhJdoT5HK8XY"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(892948194042998799)  
    old_uid = ""

    while True:
        print(old_uid)
        with open("uid", "r") as f:
            uid = f.read()
        if uid != old_uid:
            print("kdr is loading")
            kdr = web.get_kdr()
            print("kdr is done loading")
            if kdr <= 0.5:
                await channel.send(f'Nate is a tard and only got a {kdr} kdr, he is a tard {uid}')
            elif kdr > .5:
                await channel.send(f'Nate got a {kdr} kdr, he is not that much of a tard, but still is one {uid}')

            old_uid = uid

        time.sleep(5)


client.run(TOKEN)