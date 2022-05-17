""" Admittedly, there is something to be said first. Do not waste your time editing this. You need to create this database.
If you want to make one like this, contact me with your price."""

from time import sleep
import datetime 
import asyncio
import uvloop
from config import *
import pymongo
import re
import random
import traceback
from aiohttp import ClientSession
from pyrogram import filters, Client, idle
from pyrogram.types import ForceReply,CallbackQuery,InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant,FloodWait,PeerIdInvalid
from db.db import udB
import pyromod.listen
import pytz

Time_Zone = "Asia/Kolkata"
zone = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))  
timer = zone.strftime("%I:%M %p")
dater = zone.strftime("%b %d")  
date = f"2022 {dater}:{timer}"


def list_in_shudder():
    return udB.get_key("shudder") or {}

def list_in_callofduty():
    return udB.get_key("callofduty") or {}

def list_in_zee5():
    return udB.get_key("zee5") or {}

def list_in_zoom():
    return udB.get_key("zoom") or {}

def list_in_heroku():
    return udB.get_key("heroku") or {}

def list_in_pinterest():
    return udB.get_key("pinterest") or {}

def list_in_duolingo():
    return udB.get_key("duolingo") or {}

def list_in_picsart():
    return udB.get_key("picsart") or {}

def list_in_deezer():
    return udB.get_key("deezer") or {}

def list_in_virtualDj():
    return udB.get_key("virtualDj") or {}

def list_in_canva():
    return udB.get_key("canva") or {}


loop = asyncio.get_event_loop()
aiohttpsession = ClientSession()
client = pymongo.MongoClient(DATABASE)

acc = client["ACC"]
db = client["bot"]
userdb = db["user"]

app = Client("giveaway",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN,)

app.start()
x = app.get_me()
BOT_USERNAME = x.username
ADMIN = 5053761519

@app.on_message(filters.command("deezer") & ~filters.group & filters.user(Deezer))
async def start(_, message: Message):
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("deezer")
    okh = list_in_deezer()
    okhg = okh[("deezer")]
    okhg.append(text)
    user = 'deezer'
    reason = okhg
    ok = list_in_deezer()
    ok.update({user: reason})
    udB.set_key("deezer", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"Deezer account added ..😺")

@app.on_message(filters.command("canva") & ~filters.group & filters.user(Canva))
async def start(_, message: Message):
    name = ADMIN
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("canva")
    okh = list_in_canva()
    okhg = okh[("canva")]
    okhg.append(text)
    user = 'canva'
    reason = okhg
    ok = list_in_canva()
    ok.update({user: reason})
    udB.set_key("canva", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"canva account added ..😺")



@app.on_message(filters.command("virtualDj") & ~filters.group & filters.user(VirtualDj))
async def start(_, message: Message):
    name = ADMIN
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("virtualDj")
    okh = list_in_virtualDj()
    okhg = okh[("virtualDj")]
    okhg.append(text)  
    user = 'virtualDj'
    reason = okhg
    ok = list_in_virtualDj()
    ok.update({user: reason})
    udB.set_key("virtualDj", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"VirtualDj account added ..😺")


@app.on_message(filters.command("picsart") & ~filters.group& filters.user(Picsart))
async def start(_, message: Message):
    name = ADMIN
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("picsart")
    okh = list_in_picsart()
    okhg = okh[("picsart")]
    okhg.append(text)  
    user = 'picsart'
    reason = okhg
    ok = list_in_picsart()
    ok.update({user: reason})
    udB.set_key("picsart", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"Picsart account added ..😺")


@app.on_message(filters.command("duolingo") & ~filters.group & filters.user(Duolingo))
async def start(_, message: Message):
    name = ADMIN
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("duolingo")
    okh = list_in_duolingo()
    okhg = okh[("duolingo")]
    okhg.append(text)   
    user = 'duolingo'
    reason = okhg
    ok = list_in_duolingo()
    ok.update({user: reason})
    udB.set_key("duolingo", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"Duolingo account added ..😺")

@app.on_message(filters.command("pinterest") & ~filters.group & filters.user(Pinterest))
async def start(_, message: Message):
    name = ADMIN
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("pinterest")
    okh = list_in_pinterest()
    okhg = okh[("pinterest")]
    okhg.append(text) 
    user = 'pinterest'
    reason = okhg
    ok = list_in_pinterest()
    ok.update({user: reason})
    udB.set_key("pinterest", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"pinterest account added ..😺")

@app.on_message(filters.command("heroku") & ~filters.group & filters.user(Heroku))
async def start(_, message: Message):
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("heroku")
    okh = list_in_heroku()
    okhg = okh[("heroku")]
    okhg.append(text)
    user = 'heroku'
    reason = okhg
    ok = list_in_heroku()
    ok.update({user: reason})
    udB.set_key("heroku", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"heroku account added ..😺")


