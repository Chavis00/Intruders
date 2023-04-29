"""CAMERA"""
import os

INSTALLED_APPS = [
    'TELEGRAM_BOT',
    'AZURE_FACE_DETECTION',
    'GARBAGE_COLLECTOR',
    'IMGUR'
]

# Camera config
CAMERA = os.environ.get("CAMERA")  # 0  # 0 for default,for IP camera just set "IP:PORT/video"
SIZE_PX = 500  # Size in pixel

# Telegram bot config
TOKEN = os.environ.get("TELEGRAM_TOKEN")
USERS_IDS = [
    1499495357
]
# Microsoft Azure Face API config
FKEY = os.environ.get("AZURE_FKEY")
ENDPOINT = os.environ.get("AZURE_ENDPOINT")


# Imgur Client ID
CLIENT_ID = os.environ.get("IMGUR_CLIENT_ID")

# Image Saving Path
OUTPUTPATH = os.path.join(os.getcwd(), 'shots')
if not os.path.exists(OUTPUTPATH):
    os.makedirs(OUTPUTPATH)
LOG_PATH = os.path.join(os.getcwd(), 'log')
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
# FACE MODEL
CASCPATH = os.path.join(os.getcwd(), 'models/face_model/haarcascade_frontalface_default.xml')
