import pandas as pd
import matplotlib.pyplot as plt
from sqlmodel import Session, select
from telegram import Update
from telegram.ext import (
    ContextTypes,
)
from stats_bot.db.models import Message, User
from stats_bot.db.client import engine
import io

from stats_bot.decorators.admin import admin

@admin
async def plot_table(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Generates a table of top 10 users by number of messages and average message length,
    and plots a bar chart to visualize the data.

    Args:
        update (Update): The update object containing information about the incoming message.
        context (ContextTypes.DEFAULT_TYPE): The context object containing bot-related information.

    Returns:
        None
    """
    msg = await update.effective_message.reply_text("Generating table...")
    data = []

    # fetch this data from database
    with Session(engine) as session:
        # users = session.exec(select(User)).all()
        messages = session.exec(
            select(Message).where(Message.group_id == update.effective_chat.id)
        ).all()
        # make a list of users, messages of whom are in the messages variable
        users = []
        for message in messages:
            if message.user_id not in users:
                users.append(message.user_id)
        # print(users)
        for user in users:
            usr = session.exec(select(User).where(User.id == user)).first()
            msgs = session.exec(
                select(Message.text).where(Message.user_id == usr.id)
            ).all()
            data.append((usr.username or str(usr.id), msgs))

    print(data)

    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data, columns=["user_id", "messages"])

    print(df)

    df["num_messages"] = df["messages"].apply(len)

    # Calculate average message length per user
    df["avg_message_length"] = df["messages"].apply(
        lambda x: sum(len(message) for message in x) / len(x)
    )

    # Sort users by number of messages and average message length
    df = df.sort_values(by=["num_messages", "avg_message_length"], ascending=False)

    # Plot top 10 users
    top_10_users = df.head(10)
    plt.figure(figsize=(10, 6))  # Fix: Correct spelling of figsize
    plt.bar(
        top_10_users["user_id"],
        top_10_users["num_messages"],
        color="blue",
        alpha=0.6,
        label="Number of Messages",
    )
    plt.xlabel("User ID")  # Fix: Correct spelling of xlabel
    plt.ylabel("Number of Messages")  # Fix: Correct spelling of ylabel
    plt.title("Top 10 Users by Number of Messages and Average Message Length")
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    await msg.delete()
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=buf,
        reply_to_message_id=msg.reply_to_message.message_id,
    )