@app.on_message(filters.command("zoom") & ~filters.group & filters.user(Zoom))
async def start(_, message: Message):
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("zoom")
    okh = list_in_zoom()
    okhg = okh[("zoom")]
    okhg.append(text)
    user = 'zoom'
    reason = okhg
    ok = list_in_heroku()
    ok.update({user: reason})
    udB.set_key("zoom", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"zoom account added ..😺")

@app.on_message(filters.command("zee5") & ~filters.group& filters.user(Zee5))
async def start(_, message: Message):
    name = ADMIN
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("zee5")
    okh = list_in_zee5()
    okhg = okh[("zee5")]
    okhg.append(text) 
    user = 'zee5'
    reason = okhg
    ok = list_in_heroku()
    ok.update({user: reason})
    udB.set_key("zee5", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"zee5 account added ..😺")

@app.on_message(filters.command("cod") & ~filters.group & filters.user(callofduty))
async def start(_, message: Message):
    name = ADMIN
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("callofduty")
    okh = list_in_callofduty()
    okhg = okh[("callofduty")]
    okhg.append(text)
    user = 'callofduty'
    reason = okhg
    ok = list_in_heroku()
    ok.update({user: reason})
    udB.set_key("callofduty", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"callofduty account added ..😺")


@app.on_message(filters.command("shudder") & ~filters.group & filters.user(Shudder))
async def start(_, message: Message):
    name = ADMIN
    text = (message.text.split(None, 1)[1]).lower()
    print(text)   
    okg = udB.get_key("shudder")
    okh = list_in_shudder()
    okhg = okh[("shudder")]
    okhg.append(text)    
    user = 'shudder'
    reason = okhg
    ok = list_in_shudder()
    ok.update({user: reason})
    udB.set_key("shudder", ok)
    await app.send_message(chat_id=message.from_user.id, text=f"Shudder account added ..😺")
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
                    f"🍃 **Bot** : [@{BOT_USERNAME}](https://t.me/{BOT_USERNAME}?start=1467358214)\n\n"
                    f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)
    await x.delete() 
    await app.send_sticker(chat_id,"CAACAgEAAxkBAAEGVaVibOE9cIWB7CtNX4kdJnH9_M9M8wAC6wcAAuN4BAABnwXByysQy_ceBA",reply_markup=keyboard)
    await app.send_message(
                chat_id=chat_id,
                text=(
                    f"💬 Hello sir this your {acc} Account \n\n"
                    f"📧 **Email** : `{point.text}`\n"
                    f"🔐 **Password** :`{sems.text}`\n\n"
                    f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
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
					await app.send_sticker(user_id, "CAACAgIAAxkBAAEGVFxibK3z1mlw0_dMI71IZRt8-6lY6wAC-QEAAhZCawp25-ZIrBxpvR4E")
					await app.send_message(chat_id=user_id, text=f"Already started ..😿")
					return
				if supun == None:
					await app.send_sticker(user_id, random.choice(STICKER), reply_markup=keyboard)
					await message.reply_text(START_TEXT.format(umention), disable_web_page_preview=True, reply_markup=comman)
					await app.send_message(chat_id=user_id, text=f"🎖 **You were invited by user** : {name}")
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
	

@app.on_message(filters.private & filters.regex(pattern="📢 Channels"))
async def refferal(_, message: Message):
    name = message.from_user.id
    await app.send_sticker(name,random.choice(STICKER),reply_markup=keyboard)
    try:
       await message._client.get_chat_member(-1001797172159, message.from_user.id)
       await message._client.get_chat_member(-1001518620432, message.from_user.id)
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
       await message._client.get_chat_member(-1001787361488, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
**🔥Join all of channel bellow to get more giveaways **""",
			reply_markup=fsubbutton)
       return
    await app.send_message(name,f"🙃 You have already Joined.")

            
@app.on_message(filters.private & filters.regex(pattern="👥 Referral"))
async def refferal(_, message: Message):
    name = message.from_user.id
    await app.send_sticker(name,random.choice(STICKER),reply_markup=keyboard)
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}

❗️ You Must Join This Channel First !

@szteambots
""")
       return
    url = f"https://t.me/{BOT_USERNAME}?start={name}"
    await app.send_photo(name,
      "https://telegra.ph/file/77a8798d0dbb97c472455.jpg",
      caption = f"""
✅ **Premium Accounts BOT**

❤️ Premium Accounts.
👥 Normal Accounts.
🔐 Safe and secure payment.

🔗{url} """)
    sleep(2.0)
    await app.send_message(chat_id=name, text=REF.format(name))

@app.on_message(filters.private & filters.regex(pattern="☎️ Support"))
async def refferal(_, message: Message):
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


@app.on_message(filters.private & filters.regex(pattern="«Back"))
async def refferal(_, message: Message):
    name = message.from_user.id
    await app.send_message(
                chat_id=name,
                text="🔙 You have returned to the main menu",reply_markup=keyboard)
    

@app.on_message(filters.private & filters.regex(pattern="👤 My Account"))
async def balance(_, message: Message):
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}

❗️ You Must Join This Channel First !

@szteambots
""")
       return
    name = message.from_user.id
    balance = userdb.find({'username': name})
    for data in balance:
        blan = data['wallet']
        dat = data['date']
    await message.reply_text(f"""
👤 **User ID**: {name}
👉 **Name** : {message.from_user.mention}
👉 **Registry Date**: {dat}
💰 **Balance**: {blan} $

⏱ This status report was taken on : {date}""")


@app.on_message(filters.private & filters.regex(pattern="💎Get Accounts💎"))
async def withdraw(_, message: Message):
    name = message.from_user.id
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}

❗️ You Must Join This Channel First !

@szteambots
""")
       return    
    await app.send_sticker(name,random.choice(STICKER),reply_markup=keyboard)
    await message.reply_text(f"""
💰 **Select Your Price From Bellow Buttons**
""", reply_markup=accountf
,disable_web_page_preview=True)


