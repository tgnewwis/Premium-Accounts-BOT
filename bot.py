from time import sleep
import datetime 
import asyncio
from config import *
import pymongo
import random
import traceback
from pyrogram import filters, Client
from pyrogram.types import ForceReply,InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant,FloodWait
import pyromod.listen
import pytz

Time_Zone = "Asia/Kolkata"
zone = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))  
timer = zone.strftime("%I:%M %p")
dater = zone.strftime("%b %d")  
date = f"2022 {dater}:{timer}"

client = pymongo.MongoClient(DATABASE)
acc = client["ACC"]
db = client["bot"]
userdb = db["user"]

app = Client("giveaway",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN,)

app.start()
x = app.get_me()
BOT_USERNAME = x.username
ADMIN = BOT_OWNER


async def acc_provide(_, m: Message, help_option: str):
    chat_id = int(help_option.split("_")[1])
    name = ADMIN
    acc= help_option.split("_")[2]
    m = await app.send_message(
                chat_id=name,
                text="Enter **Email** of acoount",reply_markup=ForceReply(selective=True))
    point = await app.listen(name, filters=None, timeout=60)
    await m.delete() 
    x = await app.send_message(
                chat_id=name,
                text="Enter **password** of account",reply_markup=ForceReply(selective=True))
    sems = await app.listen(name, filters=None, timeout=60)
    await app.send_message(
                chat_id=name,
                text="Done! payment sucsessfull✅")
    await app.send_message(
                chat_id=-1001518620432,
                text=(
                    f"✅ ** New Withdraw Paid**\n\n"
                    f"🆔 **User id**: `{chat_id}`\n\n"
                    f"💰 **Amount **: 5 coin\n\n"
                    f"📦 **Account type**:{acc}\n\n"
                    f"🍃 **Bot** : [@{BOT_USERNAME}](https://t.me/{BOT_USERNAME}?start=5246051676)\n\n"
                    f"[❗️ ADD](https://t.me/EpicPaymentProof/2) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)
    await x.delete() 
    await app.send_sticker(chat_id,"CAACAgEAAxkBAAEGVaVibOE9cIWB7CtNX4kdJnH9_M9M8wAC6wcAAuN4BAABnwXByysQy_ceBA",reply_markup=keyboard)
    await app.send_message(
                chat_id=chat_id,
                text=(
                    f"💬 Hello sir this your {acc} Account \n\n"
                    f"📧 **Email** : `{point.text}`\n"
                    f"🔐 **Password** :`{sems.text}`\n\n"
                    f"[❗️ ADD](https://t.me/EpicPaymentProof/2╔═════ೋೋ═════╗

🤩ʟᴏɢᴏ ɢɪᴠᴇᴀᴡᴀʏ ᴛɪᴍᴇ🤩

🔰ᴍᴡ ɢɪᴠᴇᴀᴡᴀʏ

✍ᴄᴏᴅᴇ - ʟᴏɢᴏ ᴏɴᴇ🥲

✅ᴡɪɴɴᴇʀ - 30ᴛʜ ᴄᴏᴍᴍᴇɴᴛ  

🧑‍💻ɢɪᴠᴇᴀᴡᴀʏ ʙʏ @wisula4

╚═══❖•ೋ° °ೋ•❖═══╝) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)
    return 


async def contact_admin(_, m: Message, help_option: str):
    chat_id = int(help_option.split("_")[1])
    question = help_option.split("_")[2]
    name = ADMIN
    m = await app.send_message(
                chat_id=name,
                text="Enter message here",reply_markup=ForceReply(selective=True))
    point = await app.listen(name, filters=None, timeout=60)
    await app.send_message(
                chat_id=name,
                text="Done! Message was sent user DM.")
    await m.delete() 
    await app.send_message(
         chat_id=chat_id,
                text=(f"""
💭 <u>**Message From Admin**</u>

🔹 Question:{question}
🔹 Answer : {point.text}  """))
    return  


@app.on_message(filters.command("start") & ~filters.group)
async def start(_, message: Message):
	umention = message.from_user.mention
	user_id = message.from_user.id
	if len(message.text.split()) > 1:
		try:
			name = (message.text.split(None, 1)[1]).lower()
			if name.startswith("acc"):
				await acc_provide(app, message, name)
				return
			if name.startswith("contact"):
				await contact_admin(app, message, name)
				return
			if int(name) !=user_id:
				supun = userdb.find_one({"username": user_id})
				if supun != None and supun["username"] == int(user_id):
					await app.send_sticker(user_id, "CAACAgUAAxkBAAEFYcVi37qOtZB2bKEAAUytIz-HbIiVSwcAAssGAAK7_uhWUZrkOw-u48QpBA)
					await app.send_message(chat_id=user_id, text=f"Already started ..🙄")
					return
				if supun == None:
					await app.send_sticker(user_id, random.choice(STICKER), reply_markup=keyboard)
					await message.reply_text(START_TEXT.format(umention), disable_web_page_preview=True, reply_markup=comman)
					await app.send_message(chat_id=user_id, text=f"🚀 **You were invited by user** : {name}")
					data = userdb.find({'username': int(name)})
					if data == None:
						return
					for d in data:
						balance = d["wallet"]
					userdb.update_one({"username": int(name)}, {
							"$set": {"wallet": int(balance)+1}})
					await app.send_message(
					  	chat_id=int(name),
					  	text=(
						  f"✅ {umention} **entered the robot through your link**.\n💰**Received +1 $**"
					  )
					)
					Data = {
					  'username': user_id,
					  'wallet': 0,
					  'date': date,
                      'fsub' : 0
				  	}
					userdb.insert_one(Data)
		except:
			await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))
		return
	else:
		await app.send_sticker(user_id,random.choice(STICKER),reply_markup=keyboard)
		await message.reply_text(START_TEXT.format(umention),disable_web_page_preview=True,reply_markup=comman)
		pocket = userdb.find_one({'username': int(user_id)})
		if pocket == None:
			Data = {
				'username': user_id,
				'wallet': 0,
				'date': date,
                'fsub' : 0
			}
			userdb.insert_one(Data)
		return 
	     
@app.on_message(filters.private & filters.regex(pattern="📮 Referral"))
async def refferal(_, message: Message):
    name = message.from_user.id
    await app.send_sticker(name,random.choice(STICKER),reply_markup=keyboard)
    try:
       await message._client.get_chat_member(int(CHANNEL_ID), message.from_user.id)
       link = await app.create_chat_invite_link(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID))
   
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}
❗️ You Must Join This Channel First !
""",
     reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("🚀 Join Now  ", url=f"{link}"),
                 ],
             ]
            ))
       return
    url = f"https://t.me/{BOT_USERNAME}?start={name}"
    await app.send_photo(name,
      "https://te.legra.ph/file/6d8c3ee84fd7bb11f8c5c.mp4",
      caption = f"""
