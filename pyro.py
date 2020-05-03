from pyrogram import Client, Filters
from pyrogram.api import functions
import datetime
import time
import pytz
api_id = 1194939
api_hash = "d8ed4b10ed554767a4570cf59c3ea49e"
app = Client("my_account",api_id,api_hash)
app.start()
while True:
    ok = pytz.timezone(Asia/Tashkent)
    x = datetime.datetime.now(tz=ok)
    x = x.strftime("%H:%M")
    app.send(functions.account.UpdateProfile(
    first_name=str(x),
    about="time" +str(x)
    ))
    time.sleep(30)
