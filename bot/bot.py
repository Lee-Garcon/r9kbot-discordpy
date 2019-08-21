import discord
import sqlalchemy
import re
from config import config_get

from db import Session, reset_db, Message

reset_db()
s = Session()

config = config_get()

def all(iterable, func):
    for x in iterable:
        if not func(x):
            return False
    return True

def strip(iterable):
    for x in iterable:
        yield x.strip()

class R9kBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if config.get('channels-whitelist') and message.channel.name not in strip(config.get('channels-whitelist').split(',')):
            return

        if config.get('channels-blacklist') and message.channel.name in strip(config.get('channels-blacklist').split(',')):
            return

        content = message.content
        mentions = message.mentions
        bot_mention = lambda user: not user.bot
        if all(mentions, bot_mention):
            return

        if message.author.bot:
            return

        if len(message.attachments) > 0:
            return

        r = s.query(Message).filter(Message.message.ilike(content)).one_or_none()
        if r:
            channel = message.channel
            await message.delete()
            await channel.say('{0} Your message has been deleted as an identical message has been sent already.'.format(author.mention))
        else:
            db_entry = Message(username=message.author.name, message=content)
            s.add(db_entry)
            s.commit()

client = R9kBot()
client.run(config['token'])

s.close()
