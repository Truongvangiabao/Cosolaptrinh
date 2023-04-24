# L=[]
# x=int(input('x='))
# n=int(input('n='))
# for i in range(1,n+1):
#     a=int(input())
#     L=L+[a]
    
# def delete(L, x):
#     for i in L:
#         if i == x:
#             del(x)

# delete(L,x)
# print(L)

L=[]
x=int(input())
n=int(input())
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
def delete(L,x):
    i=0
    while i<len(L):
        if x==L[i]: #i la index cua phan tu can xoa
            L=L[:i]+L[i+1:]
        else:
            i=i+1
    return L


L=delete(L,x)
print(L)