✅ **Premium Accounts BOT**

❤️ Premium Accounts.
👥 Normal Accounts.
🔐 Safe and secure payment.
🤩 owner @wisula4

🔗{url} """)
    sleep(2.0)
    await app.send_message(chat_id=name, text=REF.format(name))


@app.on_message(filters.private & filters.regex(pattern="☎️ Support"))
async def refferal(_, message: Message):
    try:
       await message._client.get_chat_member(int(CHANNEL_ID), message.from_user.id)
       link = await app.create_chat_invite_link(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID))
   
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}
❗️ You Must Join This Channel First !
""",
     reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("🚀 Join Now  ", url=f"{link}"),
                 ],
             ]
            ))
       return
    name = message.from_user.id
    names = message.from_user.id
    await app.send_sticker(name,"CAACAgEAAxkBAAEGRG9ia1ktrH_wOZpci8kQzVP0K5hhBQACIwkAAuN4BAABn1mg9roZ0DkeBA",reply_markup=keyboard)
    nam = message.from_user.mention
    m = await app.send_message(
                chat_id=name,
                text=SUPORT,reply_markup=back)
    point = await app.listen(name, filters=None, timeout=60)
    if point.text[0] == "«":
        await app.send_message(
                chat_id=name,
                text="🔙 You have returned to the main menu",reply_markup=keyboard)
        return
    if point.text[0] == "/":
        await app.send_message(
                chat_id=name,
                text="Commands not allow 🥲 ",reply_markup=keyboard)
        return
    test = point.text
    await app.send_sticker(name,"CAACAgIAAxkBAAEGRuJia9yE2U6lvvQbZ2qk5E-dXL2n4wACSAIAAladvQoc9XL43CkU0B4E",reply_markup=keyboard)
    await app.send_message(
                chat_id=name,
                text="Done! reported to admins sucsessfull✅",reply_markup=keyboard)
    await m.delete() 
    await app.send_message(
                chat_id=ADMIN,
                text=(
                    f"Hello sir, I am {nam} I have some problem\n"
                    f"❓ problem : **{point.text}**\n"
                ),reply_markup=InlineKeyboardMarkup(
                [[
                        InlineKeyboardButton(
                            text="💬 Reply to him", url=f"https://t.me/{BOT_USERNAME}?start=contact_{names}_{test}")
                ]]
            ))