@app.on_message(filters.private & filters.regex(pattern="/about"))
async def about(_, message: Message):
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}

❗️ You Must Join This Channel First !

@szteambots
""")
       return      
    name = message.from_user.id
    await app.send_sticker(name,"CAACAgIAAxkBAAEGRAdia1DbQywH8Bki72cFdHfW6MIemwACjgADFkJrCr6khn1tfi1cHgQ",reply_markup=keyboard)
    await message.reply_text(ABOUT_TEXT, reply_markup=comman
,disable_web_page_preview=True)

@app.on_message(filters.private & filters.regex(pattern="💳sponsorship"))
async def about(_, message: Message):
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}

❗️ You Must Join This Channel First !

@szteambots
""")
       return      
    name = message.from_user.id
    await message.reply_text(SPON_TEXT, reply_markup=keyboard
,disable_web_page_preview=True)

@app.on_message(filters.private & filters.regex(pattern="/help"))
async def support(_, message: Message):
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}

❗️ You Must Join This Channel First !

@szteambots
""")
       return      
    name = message.from_user.id
    await app.send_sticker(name,"CAACAgIAAxkBAAEGRApia1D_syYa7NQlMTNcJlbPwn_MuAACkQADFkJrCkATS0FTbcBkHgQ",reply_markup=keyboard)
    await message.reply_text(HELP_TEXT,disable_web_page_preview=True,reply_markup=comman)


@app.on_message(filters.private & filters.regex(pattern="📊 Statistics"))
async def accounts(_, message: Message):
    try:
       await message._client.get_chat_member(-1001325914694, message.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=message.from_user.id,
			text=f"""
⚠️ **Access Denied** {message.from_user.mention}

❗️ You Must Join This Channel First !

@szteambots
""")
       return      
    name = message.from_user.id
    await app.send_sticker(name,"CAACAgEAAxkBAAEGRlhia6VbRZX4DZ36TIT0CP6BgugBsAAC7gMAAv5DwUe0nbeQnSoavB4E",reply_markup=keyboard)    
  
    countma = await app.get_chat_members_count(-1001797172159)
    countm = await app.get_chat_members_count(-1001518620432)
    counts = await app.get_chat_members_count(-1001325914694)

    u_count = userdb.find({})
    count = 0
    for stat in u_count:
            count = count + 1

    acc1 = list_in_heroku()
    sz1 = acc1[("heroku")]
    herokuaccs = len(sz1)

    acc2 = list_in_zoom()
    sz2 = acc2[("zoom")]
    zoomaccs = len(sz2)

    acc3 = list_in_shudder()
    sz3 = acc3[("shudder")]
    shudeeraccs = len(sz3)

    acc4 = list_in_callofduty()
    sz4 = acc4[("callofduty")]
    callofdutyaccs = len(sz4)

    acc5 = list_in_zee5()
    sz5 = acc5[("zee5")]
    zee5accs = len(sz5)

    acc6 = list_in_pinterest()
    sz6 = acc6[("pinterest")]
    pinterestaccs = len(sz6)

    acc7 = list_in_duolingo()
    sz7 = acc7[("duolingo")]
    Duolingoaccs = len(sz7)

    acc8 = list_in_picsart()
    sz8 = acc8[("picsart")]
    Picsartaccs = len(sz8)

    acc9 = list_in_deezer()
    sz9 = acc9[("deezer")]
    Deezeraccs = len(sz9)

    acc10 = list_in_virtualDj()
    sz10 = acc10[("virtualDj")]
    VirtualDjaccs = len(sz10)

    acc11 = list_in_canva()
    sz11 = acc11[("canva")]
    canvaaccs = len(sz11)

    await message.reply_text(f"""
