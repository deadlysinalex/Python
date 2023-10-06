def loop():
    print("What number do you want to use?")#asking user to give a number
    l = eval(input("your number: "))
    for i in range(0,l):
        print(i)
        num=1
        for j in range(0, i+1):
            print(num, end=" ")
            num=num+1
loop()
