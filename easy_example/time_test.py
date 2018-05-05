import time

t = time.time()
print(t)
print(time.asctime())

ti = time.localtime(t)
print(ti)

str_ti = time.strftime("%a %b %d %H:%M:%S %Y", ti)
print(str_ti)

str_ti = time.strftime("%Y-%m-%d %H:%M:%S", ti)
print(str_ti)