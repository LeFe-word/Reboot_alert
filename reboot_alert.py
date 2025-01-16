import requests
import configparser

# Укажите ваш Telegram Bot токен и Chat ID
BOT_TOKEN = "ВАШ_BOT_TOKEN"
CHAT_ID = "ВАШ_CHAT_ID"

def send_message(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")
def main():
    # Создаем объект ConfigParser
    config = configparser.ConfigParser()
    # Читаем файл конфигурации
    config.read("send.ini")

    try:
        # Извлекаем данные из секции [Telegram]
        token = config["Telegram"]["token"]
        chat_id = config["Telegram"]["chat_id"]
    except KeyError as e:
        print(f"Error: Missing configuration parameter: {e}")
        return

    # Отправка пакета
    send_message("Сервер был перезагружен.", token, chat_id)
if __name__ == "__main__":
    main()

