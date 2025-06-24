from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 6798960191

CARD_INFO = """🏦 بانک رفاه - یاسین ظهیری
💳 شماره کارت: 5894 6312 1169 8923
🔢 شبا: IR880130100000000366857307"""

WELCOME_TEXT = """📍 لوكيشن آلمان 🇩🇪

🔹 ١٠ گيگ - 259,000 تومان ✅  
🔹 ٢٠ گيگ - 459,000 تومان ✅  
🔹 ٣٠ گيگ - 659,000 تومان ✅

💎 اتصال با يك كليك در لحظه  
😍 قابليت باز كردن اينستاگرام، تلگرام، يوتيوب و ...

📢 کانال ما:
@faplazachannel

✨ شما لياقت بهترين‌ها و باكيفيت‌ترين‌هارو داريد ✨

👇 برای خرید VPN، دکمه زیر رو بزن:"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("💳 خرید VPN")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.effective_message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    user = update.effective_user

    if message.text == "💳 خرید VPN":
        await message.reply_text(f"لطفاً مبلغ را به شماره کارت زیر واریز کن و رسید را ارسال کن:

{CARD_INFO}")
    else:
        await message.reply_text("✅ رسید دریافت شد. لطفاً چند لحظه صبر کن.")
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🧾 رسید جدید از:
👤 {user.first_name} (@{user.username})
🆔 {user.id}"
        )
        await message.forward(chat_id=ADMIN_ID)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, message_handler))
    print("🤖 ربات فاپلازا VPN اجرا شد.")
    app.run_polling()
