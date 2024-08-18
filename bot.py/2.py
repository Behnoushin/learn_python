import asyncio # برای جلوگیری از خطای ورودی و خروجی ناهمگام
from telegram import Bot # برای برقراری با توکن رباتمون ار این استفاده کردیم 
from telegram.error import TelegramError # برای ندیریت خطاهایی که در رابزه با ای پی آی تلگرامه استفاده شده

TOKEN = '7352228948:AAFIPyJBKEHE13Dt0msqddRoMFnakhSqpfY'

async def main(): # ---> این توابع به توابع ناهمگام مشهورند و چون مدل خاصب هستند قبل از تابع کلمه async می آید 
    bot = Bot(TOKEN)
    
    try: # این برنامه تحرا می شود اما هر زمان خطا خورد از این قسمت خارج میشه و وارد مرحله except
        updates = await bot.get_updates()
        for update in updates:
            if update.message:
                chat_id =29637597
                print(f"Chat ID: {chat_id}")
        
        a = input("text: ") # پیاممون
        
        # شناسه چت مورد نظر (می‌توانید از chat_id خود استفاده کنید)
        CHAT_ID = input("Please enter the CHAT_ID to send the message to: ")
        
        # ارسال پیام به تلگرام
        await bot.send_message(chat_id=CHAT_ID, text=a)
        
        # نمایش ورودی در خروجی
        print(f"Message sent: {a}")
        
    except TelegramError as e:
        print(f"Telegram error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# اجرای تابع اصلی
if __name__ == "__main__":
    asyncio.run(main())