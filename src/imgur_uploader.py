import datetime

from pyimgur import Imgur
from src import logging_config
from src.observer import Observer
from src.telegram_bot import TelegramBot


class ImgurHelper(Observer):
    def __init__(self, client_id: str, telegram_bot: TelegramBot, priority: int):
        super().__init__(priority)
        self.client = Imgur(client_id)
        self.telegram_bot = telegram_bot

    async def update(self, file_path: str, current_time=datetime.datetime):
        now = current_time.strftime("%H:%M:%S -- %d-%m-%Y")
        img_url = self.upload(path=file_path, description=now)
        msg = "Image URL: "+img_url
        if self.telegram_bot is not None:
            await self.telegram_bot.send_msg(msg=msg)
        logging_config.logging.info("Image uploaded to Imgur! " + img_url)

    def upload(self, path: str, description: str) -> str:
        uploaded_img = self.client.upload_image(path, title="Intruder", description=description)
        return str(uploaded_img.link)