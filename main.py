
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# توكن البوت الخاص بك
BOT_TOKEN = "7467974581:AAHMn45v57wU8NMYyW96-Y_SJOf7JLqYdAM"

# رسالة الترحيب
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلًا بك في 🎓 *ميدو أكاديمي – للبحوث والدراسات الجامعية* 📚\n\n"
        "نحن هنا لمساعدتك في:\n"
        "✅ حلول الكويزات\n✅ مشاريع التخرج\n✅ أبحاث جامعية\n\n"
        "استخدم الأوامر التالية لاختيار الخدمة المطلوبة:\n"
        "/طلب_بحث – لطلب بحث\n"
        "/حل_كويز – لحل كويز\n"
        "/مشروع_تخرج – لطلب مشروع\n"
        "/تواصل – للتواصل مع الفريق\n\n"
        "📌 تابع قناتنا: t.me/Universty_ESU",
        parse_mode="Markdown"
    )

async def طلب_بحث(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 أرسل تفاصيل البحث: التخصص، عدد الصفحات، وموعد التسليم.")

async def حل_كويز(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📩 أرسل صورة أو نص الكويز وسنقوم بمساعدتك بأسرع وقت!")

async def مشروع_تخرج(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎓 أرسل عنوان المشروع والتخصص والموعد المطلوب.")

async def تواصل(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 للتواصل مع فريق الدعم، راسلنا عبر: @YourSupportUsername")

# إعداد التطبيق
app = ApplicationBuilder().token(BOT_TOKEN).build()

# ربط الأوامر بالمهام
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("طلب_بحث", طلب_بحث))
app.add_handler(CommandHandler("حل_كويز", حل_كويز))
app.add_handler(CommandHandler("مشروع_تخرج", مشروع_تخرج))
app.add_handler(CommandHandler("تواصل", تواصل))

# بدء تشغيل البوت
print("🤖 البوت يعمل الآن...")
app.run_polling()
