i=1
while i<2:
    print("hello"*3)
    i=i+1




i=1
while i<=100:
    if i%3==0 and i%7==0:
        print("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    else:
        print(i)
    i=i+1


i=30
while i<=421:
    if i%8==0:
        print(i)
    i=i+1

num=int(input("enter no"))
num1=int(input("enter no"))
i=1
s=0
while i<=num:
    s=s+num1
    i=i+1
print(s)