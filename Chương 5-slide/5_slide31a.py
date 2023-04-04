A=[]
print('Nhap 10 so nguyen:')
i=1
while i<=10:
    n=int(input())
    i=i+1
    A=A+[n]
x=int(input('x='))
for i in range(len(A)):
    if A[i]==5:
        A[i]=x
print(A)


