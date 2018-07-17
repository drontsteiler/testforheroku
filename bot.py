import config
import telebot

bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, "You write to me: "+message.text)
    print ("Message text: "+ message.text)
if __name__ == '__main__':
    bot.polling(none_stop=True)
