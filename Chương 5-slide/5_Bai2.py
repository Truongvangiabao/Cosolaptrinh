# L=[]
# x=int(input('x='))
# n=int(input('n='))
# for i in range(1,n+1):
#     a=int(input())
#     L=L+[a]

# def search(L,x):
#     if x in L:
#         return print('index=',L.index(x),sep='')
#     else:
#         return print('None')

# search(L,x)


L=[]
x=int(input())
n=int(input())
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
def search(L,x):
    for i in range(len(L)):
        if x==L[i]:
            return i 
    return None

print(search(L,x))