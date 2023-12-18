# Stats Bot

Stats Bot is a Python-based Telegram bot that generates statistics about your group chat. It can provide insights such as the top 10 users by number of messages and average message length.

## Features

- **User Statistics**: The bot can generate a table of the top 10 users by the number of messages and average message length.
- **Group Statistics**: The bot can provide insights about the group such as the total number of messages, active users, etc. **[WIP]**
- **Data Visualization**: The bot can plot a bar chart to visualize the data it generates.

## Technologies Used

- [Python 3](https://www.python.org/)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [SQLite](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Matplotlib](https://matplotlib.org/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)

## Getting Started

To get started, add the bot to your group and send the `/textstats` command. The bot will then generate the statistics and send a message with the results.

### Development

This project uses Python 3.8+ and relies on several packages for its functionality. To set up a development environment, follow these steps:

- Clone the repository
- Create a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
- Install the dependencies: `pip install -r requirements.txt`
- Run the bot: `python -m stats_bot`

## Configuration

The bot uses a configuration file (`config.ini`) to store sensitive information such as the bot token. Make sure to create this file and add your bot token like so:

```ini
[stats_bot]
token = YOUR_BOT_TOKEN
```

### Running as a systemd service

To run the bot as a systemd service, create a file called `statsbot.service` in `/etc/systemd/system` and add the following:

```ini
[Unit]
Description=Stats Bot Service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/stats-bot
ExecStartPre=/usr/bin/python3 -m venv venv
ExecStartPre=/home/ubuntu/stats-bot/venv/bin/pip install -r requirements.txt
ExecStart=/home/ubuntu/stats-bot/venv/bin/python -m stats_bot
Restart=always

[Install]
WantedBy=multi-user.target
```

**Do not forget to change the `User` and `WorkingDirectory` fields to match your environment.**

Then, run the following commands to enable and start the service:

```bash
sudo systemctl enable statsbot.service
sudo systemctl start statsbot.service
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### License

This project is licensed under the terms of the MIT license.
