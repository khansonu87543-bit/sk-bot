import asyncio
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyrogram import Client, filters
import random
from flask import Flask
from threading import Thread

# --- Flask Web Server (24/7 Keep-Alive) ---
web_app = Flask('')
@web_app.route('/')
def home():
    return "SK Ultimate Bot is running 24/7, 365 days!"

def run_web():
    web_app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# --- Configuration ---
API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"
BOT_TOKEN = "8936926889:AAG6hOg66zUleGTgn50qx4CrdPdfnnXvowQ"

app = Client("sk_ultimate_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- Data Lists ---
POEMS = [
    "Time changes, life changes... but true friends never change! 🥂",
    "Smiling in solitude is an art, but celebrating with friends is real fun! 😎",
    "Silence speaks a lot if you listen closely... 🎤"
]
GOOD_MORNING = ["Good morning! A new day, a new beginning! 🔥", "Morning everyone! Have a great day! ☕"]
AVAILABLE_REACTIONS = ["🔥", "👍", "❤️", "👏", "😎", "🤩", "💯", "🎉"]

# --- Main Bot Engine (All Features Included) ---
@app.on_message(filters.all)
async def main_engine(client, message):
    if message.from_user and message.from_user.is_self:
        return

    # 1. Private Chat Handler (DM)
    if message.chat.type.name == "PRIVATE":
        text = message.text.lower() if message.text else ""
        if any(w in text for w in ["owner", "link", "channel", "creator"]):
            await message.reply_text("👑 Owners: t.me/SK_KING_CHILL / t.me/S_K_KI_NG\n📢 Channel: t.me/SK_Chatting_Club")
            return
        await message.reply_text("Hey! The owners are currently offline. Drop your message here!")
        return

    # 2. Welcome System for New Members
    if message.new_chat_members:
        for member in message.new_chat_members:
            await message.reply_text(
                f"🔥 Welcome {member.mention} to the group! 🎉\n\n"
                f"👑 Owners: t.me/SK_KING_CHILL & t.me/S_K_KI_NG\n"
                f"📢 Channel: t.me/SK_Chatting_Club"
            )
        return

    if not message.text:
        # Media Protection (Photos/Videos block if needed)
        return

    text = message.text.lower()

    # 3. Pin Command
    if text.startswith("/pin") and message.reply_to_message:
        await client.pin_chat_message(message.chat.id, message.reply_to_message.id)
        await message.reply_text("📌 Message pinned successfully!")
        return

    # 4. Purge Command (Clear messages)
    if text.startswith("/purge") and message.reply_to_message:
        chat_id = message.chat.id
        message_ids = []
        msg_id = message.reply_to_message.id
        while msg_id <= message.id:
            message_ids.append(msg_id)
            msg_id += 1
            if len(message_ids) == 100:
                await client.delete_messages(chat_id, message_ids)
                message_ids = []
        if message_ids:
            await client.delete_messages(chat_id, message_ids)
        await message.reply_text("🧹 Purge complete! Messages cleaned.")
        return

    # 5. Salam - Dua System
    if "assalamualaikum" in text or "assalam o alaikum" in text:
        await message.reply_text("Walaikum Assalam! 😊")
        return
    elif "khuda hafiz" in text:
        await message.reply_text("Allah Hafiz! 🤲")
        return
    elif "allah hafiz" in text:
        await message.reply_text("Khuda Hafiz! 🤲")
        return

    # 6. Bad Word Block (Anti-Abuse)
    bad_words = ["chutiya", "madarchod", "bhenchod", "lund", "bhosdike"]
    for word in bad_words:
        if word in text:
            await message.delete()
            warn = await message.reply_text(f"⚠️ {message.from_user.mention}, please do not use abusive language!")
            await asyncio.sleep(4)
            await warn.delete()
            return

    # 7. Link Protection (Anti-Link)
    if "http" in text or "t.me/" in text or "www." in text:
        if "t.me/" not in text:
            await message.delete()
            warn_msg = await message.reply_text(f"⚠️ {message.from_user.mention}, external links are not allowed!")
            await asyncio.sleep(4)
            await warn_msg.delete()
            return

    # 8. General Commands & Owner Info
    if any(w in text for w in ["owner", "link", "channel", "creator"]):
        await message.reply_text("👑 Owners: t.me/SK_KING_CHILL / t.me/S_K_KI_NG\n📢 Channel: t.me/SK_Chatting_Club")
        return

    if any(w in text for w in ["good morning", "gm", "morning"]):
        await message.reply_text(random.choice(GOOD_MORNING))
        return

    if any(w in text for w in ["shayari", "poetry", "bore"]):
        await message.reply_text(random.choice(POEMS))
        return

    if text.startswith("/start") or text.startswith("/help"):
        await message.reply_text("🔥 SK Ultimate Bot v8.0 (24/7 Active Mode)\nRunning forever without downtime!")
        return

    # 9. Auto-Reaction System
    try:
        await client.set_message_reaction(chat_id=message.chat.id, message_id=message.id, emoji=random.choice(AVAILABLE_REACTIONS))
    except: pass

# --- Start System ---
if __name__ == "__main__":
    keep_alive()
    print("🚀 SK Ultimate Bot: System status - 24/7 Active, Never Sleeping, Full Power!")
    app.run()
    
