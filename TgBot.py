import telebot
import pytube
from bs4 import BeautifulSoup
import requests
from Config_file import TOKEN

bot = telebot.TeleBot(token = TOKEN)

@bot.message_handler(commands = ["video"])
def send_video(message):
	url = message.text.split(" ")[1]
	resource = requests.get(url)
	soup = BeautifulSoup(resource.text,"html.parser")
	title = soup.title.string
	youtube = pytube.YouTube(url)
	streams = youtube.streams.filter(progressive = True,file_extension = "mp4").first()

	streams.download()
	
	with open(streams.default_filename,"rb")as video:
		bot.send_video(chat_id = message.chat.id,video = video,caption = title)
	#bot.send_message(chat_id = message.from_user.id,text = title)


	
	
if __name__ == '__main__':
	print("< < <RUN BOT> > >")
	bot.polling(non_stop = True)
	print("< < <STOP BOT> > >")
