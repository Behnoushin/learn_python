import os, time

path = "myfile.txt"

time_interval= time.time()

ti_c = os.path.getctime(path)

c_ti = time.ctime(ti_c)

print(f"The file located at the path {path} \
was created at {c_ti} and was "
      f"My program took", time.time() - time_interval, "to run")