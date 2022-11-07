n=int (input('enter arm strong num'))
i=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if i==sum:
    print("armstrong num")
else:
    print("not armstrong num")
