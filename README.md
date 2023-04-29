# Intruders Face Detection
The purpose of this application is to enhance camera security by detecting the faces of potential intruders nearby and alerting the user by sending a photo of the intruder.
## Application Overview
The main application utilizes OpenCV to detect faces near an IP camera or webcam. Additionally, it integrates four separate modules:
- Microsoft Azure's facial recognition API to detect facial attributes and state. 
- Telegram's API to send photos of recognized faces.
- Imgur's API to upload images and obtain a URL.
- A "Garbage Collector" to remove old images from the system.

It is not necessary to use or have all four applications configured. To choose which applications the bot will use, you need to change the following in config.py:
```python
INSTALLED_APPS = [
    'TELEGRAM_BOT',
    'AZURE_FACE_DETECTION',
    'GARBAGE_COLLECTOR',
    'IMGUR'
]
```
## Application Configuration

### Camera
To configure the camera, you need to set the camera URL in enviroment variables:
```dosini
CAMERA=yourcameraurl
```
If you want to use a webcam, you can use the following URL:
```dosini
CAMERA=0
```
Or any other number if you have multiple webcams

### Telegram Bot
Send a Telegram message to @BotFather and type /newbot, then configure your token in enviroment variables
```dosini
BOT_TOKEN=yourownbottoken
```
To set users to notify about intruders, you need to add their Telegram Chat ID to the following list in config.py:
```python 
USERS_IDS = [
    1234567890,
    1234567890,
    1234567890
]
```
### Microsoft Azure Face API
To configure the Microsoft Azure Face API, you need to create a resource in [Azure-Cognitive-Services](https://azure.microsoft.com/en-us/services/cognitive-services/face/) and obtain the API Key and Endpoint. Then, you need to set them in enviroment variables:
```dosini
AZURE_FKEY=yourapikey
AZURE_ENDPOINT=yourendpoint
```
These are the features and pricing for available features available in the Face API:

| Tiers / Features                       | F0 Free (20 Calls per minute, 30K Calls per month) | S0 Standard (10 Calls per second) | 
|----------------------------------------|----------------------------------------------------|-----------------------------------|
| Read Pricing                           | --                                                 | $0.40 USD/1000 calls (Estimated)  |
| Face Detection                         | ✓                                                  | ✓                                 | 
| Face Verification                      | ✓                                                  | ✓                                 |
| Face Identification                    | ✓                                                  | ✓                                 |
| Face Grouping                          | ✓                                                  | ✓                                 |
| Similar Face Searching                 | ✓                                                  | ✓                                 |
| Persisted Faces Per Month - 0.01USD/1K | --                                                 | ✓                                 |

Recommended to use F0 Free tier for testing purposes and S0 Standard tier for production purposes.


### Imgur API
To configure the Imgur API, you need to create an account in Imgur and create a new application [here](https://api.imgur.com/oauth2/addclient) and obtain the Client ID. Then, you need to set the client in enviroment variables:
```dosini
IMGUR_CLIENT=yourclientid
```
### Garbage Collector
No need to configure anything here.

# How to use
## Run with Docker
### Build Docker Image
```
docker build -t 'intruders-security' .
```
Execute the following command to run the script, making sure to correctly add the environment variables if necessary:
```
 docker run --name intruders-security \
  -e CAMERA=yourbottoken \
  -e AZURE_FKEY=yourworkingsheet \
  -e AZURE_ENDPOINT=yoursheetname \
  -e TELEGRAM_TOKEN=recipeapiurl \
  -e IMGUR_CLIENT_ID=recipeid
  intruders-security
```

## Run with docker-compose (Recommended)
Configure your .env file and then run
```
docker-compose up --build
```
# Implementation of the Observer design pattern
The Observer design pattern is implemented in the following classes:
- Camera
- TelegramBot
- FaceRecognition
- GarbageCollector
- Imgur

Where the Camera class is the Subject and the rest are Observers. The Camera class notifies the Observers when a face is detected and sends the image to the Observers.
So if you want to add a new Application (Observer), you just need to create a new class and implement the Observer interface.
And suscribe the new Observer to the Camera class in the main.py file

## UML Diagram
![](https://github.com/Chavis00/intruders-face-detection/blob/main/imgs/obeserver_pattern.png)

# Screenshots
![](https://github.com/Chavis00/intruders-face-detection/blob/main/imgs/example1.png)
![](https://github.com/Chavis00/intruders-face-detection/blob/main/imgs/example2.png)
