# zulip-events

Message callback events in Zulip

## Installation

1. Clone the repository.
   `$ git clone https://github.com/babangsund/zulip-events`
2. Enter the directory.
   `$ cd zulip-events`
3. Install dependencies using [pipenv](https://pipenv.kennethreitz.org/en/latest/):
   `$ pipenv install`

## Usage

1. Create a `.zuliprc` in the project directory. You will need to provide a Zulip API key herein.

   ```rc
   [api]
   key=MY_API_KEY
   email=MY_EMAIL
   site=https://zulip.MYDOMAIN.com
   ```

2. Make sure you have a giphy API key bound to `GIPHY_API_KEY` in your environment path.
3. Enter the virtual Python environment by typing `pipenv shell`.
4. Start listening `python main.py`.

---

## Credits

zulip-events is built and maintained by **babangsund**.  
[@blog](https://babangsund.com/).  
[@github](https://github.com/babangsund).  
[@twitter](https://twitter.com/babangsund).
