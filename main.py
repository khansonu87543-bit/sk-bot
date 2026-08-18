from pyrogram import Client, filters
import asyncio
import random

# Telegram API Details & Bot Token
API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"
BOT_TOKEN = "8936926889:AAG6hOg66zUleGTgn50qx4CrdPdfnnXvowQ"

app = Client(
    "sk_ultimate_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Vibe and Poetry List for Silence/Boredom
POEMS_AND_VIBES = [
    "✨ **Time changes, life changes...** But true friends never change! What's up guys? 🥂",
    "🔥 **Cool breeze in the air and fire in the heart...** Let's start something new today! 🚀",
    "💫 **Smiling in solitude is an art...** But celebrating with friends is real fun! 😎",
    "🌹 **Fragrance of flowers and company of loved ones...** That's the real vibe here! 💖",
    "🌙 **Silence speaks a lot if you listen closely...** Why so quiet in the group today guys? 🎤"
]

GOOD_MORNING_WISHES = [
    "🌅 Good Morning! A new day, a new beginning—let's rock the group today! 🔥",
    "🌞 Good morning! The sun is up and the vibe is set, what's going on guys? ☕",
    "☀️ Morning everyone! Sending good vibes to all! 🙏"
]

# Random Emoji Reactions
AVAILABLE_REACTIONS = ["🔥", "👍", "❤️", "👏", "😎", "🤩", "💯", "🎉"]

@app.on_message(filters.all)
async def ultimate_bot_engine(client, message):
    if message.from_user and message.from_user.is_self:
        return

    # ==========================================
    # 1. PRIVATE CHAT (DM) HANDLER - जब कोई तुझे पर्सनल में बात करे
    # ==========================================
    if message.chat.type.name == "PRIVATE":
        text = message.text.lower() if message.text else ""
        
        # अगर पर्सनल चैट में भी ओनर के बारे में पूछे
        owner_keywords = [
            "owner", "oaner", "creator", "boss", "who made you", "malik kaun", 
            "tera malik", "baap", "kisne banaya", "dm", "link", "channel", 
            "contact", "id", "profile", "kaun hai"
        ]
        if any(word in text for word in owner_keywords):
            await message.reply_text(
                "👑 **Here are the official Owner details and links:**\n\n"
                "👤 **Main Owner 1:** t.me/SK_KING_CHILL\n"
                "👤 **Main Owner 2:** t.me/S_K_KI_NG\n"
                "📢 **Official Channel/Group:** t.me/SK_Chatting_Club\n\n"
                "Directly click the links above to contact the owners! 🚀"
            )
            return

        dm_replies = [
            "Hey buddy! The owners (@SK_KING_CHILL / @S_K_KI_NG) are currently offline. 📴\nDrop your message here, or check their profiles: t.me/SK_KING_CHILL & t.me/S_K_KI_NG",
            "Hello! Right now owners are away. For any query, contact them directly here:\n👤 t.me/SK_KING_CHILL\n👤 t.me/S_K_KI_NG",
            "Ram-Ram! You can directly reach out to the owners here:\n👉 t.me/SK_KING_CHILL\n👉 t.me/S_K_KI_NG"
        ]
        await message.reply_text(random.choice(dm_replies))
        return

    # ==========================================
    # 2. GROUP CHAT HANDLER - किसी भी ग्रुप में काम करने के लिए
    # ==========================================
    
    # Auto-Reaction System on every message
    try:
        random_reaction = random.choice(AVAILABLE_REACTIONS)
        await client.set_message_reaction(
            chat_id=message.chat.id,
            message_id=message.id,
            emoji=random_reaction
        )
    except Exception:
        pass

    # Welcome System for New Members in any group
    if message.new_chat_members:
        for member in message.new_chat_members:
            await message.reply_text(
                f"🔥 **Welcome {member.mention} to the group!** 🎉\n\n"
                f"Glad to have you here. Enjoy your stay and follow the rules! 🥂\n\n"
                f"👑 **Owners:** t.me/SK_KING_CHILL & t.me/S_K_KI_NG\n"
                f"📢 **Channel:** t.me/SK_Chatting_Club"
            )
        return

    if not message.text:
        # Media Block (Photos/Videos)
        if message.photo or message.video or message.document:
            await message.delete()
            await message.reply_text("🚫 **Hey!** Sending photos/videos is strictly not allowed here!", quote=True)
        return

    text = message.text.lower()

    # Good Morning / Greetings
    if any(w in text for w in ["good morning", "gm", "morning"]):
        await message.reply_text(random.choice(GOOD_MORNING_WISHES))
        return
    if any(w in text for w in ["hi", "hello", "hey", "sup"]):
        await message.reply_text("Hey there! How's it going? What's the plan for today? 😎")
        return

    # Bad Word / Abuse Block
    bad_words = ["badword1", "chutiya", "madarchod", "bhenchod", "lund", "bhosdike"]
    for word in bad_words:
        if word in text:
            await message.delete()
            warn = await message.reply_text(f"⚠️ {message.from_user.mention}, please do not use abusive language here!")
            await asyncio.sleep(4)
            await warn.delete()
            return

    # Link Protection (Anti-Link)
    if "http" in text or "t.me/" in text or "www." in text:
        if "t.me/" not in text:
            await message.delete()
            warn_msg = await message.reply_text(f"⚠️ {message.from_user.mention}, sharing external links is not allowed!")
            await asyncio.sleep(4)
            await warn_msg.delete()
            return

    # ==========================================
    # 3. ULTIMATE OWNER & LINK ASSISTANT (हर तरह के सवाल पर ओनर और चैनल की लिंक देना)
    # ==========================================
    owner_keywords = [
        "owner", "oaner", "creator", "boss", "who made you", "malik kaun", 
        "tera malik", "baap", "kisne banaya", "dm", "link", "channel", 
        "contact", "id", "profile", "kaun hai", "owner link", "owner dm"
    ]
    if any(word in text for word in owner_keywords):
        await message.reply_text(
            "🤖 **Listen up!** Here are all the official links and owner profiles you requested:\n\n"
            "👤 **Owner 1 DM:** t.me/SK_KING_CHILL\n"
            "👤 **Owner 2 DM:** t.me/S_K_KI_NG\n"
            "📢 **Official Channel/Group:** t.me/SK_Chatting_Club\n\n"
            "Click right now to connect with them directly! 🚀"
        )
        return

    # VC Control Commands
    if "vc open" in text or text == "/vcopen":
        await message.reply_text(
            "🚨 **Attention everyone!** Voice Chat (VC) has been opened by the owner's command! 🎙️🔥\n"
            "Jump into the VC right now!"
        )
        return

    if text == "/vckick" or text == "clear vc":
        await message.reply_text("🛡️ **Command Active:** Clearing unwanted people from the VC! ⚡")
        return

    # Poetry / Vibe Mode (जब ग्रुप में शांति या बोरियत हो)
    if any(w in text for w in ["shayari", "poetry", "bore", "silent", "peace", "shanti"]):
        await message.reply_text(random.choice(POEMS_AND_VIBES))
        return

    # Help Menu
    if text.startswith("/botinfo") or text.startswith("/help"):
        await message.reply_text(
            "🔥 **SK Ultimate Bot v6.0 (Ultimate Owner Link Edition)** 🔥\n\n"
            "🛡️ **Features Included:**\n"
            "• Instant Owner DM & Channel Link Dispatcher\n"
            "• Private DM Offline Auto-Responder\n"
            "• Auto-Reaction System (Emojis on messages)\n"
            "• Advanced Group Protection (Anti-Link & Anti-Abuse)\n"
            "• Auto Welcome & Good Morning Greetings\n"
            "• VC Management Commands\n"
            "• Poetry & Smart Chat Engine\n\n"
            "👑 **Owners:** t.me/SK_KING_CHILL & t.me/S_K_KI_NG\n"
            "📢 **Channel:** t.me/SK_Chatting_Club"
        )
        return

    # Start Command
    if text.startswith("/start"):
        await message.reply_text(
            "🔥 What's up! I am **SK Ultimate Bot**!\n"
            "Need the owner's DM or channel link? Just ask me anytime! 🚀\n\n"
            "👑 **Owners:** t.me/SK_KING_CHILL | t.me/S_K_KI_NG"
        )
        return

    # Human-like Chat Engine (When group has random chat)
    chat_replies = [
        "Yeah buddy, I'm listening! 🎧",
        "Absolutely right! What else is going on? 😎",
        "Is that so? What happened next? 🤔",
        "Haha true, the vibe in the group is amazing today! 🔥",
        "Damn right, you nailed that point! 💯"
    ]
    
    if len(text) > 2 and not text.startswith("/"):
        if random.randint(1, 4) == 1:
            await message.reply_text(random.choice(POEMS_AND_VIBES))
        else:
            await message.reply_text(random.choice(chat_replies))

print("🚀 SK Ultimate Bot (Full Power + Instant Owner Links) is running live...")
app.run()
