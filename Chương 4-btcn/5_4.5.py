def LaSoNguyenTo(x):
    if x<=1 :
        return False
    s=0
    for i in range(1,x+1):
        if x%i==0:
            s=s+1
    if s==2:
        return True
    return False
def SoHopLe(x):
    if x<=1:
        return False
    return True
def NhapVaDem():
    dem=0
    print("Nhap day so:")
    while True:
        x=int(input())
        if SoHopLe(x)==False:
            break
        if LaSoNguyenTo(x):
            dem=dem+1
    return dem
def InKQ(dem):
    print("Co",dem,"so nguyen to")
dem=NhapVaDem()
InKQ(dem)