import datetime

import telegram

from src.observer import Observer
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)


class TelegramBot(Observer):
    def __init__(self, chat_id: int, token: str, priority: int):
        super().__init__(priority)
        self.chat_id = chat_id
        self.telegram_bot = telegram.Bot(token=token)

    async def update(self, file_path: str, *args):
        logging.info("Sending Image via Telegram " + file_path)
        await self.send_intruder_picture(date=datetime.datetime.now(), file_path=file_path)

    async def send_intruder_picture(self, date, file_path: str):
        await self.telegram_bot.sendPhoto(chat_id=self.chat_id, photo=open(file_path, 'rb'))
        await self.telegram_bot.sendMessage(chat_id=self.chat_id, text=date)

    async def send_intruder_stats(self, stats):
        await self.telegram_bot.sendMessage(chat_id=self.chat_id, text=stats)
