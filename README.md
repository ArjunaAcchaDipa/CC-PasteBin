# C&C-Pastebin

C&C-Pastebin is a **Host Reconnaissance** script that can be run in the victim machine to get their **hostname**, **logged user**, and **current privileges** and the program is **100%** invisible. It will send the **Pastebin link** into your account through Telegram so the victim will not get any output from the script.

This repository was made to fulfill the assignment of **Programming of Penetration Testing**.

## Table of Contents
* [Prerequisite and Technology](#prerequisite-and-technology)
* [Installation](#installation)
* [Telegram Bot Example](#telegram-bot-example)
* [References](#references)

## Prerequisite and Technology
- Python 3 libraries
    - decouple
    - sys
    - subprocess
    - base64
    - requests.api
    - telegram_send
- Pastebin API
- Telegram API

## Installation

From your command line, clone and run **C&C-Pastebin**:
```bash
$ git clone https://github.com/ArjunaAcchaDipa/CC-Pastebin.git

# Change directory using your terminal or cmd.
$ cd CC-Pastebin/

# Copy the example env file and make the required configuration changes in the .env file.
$ cp .env.example .env

# Set up the telegram bot to send the Pastbin link
# To set the telegram bot, check this article
# https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580

# Make Pastebin account and request API
# Set up the needed API in .env

# Run the program using python3.
$ python3 hostReconnaissance.py
```

## Telegram Bot Example

![](img/resultExample.jpg)

## References
- BA07 - Programming for Penetration Testing Lab Class
- [https://programmerall.com/article/90051358161/](https://programmerall.com/article/90051358161/)
- [https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580)