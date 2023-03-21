# Viết chương trình kiểm tra SNT

def Nhap():
    n=int(input('n='))
    return n

def LaSNT(x):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s=s+1
    if s==2:
        return True
    else:
        return False

def InKQ(n):
    if LaSNT(n):
        print(n,'la SNT')
    else:
        print(n,'khong la SNT')

n=Nhap()
InKQ(n)



      
     