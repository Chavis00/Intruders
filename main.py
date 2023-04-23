from src.FaceRecognition import FaceRecognition
from src.garbage_collector import GarbageCollector
from src.telegram_bot import TelegramBot
from src.webcam import Webcam
from config import CASCPATH, OUTPUTPATH, CAMERA, SIZE_PX, TOKEN, CHAT_ID, ENDPOINT, FKEY


if __name__ == '__main__':
    web_cam = Webcam(CASCPATH, OUTPUTPATH, CAMERA, SIZE_PX)
    telegram_bot = TelegramBot(chat_id=CHAT_ID, token=TOKEN, priority=1)
    azure_face_detection = FaceRecognition(endpoint=ENDPOINT, fkey=FKEY, priority=0, telegram_bot=telegram_bot)
    garbage_collector = GarbageCollector(priority=2)

    web_cam.add_observer(azure_face_detection)
    web_cam.add_observer(telegram_bot)
    web_cam.add_observer(garbage_collector)

    web_cam.capture()
