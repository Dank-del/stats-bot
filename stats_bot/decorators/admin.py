from telegram import Update
from telegram.ext import (
    ContextTypes,
)
from telegram.constants import ChatMemberStatus

def admin(func):
    """
    Decorator that checks if the user is an admin before executing the wrapped function.

    Args:
        func (callable): The function to be wrapped.

    Returns:
        callable: The wrapped function.

    """
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        member = await update.effective_chat.get_member(update.effective_user.id)
        if (
            member.status is not ChatMemberStatus.ADMINISTRATOR
            and member.status is not ChatMemberStatus.OWNER
        ):
            await update.message.reply_text("You are not an admin")
            return
        return await func(update, context)

    return wrapper