# n=int(input('n='))
# if 2<=n<=100 :
#     if n%2==0 or n%3==0 or n%5==0 or n%7==0 :
#         print(n,'khong la SNT')
#     elif n==2 or n==3 or n==5 or n==7 :
#         print(n,'la SNT')
#     else :
#         print(n,'la SNT')
# else :
#     print('Khong hop le.')


            
s=0
i=1
n=int(input('n='))
for i in range(1,n+1):
    if n%i==0:
        s=s+1
if s==2:
    print(n,"la SNT")
else:
    print(n,'khong la SNT')