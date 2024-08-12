# ساخت ساعت دیجیتال 
import time
while True:
    from datetime import datetime # تاریخ و زمان 
    now = datetime.now()  # تاریخ و زمان کنونی 
    print ("%s/%s/%s | %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second)) 
    # %s برای جایگرینی string 
    time.sleep(1) #  برای ایجاد وقفه و بر حیب ثانیه است 