# i=1
# while i<=18 and i>=1 :
#     n=17
#     while i-1<=n :
#         print(' ',end="")
#         n=n-2 
#     j=1
#     while j<=i :
#         print('*',end="")
#         j=j+1
#     print('')
#     i=i+2 

# i=1
# n=17
# #n=int(input("n="))
# while i<=n:
#     print(" "*((n-i)//2),end="")
#     print("*"*(i))
#     i=i+2
# print()


n=int(input('n='))
i=1
while i<=n:
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
    i=i+1