import json

"""Getting Keys"""
def get_keys(path):
    with open(path) as f:
        return json.load(f)

KEYS = get_keys("KEYS.json")


"""CAMERA"""
CAMERA = 0 #0 for default,for IP camera just set "IP:PORT/video"
SIZE_PX = 400 #Size in pixel

"""API KEYS (LET EMPTY STRING TO DESACTIVATE)"""

#Microsoft Azure Face API Key & Endpoint
FKEY = KEYS["AZURE_API_KEY"]
ENDPOINT = KEYS["AZURE_ENDPOINT"]

#Telegram bot API Token & Chat ID
TOKEN = KEYS["TELEGRAM_TOKEN"]
CHAT_ID = KEYS["TELEGRAM_CHATID"]

#Imgur Client ID
CLIENT_ID = KEYS["IMGUR_CLIENT"]


"""PATHS"""
LOGPATH = './log/webcam.log' #Log Path
OUTPUTPATH = './shots' # Snapshots Path 


"""OBJECTS"""
OBJECTS = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

"""MODELS"""
#Objects
MODEL_PATH = 'models/objects_model/MobileNetSSD_deploy.caffemodel'
PROTOTXT_PATH = 'models/objects_model/MobileNetSSD_deploy.prototxt.txt'

#Face
CASCPATH = 'models/face_model/haarcascade_frontalface_default.xml'


