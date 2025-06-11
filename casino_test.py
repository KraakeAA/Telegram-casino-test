from telethon.sync import TelegramClient

api_id = 18581709
api_hash = 'a92974bc6a79f87017552adfd19987d7'
phone = '+13468382420'  # Your NEW SMSPool number

client = TelegramClient('anon', api_id, api_hash)
client.start(phone)  # This will FAIL but show the SMS prompt
