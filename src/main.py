import logging

from aiogram.types import BufferedInputFile
from fastapi import FastAPI, Request
from aiogram import Bot
from starlette.responses import JSONResponse

from src.config import (TELEGRAM_API_TOKEN, TELEGRAM_CHAT_ID,
                        TELEGRAM_ADMIN_ID, WISE_API_TOKEN)
from src.infrastructure.api.wise.api import WiseAPI

app = FastAPI()
log_level = logging.INFO
log = logging.getLogger(__name__)

bot = Bot(token=TELEGRAM_API_TOKEN, parse_mode="HTML")


@app.post("/webhook")
async def webhook_endpoint(request: Request):
    wise = WiseAPI(api_token=WISE_API_TOKEN)

    json_data = None
    user_data = None

    try:
        user_data = await wise.get_current_user()
        json_data = await request.json()

        currency = json_data['data']['currency']
        time = json_data['data']['occurred_at'].replace("T", " ").replace("Z", "")

        text = (
            f"<b>👤 {user_data['name']}</b>\n\n"
            f"<b>💸 +{json_data['data']['amount']} {currency}</b>\n"
            f"<b>💰 {json_data['data']['post_transaction_balance_amount']} "
            f"{currency}</b>\n\n"
            f"<b>⏳ {time}</b>\n"
        )

        await bot.send_message(TELEGRAM_CHAT_ID, text)
    except Exception as _ex:
        message_text = (
            f"<b>⚠️ Error:</b> <code>{_ex}</code>"
        )

        file_text = (
            f"{json_data=}\n"
            f"{user_data=}\n"
        ).encode()
        file = BufferedInputFile(
            file=file_text,
            filename=f"error.txt"
        )

        await bot.send_document(
            chat_id=TELEGRAM_ADMIN_ID,
            caption=message_text,
            document=file
        )
    finally:
        await wise.close()
        return JSONResponse(status_code=200, content={"status": "ok"})