@app.on_message(filters.private & filters.regex(pattern="« Back"))
async def refferal(_, message: Message):
    name = message.from_user.id
    await app.send_message(
                chat_id=name,
                text="🔙 You have returned to the main menu",reply_markup=keyboard)
    

@app.on_message(filters.private & filters.regex(pattern="👤 My Account"))
async def balance(_, message: Message):
    try:
       await message._client.get_chat_member(int(CHANNEL_ID), message.from_user.id)
       link = await app.create_chat_invite_link(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID))
   
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}
❗️ You Must Join This Channel First !
""",
     reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("🚀 Join Now  ", url=f"{link}"),
                 ],
             ]
            ))
       return
    name = message.from_user.id
    balance = userdb.find({'username': name})
    for data in balance:
        blan = data['wallet']
        dat = data['date']
    await message.reply_text(f"""
👤 **User ID**: {name}
🙃 **Name** : {message.from_user.mention}
📮 **Registry Date**: {dat}
💰 **Balance**: {blan} $

⏱ This status report was taken on : {date}""")


@app.on_message(filters.private & filters.regex(pattern="💎Get Accounts💎"))
async def withdraw(_, message: Message):
    name = message.from_user.id
    names = message.from_user.id
    balance = userdb.find({'username': name})
    for data in balance:
        blan = data['wallet']
        if blan < int(10):
          await app.send_message(name,f"Your balance is insufficient to get accounts\n💰 Balance:{blan}")
		
				
          return
    await app.send_message(
                chat_id=name,
                text="Done! ✅",reply_markup=keyboard)
    await app.send_message(
                chat_id=ADMIN,
                text=(
                    f"Hello sir, I am {name} I Need account \n"
                ),reply_markup=InlineKeyboardMarkup(
                [[
                        InlineKeyboardButton(
                            text="🤑Pay Now", url=f"https://t.me/{BOT_USERNAME}?start=contact_{names}")
                ]]
            ))
    try:
        data = userdb.find({'username': name})
        for d in data:
         b = d['wallet']
        td = int(10)  
        userdb.update_one({"username": name}, {"$set": {"wallet": b - td}})

    except:
        await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))       

    await app.send_message(
                chat_id= LOGS,
                text=(
                    f"🌎 ** New  account Requested **\n\n"
                    f"🆔 **User id**: {message.from_user.mention}\n\n"
                    f"💰 **Amount **: 10 coin\n\n"
                    f"[❗️ ADD](https://t.me/EpicPaymentProof/2) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)        
                    


@app.on_message(filters.private & filters.regex(pattern="/about"))
async def about(_, message: Message):
    try:
       await message._client.get_chat_member(int(CHANNEL_ID), message.from_user.id)
       link = await app.create_chat_invite_link(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID))
   
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}
❗️ You Must Join This Channel First !
""",
     reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("🚀 Join Now  ", url=f"{link}"),
                 ],
             ]
            ))
       return       
    name = message.from_user.id
    await app.send_sticker(name,"CAACAgIAAxkBAAEGRAdia1DbQywH8Bki72cFdHfW6MIemwACjgADFkJrCr6khn1tfi1cHgQ",reply_markup=keyboard)
    await message.reply_text(ABOUT_TEXT, reply_markup=comman
,disable_web_page_preview=True)

