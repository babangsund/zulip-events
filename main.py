import zulip

# Pass the path to your zuliprc file here.
client = zulip.Client(config_file="./.zuliprc")


def react(msg):
    try:
        print(msg)
    except Exception:
        print("Caught exception")


# Message subscription
client.call_on_each_message(lambda msg: react(msg))
