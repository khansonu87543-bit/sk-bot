import asyncio
from pyrogram import Client, filters
import random
from flask import Flask
from threading import Thread

# --- Flask Web Server (Keep-Alive) ---
web_app = Flask('')

@web_app.route('/')
def home():
    return "SK Bot is Alive 24/7!"

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

# --- All Features Data Lists ---
SONGS = [
    "🎶 Now Playing: Lo-fi Beats to Relax/Study to (Vibing in background) ✨",
    "🎵 Playing your favorite track: Romantic Hindi Mashup 🎸",
    "🎧 Playing: Energetic Party Remix - Non-stop beat! 🔥",
    "🎶 Now Playing: Soulful Acoustic Guitar Melody 🎻"
]

CHAT_RESPONSES = [
    "Acha ji! Aur batao, kya chal raha hai phir? 😄",
    "Sahi hai bhai! Main toh bas aap logo ki baatein sun raha hoon. 😎",
    "Waise aapki yeh baat mujhe kaafi interesting lagi! Kuch aur batao इसके बारे में। 🤔",
    "Hahaha, kasam se aap bhi na kamaal ki baatein karte ho! 😆",
    "Main samajh gaya aapki baat. Batao phir aage kya plan hai? 👍"
]

POEMS = [
    "Time changes, life changes... but true friends never change! 🥂",
    "Smiling in solitude is an art, but celebrating with friends is real fun! 😎",
    "Silence speaks a lot if you listen closely... 🎤"
]

AVAILABLE_REACTIONS = ["🔥", "👍", "❤️", "👏", "😎", "🤩", "💯", "🎉"]

# --- Main Bot Engine ---
@app.on_message(filters.all)
async def main_engine(client, message):
    if message.from_user and message.from_user.is_self:
        return

    # 1. Private Chat DM Handler
    if message.chat.type.name == "PRIVATE":
        text = message.text.lower() if message.text else ""
        if any(w in text for w in ["owner", "link", "channel"]):
            await message.reply_text("👑 Owners: t.me/SK_KING_CHILL / t.me/S_K_KI_NG\n📢 Channel: t.me/SK_Chatting_Club")
            return
        await message.reply_text("Hey! The owners are offline right now. Drop your message here or type song/chat to interact!")
        return

    # 2. Welcome System
    if message.new_chat_members:
        for member in message.new_chat_members:
            await message.reply_text(
                f"🔥 Welcome {member.mention} to the group! 🎉\n\n"
                f"👑 Owners: t.me/SK_KING_CHILL & t.me/S_K_KI_NG\n"
                f"📢 Channel: t.me/SK_Chatting_Club"
            )
        return

    if not message.text:
        return

    text = message.text.lower()

    # 3. Pin Command
    if text.startswith("/pin") and message.reply_to_message:
        await client.pin_chat_message(message.chat.id, message.reply_to_message.id)
        await message.reply_text("📌 Message pinned successfully!")
        return

    # 4. Purge Command (Clear Messages)
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

    # 5. Music System
    if any(w in text for w in ["play music", "gana bajao", "song", "music", "play"]):
        await message.reply_text(random.choice(SONGS))
        return

    # 6. Chat/Conversation System
    if any(w in text for w in ["hello bot", "kya haal", "kaise ho", "bhai", "suno", "bot"]) or (message.reply_to_message and message.reply_to_message.from_user.is_self):
        await message.reply_text(random.choice(CHAT_RESPONSES))
        return

    # 7. Salam - Dua System
    if "assalamualaikum" in text or "assalam o alaikum" in text:
        await message.reply_text("Walaikum Assalam! 😊")
        return
    elif "khuda hafiz" in text or "allah hafiz" in text:
        await message.reply_text("Allah Hafiz! 🤲")
        return

    # 8. Bad Word Block (Anti-Abuse)
    bad_words = ["chutiya", "madarchod", "bhenchod", "lund", "bhosdike"]
    for word in bad_words:
        if word in text:
            await message.delete()
            return

    # 9. Link Protection (Anti-Link)
    if "http" in text or "t.me/" in text or "www." in text:
        if "t.me/" not in text:
            await message.delete()
            return

    # 10. Owner Info & Poetry
    if any(w in text for w in ["owner", "link", "channel", "creator"]):
        await message.reply_text("👑 Owners: t.me/SK_KING_CHILL / t.me/S_K_KI_NG\n📢 Channel: t.me/SK_Chatting_Club")
        return

    if any(w in text for w in ["shayari", "poetry", "bore"]):
        await message.reply_text(random.choice(POEMS))
        return

    if text.startswith("/start") or text.startswith("/help"):
        await message.reply_text("🔥 SK Ultimate Bot v10.0 (24/7 Active Mode)\nMusic, Chat, Protection - Everything is Online!")
        return

    # 11. Auto-Reaction System# 11. Auto-Reaction System
try:
    await client.set_message_reaction(message.chat.id, message.id, "🔥")
except:
    pass

# --- Start System properly with Event Loop ---
if __name__ == "__main__":
    try:
        keep_alive()
    except NameError:
        pass
        
    print("🚀 SK Ultimate Bot: System status - 24/7 Active!")
    
    import asyncio
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    app.run()
    
