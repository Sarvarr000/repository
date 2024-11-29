from twilio.rest import Client
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Twilio uchun o'zgaruvchilar
TWILIO_SID = "SKd4c51544ef4ebb5a4cd8f78508fcecdc"
TWILIO_AUTH_TOKEN = "77485e269d95855660d1bbdc09b983e7"
TWILIO_PHONE_NUMBER = "+99891016631"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Telegram bot funksiyasi
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom! Telefon raqamini yuboring (masalan, +998901234567):")

def send_sms(update: Update, context: CallbackContext):
    phone_number = update.message.text
    try:
        # SMS jo'natish
        message = client.messages.create(
            body="Salom ishlar qalay bir tanishing seni yo'qladi.",  # SMS matni
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        update.message.reply_text("SMS yuborildi!")
    except Exception as e:
        update.message.reply_text(f"Xatolik: {e}")

# Botni sozlash
def main():
    TELEGRAM_TOKEN = "7082154548:AAH1kfnQF9RpoErhc2C1UwkL9ftFTCO0MjM"
    updater = Updater(TELEGRAM_TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, send_sms))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
