from sqlmodel import Session
from telegram import Update
from telegram.ext import (
    ContextTypes,
)
from stats_bot.db.client import engine
from stats_bot.db.models import Group, Attachment, Message, User


async def handle_update(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    with Session(engine) as session:
        group = Group(
            id=update.message.chat.id,
            title=update.message.chat.title,
            username=update.message.chat.username,
            type=update.message.chat.type,
            members=await update.message.chat.get_member_count(),
        )
        session.merge(group)
        user = User(
            id=update.message.from_user.id,
            username=update.message.from_user.username,
            first_name=update.message.from_user.first_name,
            last_name=update.message.from_user.last_name,
        )
        session.merge(user)
        if not update.effective_message.from_user.is_bot:
            if update.effective_message.text:
                message = Message(
                    user_id=update.message.from_user.id,
                    group_id=update.message.chat.id,
                    text=update.message.text,
                    timestamp=update.message.date,
                )
                session.add(message)
            else:
                media = Attachment(
                    user_id=update.message.from_user.id,
                    group_id=update.message.chat.id,
                    message_id=update.message.message_id,
                    media_type=str(type(update.effective_message.effective_attachment))
                    .split(".")[-1]
                    .replace("'>", ""),
                    timestamp=update.message.date,
                )
                session.add(media)
        session.commit()
    # await update.message.reply_text(f"You said: {update.message.text}")
