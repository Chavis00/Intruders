from src.FaceRecognition import FaceRecognition
from src.garbage_collector import GarbageCollector
from src.imgur_uploader import ImgurHelper
from src.telegram_bot import TelegramBot
from src.webcam import Webcam
from config import CASCPATH, OUTPUTPATH, CAMERA, SIZE_PX, TOKEN, ENDPOINT, FKEY, INSTALLED_APPS, USERS_IDS, CLIENT_ID


def init_applications(web_cam: Webcam) -> None:
    if "TELEGRAM_BOT" or "AZURE_FACE_DETECTION" or "IMGUR" in INSTALLED_APPS:
        telegram_bot = TelegramBot(users_ids=USERS_IDS, token=TOKEN, priority=0)
        web_cam.add_observer(telegram_bot)
    if "AZURE_FACE_DETECTION" in INSTALLED_APPS:
        azure_face_detection = FaceRecognition(endpoint=ENDPOINT, fkey=FKEY, priority=1, telegram_bot=telegram_bot)
        web_cam.add_observer(azure_face_detection)
    if "GARBAGE_COLLECTOR" in INSTALLED_APPS:
        garbage_collector = GarbageCollector(priority=2)
        web_cam.add_observer(garbage_collector)
    if "IMGUR" in INSTALLED_APPS:
        imgur_helper = ImgurHelper(client_id=CLIENT_ID, telegram_bot=telegram_bot, priority=1)
        web_cam.add_observer(imgur_helper)


if __name__ == '__main__':
    web_cam = Webcam(CASCPATH, OUTPUTPATH, CAMERA, SIZE_PX)
    init_applications(web_cam)
    web_cam.capture()
