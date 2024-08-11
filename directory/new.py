import time
def decorator(func):
    def a():
        start_time = time.time()
        ctime = time.ctime(start_time)
        print(f"start: {start_time} --> {ctime}")
        
        func()
        
        end_time = time.time()
        etime = time.ctime(end_time)
        print(f"end: {end_time} --> {etime}")
        
    return a

@decorator
def b():
    start_time = time.time()
    end_time = time.time()
    ejra = end_time - start_time
    print(f"ejra: {ejra}")
    
b()
