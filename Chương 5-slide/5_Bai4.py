# L=[]
# def count(L):
#     i=0
#     while True:
#         a=int(input())
#         L=L+[a]
#         i=i+1
#         if a==0:
#             break
#     print('So luong phan tu la:',i,sep='')
#     return L
# count(L)

L=[]
n=int(input())
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
def count(L):
    a=0
    for i in range(len(L)):
        a=a+1
    return a

a=count(L)
print(a)



