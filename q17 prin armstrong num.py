n=int(input("entwr armstrong num"))
b=(n)
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if b==sum:
    print("armstrong")
else:
    print("no armstrong num")