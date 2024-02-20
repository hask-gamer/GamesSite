import requests


def send_message_to_telegram(message):
    bot_token = "6359732207:AAGnUwondsjczLIww2CGC_fxjKBpvZTwFcQ"
    group_id = -1001994832215
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={group_id}&text={message}"

    requests.get(url)