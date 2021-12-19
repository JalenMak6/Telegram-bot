from stock_function import *
import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

API_KEY = '79LEDAQZYWAS78X2'
token = '5013583990:AAHCh4ggSae1bVdXK2BWtG1ItWZye0TeR4I'

updater = Updater ( token )

logging.basicConfig (
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO
)

logger = logging.getLogger ( __name__ )


def start( update: Update, context: CallbackContext ) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2 (
        fr'Hi {user.mention_markdown_v2 ()} \!, this is a stock&crypto price tracker bot',
        reply_markup = ForceReply ( selective = True ),
    )

def echo( update: Update, context: CallbackContext ) -> None:
    """Echo the user message."""
    crypto = ['BTC', 'ETH', 'XRP', 'BCH', 'ADA', 'LTC', 'XEM', 'XLM', 'EOS', 'NEO', 'MIOTA', 'DASH', 'XMR', 'TRX',
              'XTZ', 'DOGE', 'ETC', 'VEN', 'USDT', 'BNB']
    update.message.reply_text ( "Please wait..." )
    if (update.message.text.isnumeric()):
        stock = update.message.text
        update.message.reply_text (hkstock(stock))
    elif update.message.text.upper() in crypto:
        stock = update.message.text
        update.message.reply_text(crypto_intraday(stock, API_KEY))
    else:
        stock = update.message.text
        update.message.reply_text((new_daily(stock, API_KEY)))

while True:
    updater.dispatcher.add_handler ( MessageHandler ( Filters.text & ~Filters.command, echo ) )
    updater.start_polling ()
    updater.idle ()