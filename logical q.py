i=0
while i<=15:
    i=i+1
    if i==3:
        print("continue",i)
        continue
    elif i==6:
        print("pass",i)
        pass
    elif i==10:
        print("break",i)
        break
    else:
        print(i)

a=int(input("enter no"))
i=0
max=a
min=a
while i<=10:
    a=int(input("enter no"))
    if a>max:
        max=a
    elif a<min:
        min=a
    i=i+1
print("max",max)
print("min",min)