**Bot Advanced Statistics 📊**

** 👥Members Counts in Our channels:**

✪ Mafi Official : `{countma}`
✪ Mafia Proof :`{countm}`
✪ Developer Main :`{counts}`

** 🗃Storage usage:**

✪ Heroku Accounts :`{herokuaccs}`
✪ Zoom  Accounts : `{zoomaccs}`
✪ Deezer Accounts : `{Deezeraccs}`
✪ VirtualDj Accounts : `{VirtualDjaccs}`
✪ Picsart Accounts : `{Picsartaccs}`
✪ Duolingo Accounts : `{Duolingoaccs}`
✪ Shudder Accounts : `{shudeeraccs}`

👥** Total amount of users**: `{count}`

🌀<u>**Last Update**</u> : {date}
""")

@app.on_message(filters.private & filters.command("bcast") & filters.user(1467358214) & filters.reply)
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


@app.on_message(filters.command("freecoin") & filters.user(ADMIN))
async def broadcastcoin(_, message):
    m = await message.reply_text("`sending...`")
    success = 0
    failed = 0
    chats = userdb.find({})
    for chat in chats:
      try:
        await app.send_message(chat['username'],"""Admin bonus is waiting for you. Get it now:""",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🎁", callback_data="free$")
                ]
            ]
        ))
        success += 1
      except FloodWait as flood:
          await sleep(flood.x)
      except:
        failed += 1
        pass
    await m.delete()
    await message.reply_text(f"""
Success  - {success} 
Failed - {failed}
""") 


@app.on_callback_query()
async def button(bot: Client, cmd: CallbackQuery):
    name = cmd.from_user.id
    cb_data = cmd.data
    if "coin2" in cb_data:
        await cmd.message.delete()
        await app.send_message(cmd.message.chat.id,text=f"""
🔥**Select Your Accounts From Bellow Buttons**
""", reply_markup=account
,disable_web_page_preview=True)

    if "5coin" in cb_data:
        await cmd.message.delete()
        await app.send_message(cmd.message.chat.id,text=f"""
🔥**Select Your Accounts From Bellow Buttons**
""", reply_markup=account1
,disable_web_page_preview=True)

    if "10coins" in cb_data:
        await cmd.message.delete()
        await app.send_message(cmd.message.chat.id,text=f"""
🔥**Select Your Accounts From Bellow Buttons**
""", reply_markup=account2
,disable_web_page_preview=True)

    if "closed" in cb_data:
        await cmd.message.delete()
    if "backs" in cb_data:
        await cmd.message.delete()
        await app.send_message(cmd.message.chat.id,text=f"""
