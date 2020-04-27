from pyrogram import Client, Filters
from pyrogram.api import functions

import random, time, requests

headers = {
    'authority': 'thispersondoesnotexist.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
}

names = []
app_id = 1194939
app_hash = "d8ed4b10ed554767a4570cf59c3ea49e"

with open("./names.txt", "r") as file:
	names = file.read().split('\n')
	file.close()

app = Client(
	"my_account",
	api_id=app_id,
	api_hash=app_hash)

@app.on_message(None)
def hello(client, message):
    while True:
        with open('./profile.jpeg', 'wb') as f:
            f.write(requests.get('https://thispersondoesnotexist.com/image', headers=headers).content)
            app.set_profile_photo(photo="./profile.jpeg")
            app.send(functions.account.UpdateProfile(first_name=random.choice(names), last_name=random.choice(names)))
            time.sleep(60)

app.run()
