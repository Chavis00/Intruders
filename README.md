# Introduction
See who is near your cam!  

Using OpenCV this application can detect specific objects and faces in real time from you webcam or ipcam, if a face is detected, it is produced to save it and send it to Microsoft Azure Face API analyze facial expressions and estimate the age, and finally send all this information using a Telegram Bot. 

## Instalation
Clone this repository
```bash
git clone https://github.com/Chavis00/intruders.git
```
Install requirements
```bash
pip install -r requirements.txt 
```

### CV2 Instalation
Installing CV2 for your OS:
- [CV2 for Ubuntu Tutorial](https://docs.opencv.org/3.4/d2/de6/tutorial_py_setup_in_ubuntu.html)
- [CV2 for Windows Tutorial](https://docs.opencv.org/4.x/d5/de5/tutorial_py_setup_in_windows.html)

- [CV2 for MacOs Tutorial](https://docs.opencv.org/4.x/d0/db2/tutorial_macos_install.html)

## Get Keys
- [Microsoft Azure Face API](https://azure.microsoft.com/es-es/services/cognitive-services/face/)
- [Imgur API](https://api.imgur.com/oauth2/addclient) 
- Telegram API: Send a Telegram message to @BotFather and type /newbot
## Config Keys in config.py
```python
#Microsoft Azure Face API Key & Endpoint
FKEY = KEYS["AZURE_API_KEY"]
ENDPOINT = KEYS["AZURE_ENDPOINT"]

#Telegram bot API Token & Chat ID
TOKEN = KEYS["TELEGRAM_TOKEN"]
CHAT_ID= KEYS["TELEGRAM_CHATID"]

#Imgur Client ID
CLIENT_ID = KEYS["IMGUR_CLIENT"]

```
## Enjoy!
```bash
python3 set_up.py
```
