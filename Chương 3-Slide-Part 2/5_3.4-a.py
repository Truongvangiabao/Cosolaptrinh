 # i=1
# while i<=9:
#     print("$"*(10-i))
#     i=i+1
    
    
# i=1
# n=int(input('n='))
# while i<=n:
#     print("$"*(n+1-i))
#     i=i+1

a=9
b=1
while a>=1:
    for i in range(1,10) :
        print('$'*((a*i)//b))
        a=a-1
        b=b+1