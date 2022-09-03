import requests


def start_command(update, context):
    return update.message.reply_text("Hello, Welcome to Devocoe!")


def help_command(update, context):
    return update.message.reply_text(
        "If you need any help contact me via email at piyushprasad816@gmail.com")


def send_qoute(update, context):

    res = requests.get(
        "https://goquotes-api.herokuapp.com/api/v1/random?count=1")

    data = res.json()

    qoute = data.get("quotes")[0]

    return update.message.reply_text(
        f"{qoute['text']}\n\n\nBy - {qoute['author']}")


def message_handler(update, context):

    if("qoute" in update.message.text):
        return send_qoute(update, context)

    return update.message.reply_text(f"you said {update.message.text}")
