import time
print("welcome to my world ")
db=(input("are you ready to star the calculator ? "))
if db=='yes':
 print("please , wait  for 3 seconds ! ")
time.sleep(3)
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=(input("enter + - * /:"))
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c == '/':
    print(a / b)
else :
    print("Invalid Operation !")