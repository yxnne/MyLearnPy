import easygui as g

# user_press = g.msgbox('hi,girl~')
# print(user_press)

# user_choose = g.buttonbox("what do you want ?", choices=['A', 'B', 'C'])
# g.msgbox('你的选择是' + user_choose)

# user_choose = g.choicebox("what do you want ?", choices=['A', 'B', 'C'], title='测试')
# g.msgbox('你的选择是' + user_choose)


# user_choose = g.buttonbox("what do you want ?", image='./res/timg.gif', choices=['A', 'B', 'C'])
# g.msgbox('你的选择是' + user_choose)


# say = g.enterbox(msg="请说出此时你的心里话", title="心里悄悄话")
# g.msgbox('you say ' + say)

# integerbox() 为用户提供一个简单的输入框，用户只能输入范围内（lowerbound参数设置最小值，upperbound参数设置最大值）的整型数值，否则会要求用户重新输入。
g.integerbox(msg='输入下值把吧', title='Guess', default=0, lowerbound=0, upperbound=99)

