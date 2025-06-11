from telethon.sync import TelegramClient
import time, random

api_id = 18581709
api_hash = 'a92974bc6a79f87017552adfd19987d7'
phone = '+13468382420'  # 🔴 Your SMSPool number (must be active NOW)
chat = '@YourCasinoChat'

messages = ["/bet red 100", "Good luck! 🎰"]

print("Starting...")
with TelegramClient('anon', api_id, api_hash) as client:
    client.start(phone)  # 🔴 Add this line to auto-use the phone variable
    for _ in range(5):
        client.send_message(chat, random.choice(messages))
        time.sleep(random.randint(5, 30))
print("Done!")
