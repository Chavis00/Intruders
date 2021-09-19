# Intruders
See who is trying to use your pc in real time!  

Using the cv2 library this application can detect faces near your PC, through Microsoft Azure Face API analyze facial expressions and estimate the age of the intruder, and finally send all this information using a Telegram Bot.

## Instalation
Clone this repository
```bash
git clone https://github.com/Chavis00/intruders.git
```
Install requirements
```bash
pip install -r requirements.txt 
```

## Get Keys
- [Microsoft Azure Face API](https://azure.microsoft.com/es-es/services/cognitive-services/face/)
- [Imgur API](https://api.imgur.com/oauth2/addclient) 
- Telegram API: Talk to @BotFather and type /newbot



## Config Keys
```python
#Microsoft Azure Face API Key & Endpoint
FKEY = '' 
ENDPOINT = ''

#Telegram bot API Token & Chat ID
TOKEN = ''
CHAT_ID= #must be an int

#Imgur Client ID
CLIENT_ID = ''
```
## Enjoy!
```bash
python3 set_up.py
```
