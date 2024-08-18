import telegram # برای این باید telegram bot رو نصب کنیم برای تعامل با API تلگرام

TOKEN = '7352228948:AAFIPyJBKEHE13Dt0msqddRoMFnakhSqpfY' # توکن ربات تلگرام

a = telegram.Bot(TOKEN) # عملیات ارسال پیام و برای برقراری ارتباط با API تلگرام

payam = input("text:") # دریافت ورودی از کاربر


updates = a.get_updates() # چت آیدی همون شناسه چت هست که مشخص کنیم به کجا ارسال شه که میتونه کانال باشع یا شخصی # روش پیدا کردن آن نیز متفاوت
for update in updates:
    chat_id = 29637597
    print(f"Chat ID: {chat_id}")

a.send_message(chat_id , payam) # (به همون چت آیدی که مشخص کردیم) ارسال پیام به تلگرام

print(f"Message sent: {payam}")