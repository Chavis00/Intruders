from scripts.webcam import Webcam
from scripts.API_control import api_controller
from multiprocessing import Process
import sys

from multiprocessing import Process
wb = Webcam()

def func1():
    print ('func1: starting')
    wb.capture()
    print ('func1: finishing')

def func2():
    print ('func2: starting')
    api_controller()
    print ('func2: finishing')

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p1.join()
  p2.join()
