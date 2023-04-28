import asyncio
import datetime
import logging as log
import os
import time

import cv2
import imutils
from PIL import Image
from imutils.video import VideoStream, FPS

from src import logging_config
from src.observer import Subject


class Webcam(Subject):
    def __init__(self, CASCPATH, OUTPUTPATH, CAMERA, SIZE_PX):
        super().__init__()
        self.camera = CAMERA
        self.cascPath = CASCPATH
        self.output_path = OUTPUTPATH
        self.size = SIZE_PX
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        self.anterior = 0

    async def save_face(self, faces, capture) -> None:
        current_time = datetime.datetime.now()  # grab the current time
        filename = "{}.jpg".format(current_time.strftime("%d-%m-%Y_%H-%M-%S"))  # construct filename
        p = os.path.join(self.output_path, filename)  # construct output path

        """Save a Snapshot"""
        current_image = Image.fromarray(capture)  # Take the snapshot
        current_image.save(p, "jpeg")  # Save image as jpeg file
        log.info("[INFO] Saved {}".format(filename))

        """Change anterior and save the log info """
        self.anterior = len(faces)  # Set Anterior

        logging_config.logging.info("faces: " + str(len(faces)) + " at " + str(datetime.datetime.now()).replace(":", "-"))  # Save Log info
        await self.notify_observers(file_path=p)

    def capture(self) -> None:
        logging_config.logging.info("Starting video stream...")
        vs = VideoStream(self.camera).start()
        time.sleep(1.0)
        """ Loop over the frames from the video stream"""
        while True:

            frame = vs.read()
            frame = imutils.resize(frame, width=self.size)
            capture = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            """Face detection"""
            faces = self.faceCascade.detectMultiScale(
                capture,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            """If capture new face"""
            if self.anterior != len(faces):
                loop = asyncio.get_event_loop()
                loop.run_until_complete(self.save_face(faces, capture))
