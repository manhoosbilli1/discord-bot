"""This is a cog for a discord.py bot.
Commands:
    None

"""
from discord.ext import commands
from discord import DMChannel


# set up log path
LOG_FILENAME = '../logs/discord_chat.log'


class ChatLog(commands.Cog, name='Chat Log'):
    def __init__(self, client):
        self.client = client
        self.logfile = open(LOG_FILENAME, 'a', encoding='utf-8')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            # Dont log messages of bots
            return
        if isinstance(msg.channel, DMChannel):
            # Don't log DMs
            return
        if not msg.channel.guild.id == self.client.main_guild.id:
            # Don't log messages on servers other than the main server
            return
        paginator = [
            msg.created_at.isoformat(),
            str(msg.channel),
            f'{msg.author.name}#{msg.author.discriminator}',
            msg.content.replace('\n', '\\n'),
            msg.author.id
        ]
        self.logfile.write('|'.join(paginator[:-1]) + '\n')
        self.logfile.flush()

        # send chat message to emkc
        if not msg.channel.guild.id == 473161189120147456:
            # prevent querying the emkc api if it's not felix
            return


async def setup(client):
    await client.add_cog(ChatLog(client))