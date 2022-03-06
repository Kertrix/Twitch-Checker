# Twitch-Checker

## Usage

1. Clone the repo
2. Run the command `pip install -r requirements.txt`
3. Create a file `config.json` and paste this: 

	``` json
	{
		"token": "bot-token"
	}
	```

	Replace "bot-token" by your token.

3. For the twitch api, create a file `.env` and paste this:

	```
	CLIENT_ID=""
	SECRET_KEY=""
	```
	Add your twitch client id and secret key.
	
4. Don't forget to change your streamer's name in the [bot.by](bot.py) file

If you need help in any kind, don't hesitate to open an issue on this repo.
