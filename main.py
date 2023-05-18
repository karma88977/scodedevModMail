import discord
from discord.ext import commands
import logging
import datetime

bot = commands.Bot(commands.when_mentioned_or("!send "), case_insensitive=True, intents=discord.Intents.all())
bot.remove_command("help")



@bot.event
async def on_ready():
    now = datetime.datetime.now()
    print(f"""--------------------------------------
    \nBot wurde gestartet um {now.strftime('%H:%M:%S %d-%m-%Y')}
    \nEingeloggt als:\n{bot.user.name}
    \nBot ID:\n{bot.user.id}
    \n--------------------------------------""")
    change_status.start()
    channel = bot.get_channel(EURE KANAL ID)
    embed = discord.Embed(description=f".... wurde erfolgreich gestartet um {now.strftime('%H:%M:%S %d-%m-%Y')}", color=0xff0000)
    await channel.send(embed=embed)

def check_team(ctx):             #SERVERID#          #TEAMROLLENID#
    return bot.get_guild(746093304273436762).get_role(1015962859752132628) in ctx.author.roles

@bot.event
async def on_connect():
    print('ModMail Blue')


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if message.author != message.author.bot:
        if not message.guild:   #SERVERID#                        #EMPFANGSKANALID#
            await bot.get_guild(746093304273436762).get_channel(1016797717600669766).send(
                f'User menition {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n\n_**Nachricht**_\n{message.content}')
    await bot.process_commands(message)


@bot.command()
@commands.check(check_team)
async def pn(ctx, member: discord.Member, *, text):
    await member.send(text)


@bot.event
async def on_resumed():
    print('reconncted')

bot.run("TOKEN")
