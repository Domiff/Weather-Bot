import os

from dotenv import load_dotenv

load_dotenv()

config: dict = {
    "bot_token": os.getenv("BOT_TOKEN"),
    "api_key": os.getenv("API_KEY"),
    "base_url": os.getenv("BASE_URL"),
}
