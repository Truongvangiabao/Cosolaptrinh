# Nhập n, trả về số lượng số nguyên dương và chẵn.

def Nhap():
    n=int(input('n='))
    return n

def LaSoDuong(x):
    if x>0 and x%2==0:
        return 1
    else:
        return 0

def XuLy(n):
    dem=0
    for i in range(1,n+1):
        x=int(input())
        if LaSoDuong(x)==1:
            dem=dem+1
    return dem

def InKQ(soluong):
    print('Co',soluong,'so nguyen duong va chan')
    
n=Nhap()
soluong=XuLy(n)
InKQ(soluong)
    