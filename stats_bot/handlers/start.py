from telegram import Update
from telegram.ext import (
    ContextTypes,
)


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Sends a welcome message to the user.

    Args:
        update (Update): The update object containing information about the incoming message.
        context (ContextTypes.DEFAULT_TYPE): The context object containing bot-related information.

    Returns:
        None

    """
    await update.effective_message.reply_text(
        "Hi! I'm a bot that can generate statistics about your group chat. "
        "To get started, add me to your group and send /textstats to see the top 10 users by number of messages and average message length."
    )
