from telegram import Bot
from config import TOKEN, CHAT_ID

def send_intruder(date, stats, pic_url, chat_id=CHAT_ID,token=TOKEN):
	bot = Bot(token=token)
	if stats:
		bot.sendPhoto(chat_id=chat_id, photo=pic_url)
		bot.sendMessage(chat_id=chat_id, text=date)
		bot.sendMessage(chat_id=chat_id, text=stats)
		print("Intruder sent")