# L=[]
# x=int(input('x='))
# k=int(input('k='))
# n=int(input('n='))
# for i in range(1,n+1):
#     a=int(input())
#     L=L+[a]
# def add(L,x,k):
#     if k > len(L):
#         L.append(x)
#     else:
#         L.insert(k,x)
#     return L

# add(L,x,k)
# print(L)

L=[]
x=int(input())
k=int(input())
n=int(input())
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
def add(L,x,k):
    if k>len(L):
        L=L+[x]
    else:
        L=L[:k]+[x]+L[k:]
    return L


L=add(L,x,k)
print(L)