# add_script.py
# for my mi 6
import os
import time
WEL = 'yxnne for add money in the game~~~~\nGood luck~~~Have Fun'

cmd_again = 'adb shell input swipe 1494 871 1494 871'
cmd_next = 'adb shell input swipe 1624 990 1624 990'
cmd_attack = 'adb shell input swipe 1737 898 1737 898'

print(WEL)
while True:
	os.system(cmd_again)
	os.system(cmd_next)
	os.system(cmd_attack)
	time.sleep(0.5)