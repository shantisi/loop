n=int(input("enter num"))
b=n
rev=0
while n>0:
    rev=(rev*10)+n%10
    n=n//10
if b==rev:
    print("palindrom num")
else:
    print("not palindrom")

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter"))
if a>b and a>c:
    print(a,"greatest number")
elif b>a and b>c:
    print(b"great")
elif c>a and c>b:
    print(c,"great")

if a>b and a<c: 
    print(a,"second")
elif b>a and b<c:
    print(b,"second")
elif c>a and c<b:
    print(c,"second")

def pro(a):
    i=0
    proo=1
    while i<len(a):
        proo=proo*a[i]
        i=i+1
    print(proo)
pro(([2,4,5,6,7,5]))        



a="my name is rani singh"
i=0
s=""
while i<len(a):
   if a[i][0]:
    k=[i][0].upper()
    s=s+k


j=1
k={}
dic ={1:300,2:300,3:300,4:100}
for i in dic:
    if dic[i] not in k:
        k.update({i:dic[i]})
print(k)

d={1:100,2:100,3:300,4:100}
d1={}
for i,j in d.items():
    if j not in d1.values():
        d1[i]=j
        # print(d1)
print (d1)

# 9. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d={}
for i in d1:
    for j in d2:
        if i==j:
            d1[i]=d1[i]+d2[j]
            d.update({i:d1[i]})
        else:
            d.update({i:d1[i]})
            d.update({j:d2[j]})
print(d)

d1 = {4: 100, 2: 200, 3:300}
for  i in d1:
    for j in d1:
        if i>=j:
            print(i)


day=int(input("enter the no"))
month=int(input("enter month no"))
year=int(input("enter year no")) 
if day>=1 and day<=31 and month>=1 and month<=12 or year>=1900 and year>=2023:
    print(day+1,"/",month+1,"/",year+1)

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i+1
while s<=5-i:
        print("",end="")
        s=s+1


i=1
while i<=5:
    s=1
    while s<=5-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    k=i-1
    while k>=1:
        print(k,end="")
        k=k-1
    print()
    i=i+1
        

a="python is very easy"
b=a.split()
print(len(b))




    