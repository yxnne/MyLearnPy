import easygui as g
import random

the_num = random.randint(0, 100)
you_guess = 0
try_times = 0

allow_time = 6

info = '现在已经准备好了秘数，请猜测一个数字，是0---100之间的'
while try_times < allow_time and you_guess != the_num:
    # you_guess = int(input(info))
    info_times = '现在还有' + str(allow_time - try_times) + '次机会'
    you_guess = g.integerbox(info + info_times, title='猜数字', lowerbound=0, upperbound=100)
    try_times += 1
    if you_guess < the_num:
        # print('你的数字小了')
        g.msgbox('你的数字小了', image='./res/q.png')
    elif you_guess > the_num:
        # print('你的数字大了')
        g.msgbox('你的数字大了', image='./res/q.png')

if you_guess == the_num:
    # print('很好，猜对了，就是', the_num)
    g.msgbox('很好，猜对了，就是' + str(the_num), image='./res/right.png')
else:
    # print('遗憾，你并没有猜中它,它是', the_num)
    g.msgbox('遗憾，你并没有猜中它,它是' + str(the_num), image='./res/wrong.png')