💰 **Select Your Price From Bellow Buttons**
""", reply_markup=accountf
,disable_web_page_preview=True)
    if "free$" in cb_data:
      await cmd.message.delete()
      await app.send_message(cmd.message.chat.id, "🎁 You got: 1coin")
      try:
            data = userdb.find({'username': name})
            for d in data:
                b = d['wallet']
            td = int(1)    
            userdb.update_one({"username": name}, {"$set": {"wallet": b+td}})
      except:
            await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))
    
    if "aboutme" in cb_data:
      await cmd.message.delete()
      await app.send_message(cmd.message.chat.id,text=ABOUT_TEXT, reply_markup=comman
,disable_web_page_preview=True)

    if "help" in cb_data:
      await cmd.message.delete()  
      await app.send_message(cmd.message.chat.id,text=HELP_TEXT,disable_web_page_preview=True,reply_markup=comman)

    if "giveme" in cb_data:
      print(cb_data)
      accs = cb_data.split("#")[1] 
      print(accs) 
      balance = userdb.find({'username': name})
      for data in balance:
        blan = data['wallet']
        if blan < int(2):
          await cmd.answer(f"⚠️ Your balance is insufficient to get {accs} account\n💰 Balance:{blan}", show_alert=True)
          return
        try:
            okg = udB.get_key(accs)
            list = okg[(accs)]

            print(okg)
            print(list)

            agg = random.choice(list)

            us = re.split(':',agg)[0]

            ps = re.split(':',agg)[1]

            print(us)
            print(ps)
            print(agg)

            if agg in list:

                list.remove(agg)

                user = accs
                reason = list
                ok = list_in_shudder()
                ok.update({user: reason})
                udB.set_key(accs, ok)
        
            else:
                print("This student does not appear in your list.")

            await app.send_message(
                    chat_id=cmd.from_user.id,
                    text=(
                        f"💬 Hello sir this your {accs} Account \n\n"
                        f"📧 **Email** : `{us}`\n"
                        f"🔐 **Password** :`{ps}`\n\n"
                        f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                    ),disable_web_page_preview=True)
            try:
                data = userdb.find({'username': name})
                for d in data:
                 b = d['wallet']
                td = int(2)    
                userdb.update_one({"username": name}, {"$set": {"wallet": b-td}})
            except:
                await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))  
            if name ==int(1467358214):
                return
            await app.send_message(
                chat_id=-1001518620432,
                text=(
                    f"✅ ** New Withdraw Paid**\n\n"
                    f"🆔 **User id**: {cmd.from_user.mention}\n\n"
                    f"💰 **Amount **: 2 coin\n\n"
                    f"📦 **Account type**:{accs}\n\n"
                    f"🍃 **Bot** : [@{BOT_USERNAME}](https://t.me/{BOT_USERNAME}?start=1467358214)\n\n"
                    f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)        
            
            await cmd.answer("✅ Your withdrawal has been done!", show_alert=True) 
            

        except IndexError:
 
            print("admin add data")

            await cmd.answer("❗️ I do not have enough data in my account at the moment I informed the Admin.  He will give you your account soon.", show_alert=True)

            await app.send_message(chat_id=ADMIN, text=f"⚠️ Admin need Add **{accs}** Accounts to db 💢\n")

            await app.send_message(
				chat_id=ADMIN,
				text=(
					f"Admin need **{accs}** Account\n"
					f"💰 **price** : 2 coin\n"
					f"📦 **Account Type**: {accs}\n"
					f"🍃 **User mention** : {cmd.from_user.mention}\n"
					f"🆔 **User Id** : `{cmd.from_user.id}`\n"
				),reply_markup=InlineKeyboardMarkup(
				[[
						InlineKeyboardButton(f"Provide his/her {accs} Account", url=f"https://t.me/{BOT_USERNAME}?start=acc_{cmd.from_user.id}_{accs}")
				]]
			))  
    if "fuckyou" in cb_data:
      print(cb_data)
      accs = cb_data.split("#")[1] 
      print(accs) 
      balance = userdb.find({'username': name})
      for data in balance:
        blan = data['wallet']
        if blan < int(5):
          await cmd.answer(f"⚠️ Your balance is insufficient to get {accs} account\n💰 Balance:{blan}", show_alert=True)
          return
        try:
            okg = udB.get_key(accs)
            list = okg[(accs)]

            print(okg)
            print(list)

            agg = random.choice(list)

            us = re.split(':',agg)[0]

            ps = re.split(':',agg)[1]

            print(us)
            print(ps)
            print(agg)

            if agg in list:

                list.remove(agg)

                user = accs
                reason = list
                ok = list_in_shudder()
                ok.update({user: reason})
                udB.set_key(accs, ok)
        
            else:
                print("This student does not appear in your list.")

            await app.send_message(
                    chat_id=cmd.from_user.id,
                    text=(
                        f"💬 Hello sir this your {accs} Account \n\n"
                        f"📧 **Email** : `{us}`\n"
                        f"🔐 **Password** :`{ps}`\n\n"
                        f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                    ),disable_web_page_preview=True)
            try:
                data = userdb.find({'username': name})
                for d in data:
                 b = d['wallet']
                td = int(5)    
                userdb.update_one({"username": name}, {"$set": {"wallet": b-td}})
            except:
                await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))  
            if name ==int(1467358214):
                return
            await app.send_message(
                chat_id=-1001518620432,
                text=(
                    f"✅ ** New Withdraw Paid**\n\n"
                    f"🆔 **User id**: {cmd.from_user.mention}\n\n"
                    f"💰 **Amount **: 5 coin\n\n"
                    f"📦 **Account type**:{accs}\n\n"
                    f"🍃 **Bot** : [@{BOT_USERNAME}](https://t.me/{BOT_USERNAME}?start=1467358214)\n\n"
                    f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)        
            
            await cmd.answer("✅ Your withdrawal has been done!", show_alert=True) 
            

        except IndexError:
 
            print("admin add data")

            await cmd.answer("❗️ I do not have enough data in my account at the moment I informed the Admin.  He will give you your account soon.", show_alert=True)

            await app.send_message(chat_id=ADMIN, text=f"⚠️ Admin need Add **{accs}** Accounts to db 💢\n")

            await app.send_message(
				chat_id=ADMIN,
				text=(
					f"Admin need **{accs}** Account\n"
					f"💰 **price** : 5 coin\n"
					f"📦 **Account Type**: {accs}\n"
					f"🍃 **User mention** : {cmd.from_user.mention}\n"
					f"🆔 **User Id** : `{cmd.from_user.id}`\n"
				),reply_markup=InlineKeyboardMarkup(
				[[
						InlineKeyboardButton(f"Provide his/her {accs} Account", url=f"https://t.me/{BOT_USERNAME}?start=acc_{cmd.from_user.id}_{accs}")
				]]
			))  
    if "sexyou" in cb_data:
      print(cb_data)
      accs = cb_data.split("#")[1] 
      print(accs) 
      balance = userdb.find({'username': name})
      for data in balance:
        blan = data['wallet']
        if blan < int(10):
          await cmd.answer(f"⚠️ Your balance is insufficient to get {accs} account\n💰 Balance:{blan}", show_alert=True)
          return
        try:
            okg = udB.get_key(accs)
            list = okg[(accs)]

            print(okg)
            print(list)

            agg = random.choice(list)

            us = re.split(':',agg)[0]

            ps = re.split(':',agg)[1]

            print(us)
            print(ps)
            print(agg)

            if agg in list:

                list.remove(agg)

                user = accs
                reason = list
                ok = list_in_shudder()
                ok.update({user: reason})
                udB.set_key(accs, ok)
        
            else:
                print("This student does not appear in your list.")

            await app.send_message(
                    chat_id=cmd.from_user.id,
                    text=(
                        f"💬 Hello sir this your {accs} Account \n\n"
                        f"📧 **Email** : `{us}`\n"
                        f"🔐 **Password** :`{ps}`\n\n"
                        f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                    ),disable_web_page_preview=True)
            try:
                data = userdb.find({'username': name})
                for d in data:
                 b = d['wallet']
                td = int(10)    
                userdb.update_one({"username": name}, {"$set": {"wallet": b-td}})
            except:
                await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))  
            if name ==int(1467358214):
                return
            await app.send_message(
                chat_id=-1001518620432,
                text=(
                    f"✅ ** New Withdraw Paid**\n\n"
                    f"🆔 **User id**: {cmd.from_user.mention}\n\n"
                    f"💰 **Amount **: 10 coin\n\n"
                    f"📦 **Account type**:{accs}\n\n"
                    f"🍃 **Bot** : [@{BOT_USERNAME}](https://t.me/{BOT_USERNAME}?start=1467358214)\n\n"
                    f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)        
            
            await cmd.answer("✅ Your withdrawal has been done!", show_alert=True) 
            

        except IndexError:
 
            print("admin add data")

            await cmd.answer("❗️ I do not have enough data in my account at the moment I informed the Admin.  He will give you your account soon.", show_alert=True)

            await app.send_message(chat_id=ADMIN, text=f"⚠️ Admin need Add **{accs}** Accounts to db 💢\n")

            await app.send_message(
				chat_id=ADMIN,
				text=(
					f"Admin need **{accs}** Account\n"
					f"💰 **price** : 10 coin\n"
					f"📦 **Account Type**: {accs}\n"
					f"🍃 **User mention** : {cmd.from_user.mention}\n"
					f"🆔 **User Id** : `{cmd.from_user.id}`\n"
				),reply_markup=InlineKeyboardMarkup(
				[[
						InlineKeyboardButton(f"Provide his/her {accs} Account", url=f"https://t.me/{BOT_USERNAME}?start=acc_{cmd.from_user.id}_{accs}")
				]]
			))  
                           
    if "ccadded" in cb_data:
      print(cb_data)
      accs = cb_data.split("#")[1] 
      print(accs) 
      balance = userdb.find({'username': name})
      for data in balance:
        blan = data['wallet']
        if blan < int(100):
          await cmd.answer(f"⚠️ Your balance is insufficient to get {accs} account\n", show_alert=True)
          return
        try:
            okg = udB.get_key(accs)
            list = okg[(accs)]

            print(okg)
            print(list)

            agg = random.choice(list)

            us = re.split(':',agg)[0]

            ps = re.split(':',agg)[1]

            print(us)
            print(ps)
            print(agg)

            if agg in list:

                list.remove(agg)

                user = accs
                reason = list
                ok = list_in_shudder()
                ok.update({user: reason})
                udB.set_key(accs, ok)
        
            else:
                print("This student does not appear in your list.")

            await app.send_message(
                    chat_id=cmd.from_user.id,
                    text=(
                        f"💬 Hello sir this your {accs} Account \n\n"
                        f"📧 **Email** : `{us}`\n"
                        f"🔐 **Password** :`{ps}`\n\n"
                        f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                    ),disable_web_page_preview=True)
            try:
                data = userdb.find({'username': name})
                for d in data:
                 b = d['wallet']
                td = int(100)    
                userdb.update_one({"username": name}, {"$set": {"wallet": b-td}})
            except:
                await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))  
            if name ==int(1467358214):
                return
            await app.send_message(
                chat_id=-1001518620432,
                text=(
                    f"✅ ** New Withdraw Paid**\n\n"
                    f"🆔 **User id**: {cmd.from_user.mention}\n\n"
                    f"💰 **Amount **: 100 coin\n\n"
                    f"📦 **Account type**:{accs}\n\n"
                    f"🍃 **Bot** : [@{BOT_USERNAME}](https://t.me/{BOT_USERNAME}?start=1467358214)\n\n"
                    f"[❗️ ADD](https://t.me/Mafiapayment/43) : {random.choice(ADDS)}"
                ),disable_web_page_preview=True)        
            
            await cmd.answer("✅ Your withdrawal has been done!", show_alert=True) 
            

        except IndexError:
 
            print("admin add data")

            await cmd.answer("❗️ I do not have enough data in my account at the moment I informed the Admin.  He will give you your account soon.", show_alert=True)

            await app.send_message(chat_id=ADMIN, text=f"⚠️ Admin need Add **{accs}** Accounts to db 💢\n")

            await app.send_message(
				chat_id=1467358214,
				text=(
					f"Admin need **{accs}** Account\n"
					f"💰 **price** : 100 coin\n"
					f"📦 **Account Type**: {accs}\n"
					f"🍃 **User mention** : {cmd.from_user.mention}\n"
					f"🆔 **User Id** : `{cmd.from_user.id}`\n"
				),reply_markup=InlineKeyboardMarkup(
				[[
						InlineKeyboardButton(f"Provide his/her {accs} Account", url=f"https://t.me/{BOT_USERNAME}?start=acc_{cmd.from_user.id}_{accs}")
				]]
			))  
    #no neeed this callback now
    """ if "refreshForceSub" in cb_data:
      try:
        await cmd._client.get_chat_member(-1001518620432, cmd.from_user.id)
        await cmd._client.get_chat_member(-1001797172159, cmd.from_user.id)
        await cmd._client.get_chat_member(-1001325914694, cmd.from_user.id)
        await cmd._client.get_chat_member(-1001787361488, cmd.from_user.id)
      except UserNotParticipant:
        await cmd.answer("😶Please join all channels", show_alert=True)
      else:
          try:
             data = userdb.find({'username': int(name)})
             if data == None:
                 return
             for d in data:
                 balance = d["wallet"]
                 fsubs = d["fsub"]
                 if fsubs == int(2):  
                   await cmd.answer("Already get your  Free Credit 😶", show_alert=True)
                   await cmd.message.delete()
                   return       
                 await cmd.answer("🔥Done , You got: 4 coin", show_alert=True)
                 userdb.update_one({"username": int(name)}, {
							"$set": {"fsub": int(fsubs)+2}}) 
                 userdb.update_one({"username": int(name)}, {
							"$set": {"wallet": int(balance)+4}})           
                 await cmd.message.delete()
                 return
          except Exception as e:
                return await app.send_message(ADMIN,text= f"{e}") """


    if "about" in cb_data:
        try:
            await cmd.answer(f"» Your id :{cmd.from_user.id}\n» First Name:{cmd.from_user.first_name}\n» Your DC:{cmd.from_user.dc_id}\n", show_alert=True)     
        except PeerIdInvalid:
          await cmd.answer("I don't know you.🤔", show_alert=True)  
          return

@app.on_message(filters.private & filters.regex(pattern="💸 Transfer"))
async def refferal(_, message: Message):
    name = message.from_user.id
    balance = userdb.find({'username': name})
    for data in balance:
        blan = data['wallet']
    m = await app.send_message(
                chat_id=name,
                text=TRANS.format(blan),reply_markup=back)
    iduser = await app.listen(name, filters=None, timeout=60)
    if blan < int(10):
          await app.send_message(chat_id=name,
                text=f"⚠️ This transfer cannot be done, it requires 10 $ to remain in your account.",reply_markup=keyboard)
          return
    await m.delete()        
    if iduser.text[0] == "«":
        await app.send_message(
                chat_id=name,
                text="🔙 You have returned to the main menu",reply_markup=keyboard)
        return
    if iduser.text[0] == "/":
        await app.send_message(
                chat_id=name,
                text="Commands not allow 🥲 ",reply_markup=keyboard)
        return
    user_id = int(iduser.text)   
    userbn = userdb.find_one({'username':user_id})
    if userbn == None: 
        await app.send_message(chat_id=name,
        text="⚠️ User not found in the bot user list!",reply_markup=keyboard)    
        return 
    x = await app.send_message(
                chat_id=name,
                text=TRANSC.format(blan),reply_markup=back)
    coin = await app.listen(name, filters=None, timeout=60)
    cash = coin.text
    if blan < int(cash):
          await app.send_message(chat_id=name,
          text=f"⚠️ Your balance isn't enough to transfer {cash}",reply_markup=keyboard)
          return
    await x.delete()
    try:
        data = userdb.find({'username': name})
        for d in data:
          b = d['wallet']
        td = int(cash)    
        userdb.update_one({"username": name}, {"$set": {"wallet": b-td}})
    except:
        await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))  
    try:
        data = userdb.find({'username': user_id})
        for d in data:
          b = d['wallet']
        td = int(cash)    
        userdb.update_one({"username": user_id}, {"$set": {"wallet": b+td}})
    except:
        await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))  
    balance = userdb.find({'username': user_id})
    for data in balance:
        bla = data['wallet']
    await app.send_message(chat_id=user_id,
    text=f"""💰**Received `{cash}` coin from** : {message.from_user.mention}""")    
    await app.send_message(chat_id=name,
    text=f"""
