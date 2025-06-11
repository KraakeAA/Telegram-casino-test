import random
import time
import asyncio
from telethon.sync import TelegramClient, events
from telethon.tl.types import MessageEntityBotCommand

# --- Settings --- #
SESSION_NAME = 'anon'
API_ID = 18581709
API_HASH = 'a92974bc6a79f87017552adfd19987d7'
CHAT = 'solanagambleschat'  # Change to your target chat
GAME_COMMANDS = ['/darts', '/bowling', '/basketball']  # Add more if needed
DELAY_BETWEEN_GAMES = 30  # Seconds between games (avoid spam)

# --- Client Setup --- #
client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH,
    device_model="iPhone 15 Pro",
    system_version="17.4.1"
)

async def click_pvb_button(event):
    """Finds and clicks the 'Play PvB' button."""
    if event.buttons:
        for row in event.buttons:
            for button in row:
                if "pvb" in button.text.lower():
                    await button.click()
                    print(f"🎮 Clicked: {button.text}")
                    return True
    return False

async def play_games():
    await client.start()
    print("⚡ Bot started. Watching for game opportunities...")

    @client.on(events.NewMessage(chats=CHAT))
    async def listener(event):
        # Auto-click "Play PvB" when a game starts
        if await click_pvb_button(event):
            return

    while True:
        try:
            # Send random game command
            game_command = random.choice(GAME_COMMANDS)
            await client.send_message(CHAT, game_command)
            print(f"🎯 Sent: {game_command}")
            
            # Wait for game to load + button to appear
            await asyncio.sleep(5)  
            
            # Random delay before next game
            delay = random.randint(DELAY_BETWEEN_GAMES, DELAY_BETWEEN_GAMES * 2)
            print(f"⏳ Waiting {delay} sec...")
            await asyncio.sleep(delay)

        except Exception as e:
            print(f"❌ Error: {e}. Retrying in 10 sec...")
            await asyncio.sleep(10)

# --- Run --- #
with client:
    client.loop.run_until_complete(play_games())
