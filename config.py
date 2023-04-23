"""CAMERA"""
import os

CAMERA = os.environ.get("CAMERA")  # 0  # 0 for default,for IP camera just set "IP:PORT/video"
SIZE_PX = 500  # Size in pixel

""" API KEYS """
# Microsoft Azure Face API Key & Endpoint
FKEY = os.environ.get("AZURE_FKEY")
ENDPOINT = os.environ.get("AZURE_ENDPOINT")

# Telegram bot API Token & Chat ID
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# Imgur Client ID
CLIENT_ID = os.environ.get("IMGUR_CLIENT_ID")

# Image Saving Path
OUTPUTPATH = os.path.join(os.getcwd(), 'shots')
LOG_PATH = os.path.join(os.getcwd(), 'log')
# FACE MODEL
CASCPATH = os.path.join(os.getcwd(), 'models/face_model/haarcascade_frontalface_default.xml')
