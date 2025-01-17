from telethon import TelegramClient
from telethon.sessions import StringSession
import os

api_id = int(os.environ["api_id"])
api_hash = os.environ["api_hash"]
string = os.environ["string"]
bot_token = os.environ["bot_token"]

crowgram = TelegramClient(StringSession(string), api_id, api_hash)
crowgram_bot = TelegramClient("crowgram", api_id, api_hash).start(bot_token=bot_token)