@app.on_message(filters.private & filters.regex(pattern="💳sponsorship"))
async def about(_, message: Message):
    try:
       await message._client.get_chat_member(int(CHANNEL_ID), message.from_user.id)
       link = await app.create_chat_invite_link(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID))
   
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}
❗️ You Must Join This Channel First !
""",
     reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("🚀 Join Now  ", url=f"{link}"),
                 ],
             ]
            ))
       return     
    name = message.from_user.id
    await message.reply_text(SPON_TEXT, reply_markup=keyboard
,disable_web_page_preview=True)

@app.on_message(filters.private & filters.regex(pattern="/help"))
async def support(_, message: Message):
    try:
       await message._client.get_chat_member(int(CHANNEL_ID), message.from_user.id)
       link = await app.create_chat_invite_link(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID))
   
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}
❗️ You Must Join This Channel First !
""",
     reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("🚀 Join Now  ", url=f"{link}"),
                 ],
             ]
            ))
       return    
    name = message.from_user.id
    await app.send_sticker(name,"CAACAgIAAxkBAAEGRApia1D_syYa7NQlMTNcJlbPwn_MuAACkQADFkJrCkATS0FTbcBkHgQ",reply_markup=keyboard)
    await message.reply_text(HELP_TEXT,disable_web_page_preview=True,reply_markup=comman)


@app.on_message(filters.private & filters.regex(pattern="📊 Statistics"))
async def accounts(_, message: Message):
    try:
       await message._client.get_chat_member(int(CHANNEL_ID), message.from_user.id)
       link = await app.create_chat_invite_link(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID))
   
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}
❗️ You Must Join This Channel First !
""",
     reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton("🚀 Join Now  ", url=f"{link}"),
                 ],
             ]
            ))
       return     
    name = message.from_user.id
    await app.send_sticker(name,"CAACAgEAAxkBAAEGRlhia6VbRZX4DZ36TIT0CP6BgugBsAAC7gMAAv5DwUe0nbeQnSoavB4E",reply_markup=keyboard)    
  
    countma = await app.get_chat_members_count(-1001620454933)
    countm = await app.get_chat_members_count(-1001717898230)
    counts = await app.get_chat_members_count(-1001567102066)
    u_count = userdb.find({})
    count = 0
    for stat in u_count:
            count = count + 1

    await message.reply_text(f"""
**Bot Advanced Statistics 📊**

** 👥Members Counts in Our channels:**

✪ Epic Bots: `{countma}`
✪ Mafia Proof :`{countm}`
✪ Epic chats :`{counts}`

** 🗃Storage usage:**

👥** Total amount of users**: `{count}`

🌀<u>**Last Update**</u> : {date}
""")


@app.on_message(filters.private & filters.command("bcast") & filters.user(ADMIN) & filters.reply)
async def broadcast_message(_, message):
    sleep_time = 0.1
    text = message.reply_to_message.text.markdown
    sent = 0
    chats = userdb.find({})
    m = await message.reply_text(
        f"Broadcast in progress"
    )
    for chat in chats:
        try:
            await app.send_message(chat['username'], text=text,disable_web_page_preview=True)
            await asyncio.sleep(sleep_time)
            sent += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await m.edit(f"**Broadcasted Message In {sent} Chats.**")


app.run()
