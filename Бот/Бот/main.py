import telebot
import extentions

bot = telebot.TeleBot(extentions.token)


@bot.message_handler(commands=['start', 'help'])
def description(message):
    text = 'Введите через пробел <b>имя первой валюты</b>___<b>имя второй валюты</b>___<b>количество первой валюты</b>'
    bot.send_message(message.chat.id, text, parse_mode='html')
    return


@bot.message_handler(commands=['values'])
def get_values(message):
    text: str = 'Ты можешь конвертировать такие валюты как: '

    for currency in extentions.currencies:
        text += str(currency) + ' '

    bot.send_message(message.chat.id, text, parse_mode='html')
    return


@bot.message_handler()
def get_user_text(message):
    input = message.text.split(' ')

    if len(input) < 3 or len(input) > 3:
        text: str = 'Параметров должно быть <b>3</b>! Сейчас их ' + str(len(input)) + '!'
        bot.send_message(message.chat.id, text, parse_mode='html')
        return

    base = str(input[0]).upper()
    quote = str(input[1]).upper()

    try:
        amount = float(input[2])
    except:
        text: str = 'Неверно введено число. Число должно быть целое, либо если десятичное - разделяться точкой'
        bot.send_message(message.chat.id, text, parse_mode='html')
        return

    if base not in extentions.currencies or quote not in extentions.currencies:

        text = ''

        if base not in extentions.currencies:
            text += str(base) + ' - неверная валюта \n'
        if quote not in extentions.currencies:
            text += str(quote) + ' - неверная валюта'

        bot.send_message(message.chat.id, text, parse_mode='html')

        return

    count = extentions.Requests.get_price(base, quote, amount)
    text = str(amount) + ' ' + base + ' = ' + str(count) + ' ' + quote
    bot.send_message(message.chat.id, text, parse_mode='html')
    return


bot.polling(none_stop=True)
