A=[]
x=0
n=int(input('n='))
for i in range(1,n+1):
    a=int(input())
    A=A+[a]
for i in A:
    if A.index(i)%2!=0:
        x=x+i
print(f'Tong={x}')


# n=int(input('n='))
# A=[]
# for i in range(n):
#     j=int(input())
#     A.append(j)
# tong=0
# for i in range(n):
#     if (i+1)%2==0: 
#         tong+=A[i]
# print('Tong=',tong,sep="")