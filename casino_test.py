from telethon.sync import TelegramClient
import time, random

api_id = 18581709
api_hash = 'a92974bc6a79f87017552adfd19987d7'
phone = '+13468382420'  # Your ACTIVE SMSPool number
chat = '@YourCasinoChat'  # Your exact chat username

messages = ["/bet red 100", "Good luck! 🎰"]

print("Starting...")
client = TelegramClient('anon', api_id, api_hash)
client.start(phone)  # 🔴 Critical: Forces non-interactive mode
for _ in range(5):
    client.send_message(chat, random.choice(messages))
    time.sleep(random.randint(5, 30))
client.disconnect()
print("Done!")
