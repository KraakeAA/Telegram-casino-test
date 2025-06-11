from telethon.sync import TelegramClient

api_id = 18581709
api_hash = 'a92974bc6a79f87017552adfd19987d7'
phone = '+13468382420'  # Your current SMSPool number
sms_code = '49938'      # ⚠️ REPLACE THIS WITH YOUR FRESH CODE

client = TelegramClient('anon', api_id, api_hash)
client.start(phone, code_callback=lambda: sms_code)  # Auto-login
client.send_message('@YourCasinoChat', '/bet red 100')  # Test message
print("Success! Session saved for future runs.")
client.disconnect()
