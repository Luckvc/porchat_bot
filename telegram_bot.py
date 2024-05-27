import logging
import vcf_conversion as vcf
import save_to_excel as save
from credentials import TELEGRAM_API_KEY
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá")

async def doc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('Request Recieved')
    new_file = await update.message.effective_attachment.get_file()
    await new_file.download_to_drive('contacts.vcf')
    print('File Downloaded')
    contacts_arr = vcf.convert_vcf_to_arr('contacts.vcf')
    save.append_to_spreadsheed(contacts_arr)
    print('Contatos salvos na planilha')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Contatos adicionados à planilha")



if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_API_KEY).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.add_handler(MessageHandler(filters.ATTACHMENT, doc))

    application.run_polling()