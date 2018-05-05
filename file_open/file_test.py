import os
# write File with python

file = open('./test_file.txt', 'w')
file.write('Here you are')
file.close()


# read file
file = open('./test_file.txt')
text = file.read()
print(text)

for filename in os.listdir('./'):
    if os.path.isdir(filename):
        print('/', filename)
    elif os.path.isfile(filename):
        print('--->', filename)
