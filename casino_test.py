from telethon.sync import TelegramClient
import time, random

api_id = 18581709                             # From your screenshot
api_hash = 'a92974bc6a79f87017552adfd19987d7' # From your screenshot
phone = '+13468382420'                        # Your number (with country code)
chat = '@YourCasinoChat'                      # Your casino chat username

messages = [
    "/bet red 100",
    "/spin 200",
    "Let’s play! 🎲",
    "Feeling lucky! 🍀"
]

print("Starting...")
with TelegramClient('anon', api_id, api_hash) as client:
    client.start(phone)
    print("Logged in! Sending messages...")
    
    for _ in range(10):  # Sends 10 messages
        msg = random.choice(messages)
        client.send_message(chat, msg)
        print(f"Sent: {msg}")
        time.sleep(random.randint(5, 30))  # Random delay
    
    print("Done!")
