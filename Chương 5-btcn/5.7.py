L=[]
M=[]
n=int(input('n='))
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
for i in L:
    if i not in M:
        M=M+[i]
print(*M) # *: chuyển list thành string.


# n=int(input('n='))
# L=[]
# for i in range(n):
#     j=int(input())
#     L.append(j)
# M=[]
# for i in L:
#    if i not in M: 
#        M.append(i)
# for a in M:
#     print(a,end=" ")
    
