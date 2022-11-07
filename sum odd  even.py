i=1
evensum=0
oddsum=0
while i<=20:
    if  i%2==0:
        evensum=evensum+i
    else:
        oddsum=oddsum+i
    i=i+1
print(evensum,"evensum")
print(oddsum,"oddsum")



n=int(input("enter no"))
i=1
while i<=n:
    j=0
    while j<=10:
        print(j*i,end=" ")
        j=j+1
    print()    
    i=i+1

    