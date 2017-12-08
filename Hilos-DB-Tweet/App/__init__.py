import threading

from tweepy import Stream, OAuthHandler, API,cursor
from tweepy.streaming import StreamListener
from tweepy.models import User
import json
import sqlite3

# db = sqlite3.connect('DB/db-tweet')
# cursor = db.cursor()
# try:
#     cursor.execute('''CREATE TABLE tweet (ID INTEGER PRIMARY KEY, TWEET TEXT)''')
#
# except Exception as e:
#     print('TABLA SUCCESS')
#     pass

ckey = 'Xh75msLLO9uKdvQzWB0BN4ngE'
csecret = 'Hfn56qzfJxcfdRyxyqafF5DmUt4xjGZWN6Zh15Oyr5UScwJXJL'
atoken = '2935386020-XJOF2nmkcs527kxKWNAv0uYYdz5aT97VpbThub1'
asecret ='cBdCC3yYm3IdXfaNNnfVRZ5rPgKSxtynKsRekDNmh5C0K'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = API(auth)

class TLListener(StreamListener):
    def on_data(self,raw_data):
        data = json.loads(raw_data)
        status = User.parse(self.api, data)
        tweet = status.text
        print(tweet)
        return (True)


    def on_error(self, status_code):
        if status_code == 420:
            return False

def crear_datos(data_h, c):
    for d in data_h:
        evt = threading.Event()
        c.put(d, evt)




try:
    twStream = Stream(auth,TLListener())
    twStream.filter(track=['#USA'])
except Exception as e:
    print(e)
    print('Imprimio este error')
    pass