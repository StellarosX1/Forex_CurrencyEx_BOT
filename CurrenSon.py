import requests

# Telegram Bot token and chat ID
BOT_TOKEN = '8461716987:AAGUvWfglOvKQD3KbaT7IEWESHjBK-Hkb74'
CHAT_ID = '8270850877'
currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD']

def get_rates_to_inr():
    msg = "💱 Conversion to INR:\n"
    for cur in currencies:
        url = f"https://api.frankfurter.app/latest?from={cur}&to=INR"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            rate = data['rates']['INR']
            msg += f"{cur} to INR: {rate:.4f}\n"
        except Exception as e:
            print(f"Error fetching rate for {cur}: {e}")
            msg += f"{cur} to INR: Error\n"
    return msg

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text}
    response = requests.get(url, params=payload)
    return response.status_code == 200

if __name__ == "__main__":
    message = get_rates_to_inr()
    print("Sending message:\n", message)
    if send_to_telegram(message):
        print("Rates sent successfully.")
    else:
        print("Failed to send rates.")
