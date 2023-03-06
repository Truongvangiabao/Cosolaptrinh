n=int(input('n='))
if 2<=n<=100 :
    if n%2==0 or n%3==0 or n%5==0 or n%7==0 :
        print(n,'khong la SNT')
    elif n==2 or n==3 or n==5 or n==7 :
        print(n,'la SNT')
    else :
        print(n,'la SNT')
else :
    print('Khong hop le.')


# n=int(input('n='))
# i=2
# for i in range (2,n-1) :
#     if n%1==0 :
#         print(n,'khong la SNT')
#         break
#     else:
#         print(n,'la SNT')