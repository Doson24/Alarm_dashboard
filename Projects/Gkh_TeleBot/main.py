import telebot
import time

def print_hi():

    token = "5224696385:AAG23ZsTeQaW8dkhAUkT8w7a-0ybzKNcwJE"
    bot = telebot.TeleBot(token)
    # Адрес телеграм-канала, начинается с @
    CHANNEL_NAME = '@test321231'
    bot.send_message(CHANNEL_NAME, 'пупсик приветasd')

    # @bot.message_handler(commands=["start"])
    # def start(m, res=False):
    #     bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    # # Получение сообщений от юзера
    # @bot.message_handler(content_types=["text"])
    # def handle_text(message):
    #     bot.send_message(CHANNEL_NAME, 'Вы написали: ' + message.text)
    # # Запускаем бота
    # bot.polling(none_stop=True, interval=0)
    'https://oauth.vk.com/blank.html#access_token=32e038fff62c7c5e5c4f554488d3e2405b6463c47fea449b4a641c120eb908e792222af4323589b80dfb1&expires_in=0&user_id=370210336'



if __name__ == '__main__':
    print_hi()
