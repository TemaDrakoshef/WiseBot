from dotenv import load_dotenv
import os

load_dotenv()

WISE_API_TOKEN = os.environ.get("WISE_API_TOKEN")
TELEGRAM_API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")
TELEGRAM_ADMIN_ID = os.environ.get("TELEGRAM_ADMIN_ID")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
