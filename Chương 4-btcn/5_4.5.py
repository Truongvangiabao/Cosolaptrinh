def LaSoNguyenTo(x):
    s=0
    for i in range(1,x+1):
        if x%i==0:
            s=s+1
    if s==2:
        return True
    return False
def SoHopLe(x):
    if x<=1:
        return True
    else:
        return False
def NhapVaDem():
    dem=0
    print('Nhap day so:')
    while True:
        x=int(input())
        if SoHopLe(x):
            break
        if LaSoNguyenTo(x)==True:
            dem=dem+1
    return dem
def InKQ(kq):
    print(f'Co {kq} so nguyen to')

dem=NhapVaDem()
kq=dem
InKQ(kq)
    