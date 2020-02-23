import telebot


token = ''


bot = telebot.TeleBot(token)

def new_order(massege):
    #YEgor's
    bot.send_message('telegram user id; must be int', massege)
    #Dasha's
    bot.send_message('telegram user id; must be int', massege)
