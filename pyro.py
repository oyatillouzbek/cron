import datetime
import time
import pytz
from pyrogram import Client, Filters
from pyrogram.api import functions


app_id = 1194939
app_hash = "d8ed4b10ed554767a4570cf59c3ea49e"

app = Client("my_account", api_id=app_id, api_hash=app_hash)
tz = pytz.timezone('Asia/Tashkent')
X=datetime.datetime.now(tz=tz)
Y=X.strftime("%H:%M")
while True:
    app.send(functions.account.UpdateProfile(first_name=str(Y),about="Soat: {}   Admin: Tilon".format(str(Y))))
    time.sleep(60)

while True:
    app.send(functions.account.UpdateStatus(offline=False))
    time.sleep(60)

    
app.run()
