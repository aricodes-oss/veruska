import discord


class Client(discord.Client):
    async def on_ready(self) -> None:
        print("Ret-2-Go!")


client: Client = Client()
