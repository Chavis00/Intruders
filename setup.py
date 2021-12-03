from scripts.webcam import Webcam
from scripts.API_control import api_controller
from multiprocessing import Process
import sys
from config import CASCPATH, LOGPATH, OUTPUTPATH, OBJECTS, CAMERA, MODEL_PATH, PROTOTXT_PATH, SIZE_PX


from multiprocessing import Process
wb = Webcam(CASCPATH, LOGPATH, OUTPUTPATH, OBJECTS, CAMERA, SIZE_PX, MODEL_PATH, PROTOTXT_PATH)

def camera():
    print ('Camera: starting')
    wb.capture()

def api():
    print ('API Controller: starting')
    api_controller()

if __name__ == '__main__':
  p1 = Process(target=camera)
  p1.start()
  p2 = Process(target=api)
  p2.start()
  p1.join()
  p2.join()
