from pyrogram.api import functions


app_id = 1194939
app_hash = "d8ed4b10ed554767a4570cf59c3ea49e"

app = Client("my_account", api_id=app_id, api_hash=app_hash)
app.send(functions.account.UpdateStatus(offline=False))
app.run()
