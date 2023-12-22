from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)
import logging, configparser
import stats_bot.db.client as client
from stats_bot.handlers.start import start
from stats_bot.handlers.group import handle_update
from stats_bot.handlers.plot import attachment_stats, plot_table

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger(__name__)

configparser = configparser.ConfigParser()
configparser.read("config.ini")


app = (
    ApplicationBuilder().token(configparser.get("stats_bot", "token")).build()
)
app.add_handler(CommandHandler("start", start, filters=filters.ChatType.PRIVATE))
app.add_handler(CommandHandler("attachmentstats", attachment_stats, filters=filters.ChatType.GROUPS))
app.add_handler(CommandHandler("textstats", plot_table, filters=filters.ChatType.GROUPS))
app.add_handler(MessageHandler(filters.ChatType.GROUPS, handle_update))

if __name__ == "__main__":
    logging.info("Creating database")
    client.load_tables()
    logging.info("Starting bot")
    app.run_polling()
