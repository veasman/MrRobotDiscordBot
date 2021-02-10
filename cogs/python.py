import discord
from discord.ext import commands
import re
import subprocess as sp

class Python(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Python Cog Loaded!')

    @commands.command()
    async def python(self, ctx, *, code):
        with open('to-compile.py', 'w') as f:
            code = re.sub('```py|```python|thon|```', '', code)
            f.write(code)
        try:
            cmd = ['to-compile.py']
            output = sp.run(cmd, stdout=sp.PIPE)
            result = output.stdout.decode('utf-8')
            await ctx.send(result)
        except:
            await ctx.send('Syntax error!')

        with open('to-compile.py', 'r+') as f:
            f.truncate()

def setup(client):
    client.add_cog(Python(client))
