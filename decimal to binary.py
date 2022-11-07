decimal=int(input("enter num"))
num=" "
while decimal!=0:
    num=str(decimal%2)+num
    decimal//=2
print(num)

d=int(input("enter num"))
b=""
while d!=0:
    b=str(d%2)+b
    d=d//2
print(b)

date=int(input("enter the number-:"))
s=date[0::8]
s1=date[3:5:]
s2=date[6:]
print(s)
print(s1)
print(s2)
a=["shivani"]
i=0
j=5
while i<len(a[0]):
    print(a[0][i],end=" ")
    print(j,end=" ")
    j=j+5
    i=i+1

l=[3,5,6,7]
b=bytes(l)
print(b)
a=(True and False )and True and True  and False and True and True and False
print(a)

a=int(input("enter the number:-"))
if a%2==0:
    print("even")
else:
    print("odd")

