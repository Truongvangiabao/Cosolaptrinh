L=[]
x=int(input())
y=int(input())
n=int(input())
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
def replace(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
    return L

L=replace(L,x,y)
print(L)