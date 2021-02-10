############################
#                          #
#   Mr RoBOT Discord Bot   #
#       by veasman         #
#                          #
############################

import discord
from discord.ext import commands
import os
import subprocess
import re
import sys
#from cleverbot_free.cbaio import CleverBot
#import asyncio
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

bot = commands.Bot(command_prefix = 'sudo ') # hehe

#cb = CleverBot()

#chatbot = ChatBot('Mr RoBOT')
#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train('chatterbot.corpus.english')

command_dict = dict()

@bot.event
async def on_ready():
    print('Bot is online.')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

# Cleverbot thing
#@bot.event
#async def on_message(message):
#    if message.channel.id != 806046043673853993:
#        pass
#
#    if message.author.id == 805901549518716978:
#        pass
#
#    #response = chatbot.get_response(message.content)
#    cb.init()
#
#    async with message.channel.typing():
#        response = cb.getResponse(message.content)
#
#    await message.channel.send(response)

#@bot.command()
#async def load(ctx, extension):
#    bot.load_extension(f'cogs.{extension}')

#@bot.command()
#async def unload(ctx, extension):
#    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')



command_dict['version'] = 'Gets my version'
@bot.command(description='Get version')
async def version(ctx):
    await ctx.send('Mr RoBOT version 1.0')

command_dict['echo'] = 'I will say whatever you tell me to'
@bot.command()
async def echo(ctx, *, out):
    await ctx.send(out)

# Clear messages in current channel
@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

# Kick a member
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

# Ban a member
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    mbmer_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member.name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

# TODO: run compiler in a docker to protect local files
command_dict['python'] = 'Run user-provided python code'
@bot.command(aliases=['py'])
async def pythonOld(ctx, *, code):
    with open('python.py', 'w') as f:
        code = re.sub('```py|```python|thon|```', '', code)
        f.write(code)
    try:
        cmd = ['python3', 'python.py']
        output = subprocess.run(cmd, stdout=subprocess.PIPE)
        result = output.stdout.decode('utf-8')

        await ctx.send(result)
    except Exception as e:
        await ctx.send(e)

    with open('python.py', 'r+') as f:
        f.truncate()

@bot.command(aliases=['c++'])
async def cpp(ctx, *, code):
    with open('cpp.cpp', 'w') as f:
        code = re.sub('```cpp|```c++|```', '', code)
        f.write(code)

    try:
        compile_cmd = ['g++ cpp.cpp -o cpp']
        run_cmd = ['./cpp']
        subprocess.run(compile_cmd, stdout=subprocess.PIPE)
        outpupt = subprocess.run(run_cmd, stdout=subprocess.PIPE)
        result = output.stdout.decode('utf-8')
        await ctx.send(result)
    except:
        await ctx.send(sys.exc_info())

    with open('cpp.cpp', 'r+') as f:
        f.truncate()

    os.remove('cpp')

# For cogs (load & unload commands)
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#@bot.event
#async def on_message(message):
#    if message.channel.id != 806046043673853993:
#        return
#
#    if message.author.id == 805901549518716978:
#        return
#
#    cb.init()
#
#    async with message.channel.typing():
#        response = cb.getResponse(message.content)
#
#    await message.channel.send(response)

bot.run('ODA1OTAxNTQ5NTE4NzE2OTc4.YBhoTg.Uaq0xW7zG_DN1-T9CxoRCKJrkWs')
