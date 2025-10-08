import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")
FILE = os.environ.get("FILE")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
REALPERSON = float(os.environ.get("REALPERSON"))
STANDBYTIME = int(os.environ.get("STANDBYTIME"))