import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='!sm:')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print ('-------')

@bot.event
async def on_message_edit(old, new):
    msg=new
    if not msg.author.bot:
        return
    if msg.channel.id not in [channel_id]:
        return
    if not new.embeds:
        return
    embed=new.embeds[0]
    user=str(embed.title)
    AofM=int(embed.description)
    if AofM < 0:
        return
    with open("currency.json") as f:
        df = json.load(f)
    df.setdefault(user, 0)
    df[user] += AofM
    f = open(r"currency.json", 'w')
    json.dump(df, f, indent=4)

bot.run(Token)
