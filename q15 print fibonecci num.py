n=int(input("enter no"))
x=0
y=1
z=0
while z<=n:
    print(z,end=" ")
    x=y
    y=z
    z=x+y

