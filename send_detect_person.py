import discord
import os
import settings
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import asyncio
import time

# watchdogというファイルの更新だとかを監視してくれるライブラリを使う
class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, loop,bot):
        self.loop = loop
        self.FILE = settings.FILE
        self.bot = bot

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(self.FILE):
            print("人間を検知!!!")
            # discordの送信送り
            asyncio.run_coroutine_threadsafe(self.bot.send_message(), self.loop)

class Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = discord.app_commands.CommandTree(self)
        self.TOKEN = settings.TOKEN
        self.FILE = settings.FILE
        self.CHANNEL_ID = settings.CHANNEL_ID

    async def send_message(self):
        channel = self.get_channel(self.CHANNEL_ID)
        with open(self.FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            output_log = lines[len(lines) - 1]
        output_log = output_log.rstrip("\n")
        print(output_log)
        if channel:
            await channel.send(f"{output_log}")

    # 起動確認用
    async def on_ready(self):
        print(f"{self.user}の起動を確認")
        print(self.get_channel(self.CHANNEL_ID))
        # watchdog の監視開始
        event_handler = FileChangeHandler(self.loop,self)
        observer = Observer()
        observer.schedule(event_handler, path=os.path.dirname(self.FILE) or ".", recursive=False)
        observer.start()

    def run_bot(self):
        self.run(self.TOKEN)


if __name__ == "__main__":
    bot = Bot()
    bot.run_bot()
