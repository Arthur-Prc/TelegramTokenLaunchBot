from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'SEU_BOT_TOKEN'

# Função de boas-vindas
def welcome(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        f"👋 Olá {user.first_name}! Bem-vindo ao grupo {update.effective_chat.title}!"
    )

# Função de aviso automático (ex: lançamento ou anúncio)
def announcement(update: Update, context: CallbackContext):
    message = "🚀 Lançamento do token hoje às 20h! Não perca!"
    update.message.reply_text(message)

# Comando de ajuda
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Comandos disponíveis: /start /announcement /help")

# Anti-spam simples: bloqueia links não autorizados
def anti_spam(update: Update, context: CallbackContext):
    if "http" in update.message.text:
        update.message.delete()
        update.message.reply_text("❌ Links não autorizados removidos.")

# Main
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", welcome))
    dp.add_handler(CommandHandler("announcement", announcement))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, anti_spam))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
