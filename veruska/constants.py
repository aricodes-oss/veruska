from .env import env

DISCORD_BOT_TOKEN = env("DISCORD_BOT_TOKEN")
BOT_TESTING_CHANNEL = env.int("BOT_TESTING_CHANNEL")
AUDIO_FILES_DIR = env("AUDIO_FILES_DIR", default="/tracks")
PLAY_CMD = env("PLAY_CMD", default="!play")
LIST_CMD = env("LIST_CMD", default="!list")
