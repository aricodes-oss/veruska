import discord

from .client import client
from .constants import DISCORD_BOT_TOKEN, BOT_TESTING_CHANNEL, PLAY_CMD, LIST_CMD
from .voice import handle_play, handle_list

COMMANDS = {PLAY_CMD: handle_play, LIST_CMD: handle_list}


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return

    cmd = message.content.lower().split(" ")[0]
    handler = COMMANDS.get(cmd)

    if handler is not None:
        await handler(message)

    if message.channel.id == BOT_TESTING_CHANNEL:
        await message.delete()


def main() -> None:
    client.run(DISCORD_BOT_TOKEN)
