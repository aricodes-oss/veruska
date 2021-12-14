from asyncio import sleep
from contextlib import suppress
from typing import Optional
import glob
import os

import discord
from use_dir import use_dir

from .constants import AUDIO_FILES_DIR, PLAY_CMD


def _get_files() -> list[str]:
    with use_dir(AUDIO_FILES_DIR):
        return glob.glob("*")


def _match_track(track: str) -> Optional[str]:
    available_tracks = _get_files()
    found = None

    # Only match the first substr
    for file_name in available_tracks:
        if file_name.lower().startswith(track.lower()):
            found = file_name
            break

    return found


async def handle_play(message: discord.Message) -> None:
    voice_status = message.author.voice
    if voice_status is None:
        return

    content = message.content

    if not content.lower().startswith(PLAY_CMD):
        return

    track = content.split(PLAY_CMD + " ")[1].lower()
    track_file = _match_track(track)

    if track_file is not None:
        with suppress(Exception):
            vc = await message.author.voice.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source=os.path.join(AUDIO_FILES_DIR, track_file)))

            while vc.is_playing():
                await sleep(1)

            await vc.disconnect()


async def handle_list(message: discord.Message) -> None:
    await message.channel.send("\n".join(_get_files()))
