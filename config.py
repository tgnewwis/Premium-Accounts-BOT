from dotenv import load_dotenv
from os import environ
from pyrogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv("config.env")

BOT_OWNER = 1467358214
BOT_TOKEN = environ.get("BOT_TOKEN", None)
API_ID = int(environ.get("API_ID", 6))
API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
DATABASE = environ.get("DATABASE")
CHANNEL_ID = environ.get("CHANNEL_ID")
LOGS = environ.get("LOGS")

STICKER = ["CAACAgIAAxkBAAEGVApibIes8S62v5AkF1lrsIRygq5xFgACAwEAAladvQoC5dF4h-X6Tx4E",
          "CAACAgIAAxkBAAEGSA5ia93HXYEAAbRDWZlDQGOgseJme-0AAhQAAztgJBQpZ4ESAvfI6h4E",
          "CAACAgIAAxkBAAEGRGtia1jSjDF3Zf5AAYPtf9wVKx79ZgACJgADDbbSGRYpFH5xkFugHgQ",
          "CAACAgIAAxkBAAEGVA1ibIfxr212zltxemfdBkynBVDQEAACjAADFkJrCkKO_mIXPU3iHgQ",
          "CAACAgIAAxkBAAEGVBBibIgYp0OjOF9R58K6DPURLcCknwACYQADDbbSGblGkUk4wVCCHgQ",
          "CAACAgIAAxkBAAEGVBNibIg0nEYtMPGO2wFY2kVOb6BG2QACzgADUomRI77CfDbcY4sSHgQ",
          "CAACAgIAAxkBAAEGVBZibIhRLEJ_jdmIK3C9_9SS2BN2ogACbgEAAjDUnRFcrCcMWa4mkh4E",      
          "CAACAgIAAxkBAAEGVBlibIiXqQWM3-OpSYNqChBYvo6umAACYwIAAsoDBgvs7jNsYlkcax4E",
          "CAACAgIAAxkBAAEGVBxibIjj0Ns8yxO-tGxMXh1blB6BUAACVQMAArVx2gYTIpfj7IkJBx4E",
          "CAACAgIAAxkBAAEGatpicIMuyHYfz2SM_WRR4Y-CAjXdAgACYwIAAsoDBgvs7jNsYlkcax4E",
          "CAACAgIAAxkBAAEGat1icIOjLcwOwNQcK4vtCtX8GGI8iwACWwADKA9qFLdiRrnAirpAHgQ",
          "CAACAgIAAxkBAAEGauBicIPGz_eREGt-k_PB7kt9Le8AAbgAAioAA8GcYAwjxoukwOqqDB4E",
          "CAACAgIAAxkBAAEGauVicIQVEz6rR8gDLQ1XmW_Wv3OtagACKQADWbv8JWiEdiw7SWZ7HgQ",
          "CAACAgIAAxkBAAEGauhicIRKAAGF1tKkfwSmkM97mLtUonEAAqsAAztgJBS0UIDM90a6nR4E"
         ]     

ABOUT_TEXT = f"""
<u>**🙋‍♂️ About  menu of Epic Premium Accounts Bot**</u>

<u>🌀 **About BOT basic** </u>

🔹 This Bot Developed And Server Maintained By [wisula](https://t.me/aboutWisula)
If You Have Any Problem With Bot Code or Another things Contact Me(Don't Come DM for Accounts)

🔹 This BOT was made useing Pyrogram + Mongo Data base.


<u>📚 **About Premium Accounts** </u>

▪️ All Of Premium Accounts Provides From This BOT Was Provided By 
@wisula4 & @ImNavanjana If you have problem With  Accounts Contact Them or simply Use Support Button.

Thank You All Of User !."""

HELP_TEXT =f"""

📮<u>**Help menu of Epic Premium Accounts Bot**</u>

▪️ After you can see   Referral  banner , share it with your friends and get 1 $ per one new user.

💎<u>** How To Get Accounts **</u>

▪️ First click Get Accounts button and get panel of accounts available in this moment click buttons as your want.

⚠️ **You must earn minimum 10 $ to get 1 account**

✅ You can see your request post in proof channel and i will provide your account..."""

START_TEXT = """
📚<u> I am bot that can provide **Premium Accounts**
Share me and get account as you want...</u>

For more open Giveaway join with [Mafia](https://t.me/MafiaGiveaways) & join with [sz team](https://t.me/szteambots) for BOT updates."""

REF = """
Send the banner above to your friends or contacts and for every new member that joins bot by you, you will gain 1 $!

UserID:`{}`
"""

SUPORT = """
**🔰 Our partners are at your service**

💁 Send us your problem bellow.
📨 For direct communication » @EpicChats

⚠️ The support department tries to respond to all incoming messages in less than 12 hours, 
so be patient until you receive a response."""


keyboard =  ReplyKeyboardMarkup(
      [
        ['💎Get Accounts💎'],
        ['👤 My Account','📊 Statistics'],
        ['👥 Referral'],
        ['☎️ Support','💳sponsorship'],
      ],resize_keyboard=True
    )

back = ReplyKeyboardMarkup(
      [
        ['« Back'],
      ],resize_keyboard=True
    )

comman =InlineKeyboardMarkup(
					[
                    [
							InlineKeyboardButton(
								"👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=5246051676),
							InlineKeyboardButton(
								"💠 Github", url="https://github.com/wisula")
					],
                    [
							InlineKeyboardButton(
								"🔰 Help", callback_data="help"),
							InlineKeyboardButton(
								"🌀 About Me", callback_data="aboutme")
					],
                    [
                        InlineKeyboardButton("🔥About You ", callback_data="about")
                    ]
                    ])

SPON_TEXT = """
**With this tool you can sponsor Bot.**

❗️ ** Terms**
 » Cannot sponsor money.
 » You can give the bot the required accounts but the minimum should be 100+ and all working premium should be sent.

✅ **Things you get**

 » Free 1 Add Life- time via Bot.
 » Force - subscribe to your channel

👨‍💻 Contact :@wisula4
"""