✅ **Successfully exchanged. The details are as follows.**

......................................
» User ID: `{user_id}`
» Amount: `{cash}`
» Total Balance: `{bla}` $
» Status: **Sent** ✅
......................................

⏱ This status report was taken on : `{date}`
  """,reply_markup=keyboard)


@app.on_message(filters.private & filters.regex(pattern="remove") & filters.user(1467358214) )# only for me (Personal use only)
async def refferal(_, message: Message):
    name = message.from_user.id
    balance = userdb.find({'username': name})
    for data in balance:
        blan = data['wallet']
    m = await app.send_message(
                chat_id=name,
                text=TRANS.format(blan),reply_markup=back)
    iduser = await app.listen(name, filters=None, timeout=60)
    if blan < int(10):
          await app.send_message(f"⚠️ This transfer cannot be done, it requires 10 $ to remain in your account.",reply_markup=keyboard)
          return
    await m.delete()        
    if iduser.text[0] == "«":
        await app.send_message(
                chat_id=name,
                text="🔙 You have returned to the main menu",reply_markup=keyboard)
        return
    if iduser.text[0] == "/":
        await app.send_message(
                chat_id=name,
                text="Commands not allow 🥲 ",reply_markup=keyboard)
        return
    user_id = int(iduser.text)   
    userbn = userdb.find_one({'username':user_id})
    if userbn == None: 
        await app.send_message(chat_id=name,
        text="⚠️ User not found in the bot user list!",reply_markup=keyboard)    
        return 
    x = await app.send_message(
                chat_id=name,
                text=TRANSC.format(blan),reply_markup=back)
    coin = await app.listen(name, filters=None, timeout=60)
    cash = coin.text
    if blan < int(cash):
          await app.send_message(chat_id=name,
          text=f"⚠️ Your balance isn't enough to transfer {cash}",reply_markup=keyboard)
          return
    await x.delete()
    try:
        data = userdb.find({'username': name})
        for d in data:
          b = d['wallet']
        td = int(cash)    
        userdb.update_one({"username": name}, {"$set": {"wallet": b+td}})
    except:
        await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))  
    try:
        data = userdb.find({'username': user_id})
        for d in data:
          b = d['wallet']
        td = int(cash)    
        userdb.update_one({"username": user_id}, {"$set": {"wallet": b-td}})
    except:
        await app.send_message(chat_id=ADMIN, text=str(traceback.format_exc()))  
    balance = userdb.find({'username': user_id})
    for data in balance:
        bla = data['wallet']
    await app.send_message(chat_id=name,
    text=f"""
✅ **Successfully exchanged. The details are as follows.**

......................................
» User ID: `{user_id}`
» Amount: `{cash}`
» Total Balance: `{bla}` $
» Status: **Sent** ✅
......................................

⏱ This status report was taken on : `{date}`
  """,reply_markup=keyboard)                 
    

async def start_bot():
    print("Bot Online Thank You")
    await idle()
    await aiohttpsession.close()
    await app.stop()
    for task in asyncio.all_tasks():
        task.cancel()
    print("Bot Down Time Started")


if __name__ == "__main__":
    uvloop.install()
    try:
        try:
            loop.run_until_complete(start_bot())
        except asyncio.exceptions.CancelledError:
            pass
        loop.run_until_complete(asyncio.sleep(2.0))  
    finally:
        loop.close()
