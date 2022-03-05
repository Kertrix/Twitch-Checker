import calendar
from datetime import datetime
import os
import time
from dotenv import load_dotenv
import requests

load_dotenv()

class CheckTwitch:

    CLIENT_ID = os.environ["CLIENT_ID"]
    CLIENT_SECRET = os.environ["SECRET_KEY"]

    body = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)

    keys = r.json()

    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': 'Bearer ' + keys['access_token']
    }

    async def check_streamer(self, streamer_name):
        stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=self.headers)

        stream_data = stream.json();

        if len(stream_data['data']) == 1:
            timestamp = calendar.timegm(datetime.strptime(stream_data['data'][0]['started_at'], "%Y-%m-%dT%H:%M:%SZ").timetuple())
            if (time.time() - timestamp) < 6000:
                data = [stream_data['data'][0]['game_name'], stream_data['data'][0]['title'], stream_data['data'][0]['started_at']]
                return data
            else:
                return None
        else:
            return None