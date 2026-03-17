import discord
import os
import settings
import logging
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FileChangeHandler(FileSystemEventHandler):
    """
    Handles file system events, specifically looking for modifications to a specific file.
    """
    def __init__(self, loop: asyncio.AbstractEventLoop, bot: 'Bot'):
        """
        Initialize the FileChangeHandler.

        Args:
            loop (asyncio.AbstractEventLoop): The asyncio event loop.
            bot (Bot): The Discord bot instance.
        """
        self.loop = loop
        self.FILE = settings.FILE
        self.bot = bot

    def on_modified(self, event: FileSystemEvent):
        """
        Called when a file or directory is modified.

        Args:
            event (FileSystemEvent): The event object representing the file system event.
        """
        if not event.is_directory and event.src_path.endswith(self.FILE):
            logger.info("File updated: %s", event.src_path)
            # Send message to Discord
            asyncio.run_coroutine_threadsafe(self.bot.send_message(), self.loop)

class Bot(discord.Client):
    """
    Custom Discord Client to handle file monitoring and messaging.
    """
    def __init__(self):
        """
        Initialize the Bot.
        """
        super().__init__(intents=discord.Intents.default())
        self.tree = discord.app_commands.CommandTree(self)
        self.TOKEN = settings.TOKEN
        self.FILE = settings.FILE
        self.CHANNEL_ID = settings.CHANNEL_ID
        self.observer = Observer()

    async def send_message(self):
        """
        Sends a message to the configured Discord channel indicating the file has been updated.
        """
        channel = self.get_channel(self.CHANNEL_ID)
        if channel:
            await channel.send(f"`{self.FILE}` が更新されました")
        else:
            logger.error("Channel with ID %s not found.", self.CHANNEL_ID)

    async def on_ready(self):
        """
        Called when the bot is ready.
        """
        logger.info("%s has started.", self.user)
        channel = self.get_channel(self.CHANNEL_ID)
        if channel:
            logger.info("Target channel found: %s", channel)
        else:
            logger.warning("Target channel with ID %s NOT found.", self.CHANNEL_ID)
        
        self.start_monitoring()

    def start_monitoring(self):
        """
        Starts the watchdog observer to monitor file changes.
        """
        logger.info("Starting watchdog observer...")
        event_handler = FileChangeHandler(self.loop, self)
        watch_dir = os.path.dirname(self.FILE) or "."
        self.observer.schedule(event_handler, path=watch_dir, recursive=False)
        self.observer.start()
        logger.info("Watchdog observer started monitoring: %s", watch_dir)

    def run_bot(self):
        """
        Runs the bot using the configured token.
        """
        if not self.TOKEN:
            logger.error("No token found in settings.")
            return
        self.run(self.TOKEN)

def main():
    """
    Main entry point for the script.
    """
    bot = Bot()
    bot.run_bot()

if __name__ == "__main__":
    main()
