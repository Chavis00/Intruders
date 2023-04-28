import datetime

import telegram

from src.observer import Observer
from src import logging_config


class TelegramBot(Observer):
    def __init__(self, users_ids: list, token: str, priority: int):
        super().__init__(priority)
        self.users_ids = users_ids
        self.telegram_bot = telegram.Bot(token=token)

    async def update(self, file_path: str, current_time=datetime.datetime):
        logging_config.logging.info("Sending Image via Telegram " + file_path)
        now = current_time.strftime("%H:%M:%S \n%d-%m-%Y")
        new_intruder_msg = "----- New intruder detected near your cam! -----"
        await self.send_msg(new_intruder_msg)
        await self.send_picture(file_path=file_path)
        await self.send_msg(now)

    async def send_picture(self, file_path: str):
        for user_id in self.users_ids:
            await self.telegram_bot.sendPhoto(chat_id=user_id, photo=open(file_path, 'rb'))

    async def send_msg(self, msg):
        for user_id in self.users_ids:
            await self.telegram_bot.sendMessage(chat_id=user_id, text=msg, disable_web_page_preview=True)
