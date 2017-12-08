#Api_key de twitter

from tweepy import Stream, OAuthHandler, API, Cursor
from tweepy.streaming import StreamListener
from tweepy.models import User
import json
import sqlite3

db = sqlite3.connect('DB/prueba')
cursor = db.cursor()
try:
    cursor.execute('''CREATE TABLE USUARIO(ID INT PRIMARY KEY, NOMBRE TEXT, TWEETS TEXT, CREADO TEXT)''')
except Exception as e:
    print('TABLA SUCCESS!')
    pass

ckey = 'Xh75msLLO9uKdvQzWB0BN4ngE'
csecret = 'Hfn56qzfJxcfdRyxyqafF5DmUt4xjGZWN6Zh15Oyr5UScwJXJL'
atoken = '2935386020-XJOF2nmkcs527kxKWNAv0uYYdz5aT97VpbThub1'
asecret ='cBdCC3yYm3IdXfaNNnfVRZ5rPgKSxtynKsRekDNmh5C0K'

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = API(auth)

# #Este trae los 10 ultimos twees que han subido a tu visualizacion
# for status in Cursor(api.home_timeline).items(10):
#     print(status)
# #Este trae la lista de tus amigos |
# for seguidor in Cursor(api.friends).items(10):
#     print(seguidor)

class TLListener(StreamListener):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        status = User.parse(self.api, data)
        location = status.user['location']
        if location == None:
            location = 'No Activado'
            print(location)
        # ------------------#
        print(location)
        print(status)
        # print(status.user['name']+': '+ status.text)
        creado = status.created_at
        id = status.id
        nom = status.user['name']
        tweet = status.text
        cursor.execute('''INSERT INTO USUARIO(ID, NOMBRE, TWEETS, CREADO) VALUES(?,?,?,?)''', (id, nom, tweet, creado))
        db.commit()
        return (True)

    def on_error(self, status_code):
        if status_code == 420:
            return False

try:
    twStream = Stream(auth, TLListener())
    twStream.filter(track=['#USA'])
except Exception :
    pass