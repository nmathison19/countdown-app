import time, subprocess, re
print('enter name')
user_name =str(input())
print('select a number to countdown to zero')
num = input()
if bool(re.search(r'[a-zA-Z]', num)):
    print('no, please enter numbers only.')
    print('select a number to countdown to zero')
    num = input()
    if bool(re.search(r'[a-zA-Z]', num)):
        print('no, please enter numbers only.')
        print('select a number to countdown to zero')
        num = input()
        if bool(re.search(r'[a-zA-Z]', num)):
            print('you are not ready. come back later.')

else:
    timeLeft= int(num)
    print("Alright. Here we go" + "," + " " + user_name +".")
    time.sleep(1)
    while timeLeft > 0:
        print(str(timeLeft))
        time.sleep(1)
        timeLeft=timeLeft-1
    print("the break is over," + " "+ user_name +".")
    print("get back to work.")






