import logging
import re

import requests
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.NOTSET)


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Woof, woof hey homan do you want some doggo photos?")
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo='https://sun9-7.userapi.com/impf/VgXC4w60HqcsyAm2YavT1VXMqqQKq01Tpn482g/PP3jW_xIn0Y.jpg?size=500x467&quality=96&proxy=1&sign=1460904564a304dc3137c3f51051ad98&type=album')


def bop(update, context):
    url = get_url()
    if re.search('([^.]*$)', url).group(1).lower() == 'mp4':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Woops, get my vido homan")
        context.bot.send_video(chat_id=update.effective_chat.id, video=url)
    elif re.search('([^.]*$)', url).group(1).lower() == 'gif':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Auuuf, gifu too  hooman")
        context.bot.send_video(chat_id=update.effective_chat.id, video=url)
    else:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)


def fuck_you(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="That's mean hoomann")


def straight(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Give me straight commando homan")
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo='https://sun9-8.userapi.com/impf/GyuZ0QlLjKzHEiA4vQBVDHK0VPJ9TOy-N6MtmA/QR-V_JeaJ2c.jpg?size=774x580&quality=96&proxy=1&sign=648ab8dee624af9a849e1bc2a0139100&type=album')


def main():
    updater = Updater(token='1636258559:AAHZAH3upgHufb5xnAXRvcZGWkwHlY8TOKw', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex('([Yy]es|bop|[Ss]end|[Oo]f course|[Ss]ure|[Mm]ore)+'), bop))
    dp.add_handler(MessageHandler(Filters.regex('[Ff]uck you'), fuck_you))
    dp.add_handler(MessageHandler(Filters.regex('\w+'), straight))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
