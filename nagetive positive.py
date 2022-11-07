num=int(input("enter no "))
while True:
    if num>0:
        print(num,"positive")
        break
    elif num<0:
        print(num,"nagetive")
        break
    else:
        print("zero")
        break
    


n=1
while n<=100:
    count=0
    i=2
    t=n//2
    while i<=t:
        if n%i==0:
            count=count+1
        i=i+1
    if count==0 and n!=1:
        print(n,end=" ")
    n=n+1