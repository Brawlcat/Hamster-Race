from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = '7122388735:AAGA24Nc12fZSB7MfEdbiayKZn3mQn5npx4'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        update = request.json
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        if text == '/start':
            response = "Welcome to the game!"
        else:
            response = play_game(text)  # Replace with your game logic

        send_message(chat_id, response)
        return 'OK'

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

def play_game(input_text):
    # Dummy game logic
    return f"You said: {input_text}"

if __name__ == '__main__':
    app.run(port=5000)
