# i=1
# n=int(input())
# while i<=n<=50 :
#     print(i,end=" ")
#     if i%10==0 :
#         print('\n')
#     i=i+1



n=int(input('n='))
i=1
if 1<=n<=50 :
    for i in range (1,n+1) :
        print(i,end=" ")
        if i%10==0 :
            print("")
else :
    print('Khong hop le')