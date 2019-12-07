import os
import sys

import requests
import zulip

# Pass the path to your zuliprc file here.
api_key = os.environ["API_KEY"]
client = zulip.Client(config_file="./.zuliprc")


def react_monkey(msg):
    """ React to all messages with the :monkey: emoji """
    client.add_reaction({"message_id": msg["id"], "emoji_name": "monkey"})


def react_giphy(msg):
    """ React to messages starting with '/giphy ', and respond with a gif. """
    type = "stream"
    subject = msg["subject"]
    content = msg["content"]
    to = msg["display_recipient"]

    if isinstance(to, list):
        type = "private"
        to = to[0]["email"]

    if content.startswith("/giphy "):
        content = content.split("/giphy ", 1)[1]
        giphy_request = (
            "https://api.giphy.com/v1/gifs"
            + "/random?lang=en"
            + f"&tag={content}"
            + f"&api_key={api_key}"
        )

        json = requests.request(method="GET", url=giphy_request).json()
        gif = json["data"]["images"]["original"]["url"]
        client.send_message(
            {"type": type, "to": to, "subject": subject, "content": gif}
        )


def react(msg):
    """ Safely react to message events """
    try:
        sys.stdout.write(str(msg))
        react_monkey(msg)
        react_giphy(msg)
    except Exception:
        print("Caught exception")


def main():
    """ Subscribes to all message events """
    client.call_on_each_message(lambda msg: react(msg))
