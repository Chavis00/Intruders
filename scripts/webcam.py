import os
import cv2
import logging as log
import datetime
from time import sleep
from PIL import Image

from scripts.faceAPI import detect
from scripts.imgur_uploader import upload
from scripts.telegram_bot import send_intruder

class Webcam:

    def __init__(self):

        self.cascPath = "scripts/xml/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        log.basicConfig(filename='log/webcam.log',level=log.INFO)

        self.video_capture = cv2.VideoCapture(0)
        self.anterior = 0

    def capture(self):

        while True:

            if not self.video_capture.isOpened():
                print('Unable to load camera.')
                sleep(5)
                pass

            # Capture frame-by-frame
            ret, frame = self.video_capture.read()

            capture = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            self.faces = self.faceCascade.detectMultiScale(
                capture,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in self.faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)






            if self.anterior != len(self.faces):

                """ Take snapshot and save it to the file """

                ts = datetime.datetime.now()  # grab the current timestamp
                filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))  # construct filename
                output_path='./shots'

                p = os.path.join(output_path, filename)  # construct output path
                current_image = Image.fromarray(capture) 
                current_image.save(p, "jpeg")  # save image as jpeg file


                print("[INFO] Guardado {}".format(filename))
                print(len(self.faces))
                date = filename.replace(".jpg", "")

                stats = detect('./shots/'+filename)
                print(stats)
                if stats:
                    link = upload('./shots/'+filename)
                    print(link)
                    send_intruder(date, stats ,link)



                """ change anterior and save the log info """
                self.anterior = len(self.faces)
                log.info("faces: "+str(len(self.faces))+" at "+str(datetime.datetime.now()))


            # Display the resulting frame
            #cv2.imshow('Video', frame)



            if cv2.waitKey(1) & 0xFF == ord('x'):
                print("Turning off camera.")
                self.video_capture.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break

            # Display the resulting frame
            cv2.imshow('Video', frame)

        # When everything is done, release the capture
        self.video_capture.release()
        cv2.destroyAllWindows()


