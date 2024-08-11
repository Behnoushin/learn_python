import os , time , datetime
def create_directory(directory_name):
    os.mkdir(directory_name) # ساخت دایرکتوری 
    zaman_feli = time.time() #زمان فعلی 
    creation_datetime=datetime.datetime.fromtimestamp(zaman_feli) # ساخت دیت تایم 
    current_datetime = datetime.datetime.now() # زمان فعلی برای مدت زمان سپری شده
    time_differance = current_datetime - creation_datetime # زمان سپری شده 
    
    print(f"Directory name ---> {directory_name}, and creation time is :{creation_datetime}, time since creation:{time_differance}")
    

directory_name = "my_directory"
create_directory(directory_name)