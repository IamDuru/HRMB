import logging
import urllib.request
import urllib.parse
import json
import time

BOT_TOKEN = "8538642410:AAGj71gExkfqPtQPHKc6EmkrpGwvQLjQLmk"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

REPLY_MESSAGE = """🔐 This is an Advanced Security Protection Bot
🛡 Only Authorized Access Allowed

Access For ➤
⏤͟͞ 𝙆𝘼͢𝙍𝙏𝙄𝙆 -//- ⌯𝐄𝐌𝐈𝐍𝐄𝐍𝐂𝐄™༯

💎 Powered By ⌯𝐄𝐌𝐈𝐍𝐄𝐍𝐂𝐄™༯ Network"""

def get_updates(offset=None):
    url = API_URL + "getUpdates?timeout=100"
    if offset:
        url += f"&offset={offset}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            res = response.read()
            return json.loads(res.decode('utf-8'))
    except Exception as e:
        print(f"Error getting updates: {e}")
        return None

def send_message(chat_id, text):
    url = API_URL + "sendMessage"
    data = urllib.parse.urlencode({'chat_id': chat_id, 'text': text}).encode('utf-8')
    try:
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req) as response:
            return response.read()
    except Exception as e:
        print(f"Error sending message: {e}")

def main():
    print("Bot is running... Waiting for messages.")
    update_id = None
    while True:
        updates = get_updates(offset=update_id)
        if updates and "result" in updates:
            for item in updates["result"]:
                update_id = item["update_id"] + 1
                if "message" in item and "text" in item["message"]:
                    chat_id = item["message"]["chat"]["id"]
                    send_message(chat_id, REPLY_MESSAGE)
        time.sleep(1)

if __name__ == '__main__':
    main()
