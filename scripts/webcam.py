from imutils.video import VideoStream, FPS
import numpy as np
import imutils
import time
import cv2
import os
import logging as log
import datetime
from PIL import Image


class Webcam:
    def __init__(self, CASCPATH, LOGPATH, OUTPUTPATH, OBJECTS, CAMERA, SIZE_PX, MODEL_PATH, PROTOTXT_PATH):

        self.model_path = MODEL_PATH
        self.prototxt_path = PROTOTXT_PATH
        self.camera = CAMERA
        self.cascPath = CASCPATH
        self.output_path = OUTPUTPATH
        self.classes = OBJECTS
        self.size = SIZE_PX

        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        log.basicConfig(filename=LOGPATH,level=log.INFO)
        self.video_capture = cv2.VideoCapture(CAMERA, cv2.CAP_DSHOW)
        self.anterior = 0

    def save_face(self, faces, capture):
        """"Constructing Path"""                
        current_time = datetime.datetime.now()  # grab the current time
        filename = "{}.jpg".format(current_time.strftime("%d-%m-%Y_%H:%M:%S"))  # construct filename
        p = os.path.join(self.output_path, filename)  # construct output path

        """Save a Snapshot"""
        current_image = Image.fromarray(capture)  # Take the snapshot
        current_image.save(p, "jpeg")  # Save image as jpeg file
        print("[INFO] Saved {}".format(filename)) # Print info

        """Change anterior and save the log info """
        self.anterior = len(faces) # Set Anterior
        
        log.info("faces: "+str(len(faces))+" at "+str(datetime.datetime.now()))  # Save Log info
    
    def extract_idx(self, detections, i, h, w):
        """Extract the index of the class label from the detections, then compute the (x, y)-coordinates of the bounding box for the object"""
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        return idx, startX, startY, endX, endY
    
    def draw_box_on_prediction(self, confidence, frame, COLORS, idx, startX, startY, endX, endY):
        """Draw the prediction on the frame"""
        label = "{}: {:.2f}%".format(self.classes[idx], confidence * 100)
        cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    def capture(self):

        """Load our serialized model from disk"""
        print("[INFO] loading model...")
        net = cv2.dnn.readNetFromCaffe(self.prototxt_path, self.model_path)

        COLORS = np.random.uniform(0, 255, size=(len(self.classes), 3))

        """Initialize the video stream, allow the cammera sensor to warmup, and initialize the FPS counter"""
        print("[INFO] starting video stream...")
        vs = VideoStream(self.camera).start()
        time.sleep(2.0)
        fps = FPS().start()
        
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

            """Draw a rectangle around the faces"""
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            """If capture new face"""
            if self.anterior != len(faces):
                self.save_face(faces, capture)
                

            """Grab the frame dimensions and convert it to a blob"""
            (h, w) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

            """Pass the blob through the network and obtain the detections and predictions"""
            net.setInput(blob)
            detections = net.forward()

            """Loop over the detections"""
            for i in np.arange(0, detections.shape[2]):
    
            	"""Extract the confidence (i.e., probability) associated with the prediction"""
            	confidence = detections[0, 0, i, 2]

            	"""Filter out weak detections by ensuring the confidence is greater than the minimum confidence"""
            	if confidence > 0.2:
                    
                    idx, startX, startY, endX, endY = self.extract_idx(detections, i, h, w)
                    self.draw_box_on_prediction(confidence, frame, COLORS, idx, startX, startY, endX, endY) 		

            """Show the output frame"""            
            cv2.imshow("Frame", frame)

            """Update the FPS counter"""
            fps.update()

            """If the 'q' key was pressed, break from the loop and end Camera"""
            if cv2.waitKey(1) & 0xFF == ord('q'):

                print("Turning off camera.")
                self.video_capture.release()

                print("Camera off.")
                print("Program ended.")
                fps.stop()

                print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
                print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

                cv2.destroyAllWindows()
                vs.stop()

                break
            
    