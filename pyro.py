import datetime
from pyrogram import Client, Filters
from pyrogram.api import functions


app_id = 1194939
app_hash = "d8ed4b10ed554767a4570cf59c3ea49e"

app = Client("my_account", api_id=app_id, api_hash=app_hash)

@app.on_message(Filters.audio)
def start(client,message):
    X=datetime.datetime.now()
    Y=X.strftime("%H:%M")
    while True:
        app.send(functions.account.UpdateProfile(
            first_name=str(Y),
            about="Soat: {}           Admin: Tilon".format(str(Y))
            ))

app.run()
