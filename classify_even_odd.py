m=int (input("enter m:  "))
n=int (input("enter n:  "))
i=0
for i in range(m, n+1):
    if(i%2==0):
        print(i,'=even')
    else:
        print(i,'=odd')
