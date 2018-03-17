import random

the_num = random.randint(0, 100)
you_guess = 0
try_times = 0

allow_time = 6

info = '请猜测一个数字，是0---100之间的'
while try_times < allow_time and you_guess != the_num:
    you_guess = int(input(info))
    try_times += 1
    if you_guess < the_num:
        print('你的数字小了')
    elif you_guess > the_num:
        print('你的数字大了')

if you_guess == the_num:
    print('很好，猜对了，就是', the_num)
else:
    print('遗憾，你并没有猜中它,它是', the_num)
