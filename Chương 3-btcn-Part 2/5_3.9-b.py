n=int(input())
if 2<=n<=50 :
    i=2
    for i in range (2,n+1,2) :
        if i<=n :
            print(i,end=" ")
else :
    print('Khong hop le')
    