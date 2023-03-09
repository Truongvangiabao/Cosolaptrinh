# n=int(input('n='))
# i=1
# while i<=n:
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1))
#     i=i+1
    
    
n=17
for i in range (1,18,2) :
    print(" "*((n-i)//2),end="")
    print("*"*i)