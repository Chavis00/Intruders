import datetime

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from src import logging_config
from src.observer import Observer

from src.telegram_bot import TelegramBot


class FaceRecognition(Observer):

    def __init__(self, endpoint: str, fkey: str, priority: int, telegram_bot: TelegramBot):
        super().__init__(priority)
        self.client = FaceClient(endpoint, CognitiveServicesCredentials(fkey))
        self.detection_model = 'detection_01'
        self.recognition_model = 'recognition_04'
        self.return_face_attributes = ['age', 'emotion']
        self.stats_unformated = "Estimated Age:  + {age} + \nNeutral:  + {neutral} + \nHappiness:  + {happiness} + \nSurprise:  + {surprise} + \nAnger:  + {anger}"
        self.stats = {}
        self.telegram_bot = telegram_bot

    async def update(self, file_path: str, current_time=datetime.datetime) -> None:
        self.scan_face(file_path=file_path)
        if self.telegram_bot is not None:
            await self.telegram_bot.send_msg(msg=self.stats[file_path])

    def scan_face(self, file_path: str):
        response = self.request_face_information(file_path=file_path)
        logging_config.logging.info('Processing image: %s', file_path)
        if not response:
            logging_config.logging.error('The image could not be processed + %s', file_path)
            self.stats[file_path] = "The image could not be processed"
            return

        for face in response:
            age = face.face_attributes.age
            emotions = face.face_attributes.emotion
            neutral = '{0:.0f}%'.format(emotions.neutral * 100)
            happiness = '{0:.0f}%'.format(emotions.happiness * 100)
            surprise = '{0:.0f}%'.format(emotions.surprise * 100)
            anger = '{0:.0f}%'.format(emotions.anger * 100)

        face_stats = self.stats_unformated.format(age=age, neutral=neutral, happiness=happiness,
                                                  surprise=surprise, anger=anger)
        self.stats[file_path] = face_stats

    def request_face_information(self, file_path):
        image_file = open(file_path, 'rb')
        response_detection = self.client.face.detect_with_stream(
            image_file,
            detection_model=self.detection_model,
            recognition_model=self.recognition_model,
            return_face_attributes=self.return_face_attributes,
        )
        type(response_detection)
        return response_detection
