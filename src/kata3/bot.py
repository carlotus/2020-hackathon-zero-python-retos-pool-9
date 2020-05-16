import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    respuesta = update.message.reply_text("Hola, Geeks!")
    return respuesta



def help(update, context):
    respuesta = "Ayudame!"
    update.message.reply_text(respuesta)
    return respuesta

def mayus(update, context):
    respuesta = " ".join(context.args).upper()
    update.message.reply_text(respuesta)
    return respuesta

def alreves(update, context):
    respuesta = update.message.text[::-1]
    update.message.reply_text(respuesta)
    return respuesta

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater(token="1240930414:AAGWs4GdCPA0vEFJAInayRhnI1lsxqRFHOs", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("mayus", mayus))
    dp.add_handler(CommandHandler("alreves", alreves))


    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #
    dp.add_handler(MessageHandler(Filters.text, alreves))
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
