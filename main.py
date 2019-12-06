import sys

import zulip

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file="./.zuliprc")


def react_monkey(msg):
    """ React to all messages with the :monkey: emoji """
    client.add_reaction({"message_id": msg["id"], "emoji_name": "monkey"})


def react(msg):
    try:
        sys.stdout.write(str(msg))
        react_monkey(msg)
    except Exception:
        print("Caught exception")


# Message subscription
def main():
    client.call_on_each_message(lambda msg: react(msg))
