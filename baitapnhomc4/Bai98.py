def nhap():
    a=input('Nhap du lieu:')
    a=a.upper() # Để loại trừ trường hợp nhập chữ thường (viết hoa)
    return a
def hex2int(a):
    A=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    s=0 # a=7DE
    B=len(a)-1 # số mũ
    for i in a: # i nhận từ giá trị trong chuỗi a
        if i in A:
            x=A.index(i) # vi thu cua i trong chuoi A , x=3
            s=s+x*(16**B)
        B=B-1
    return s
def int2hex(a):
    B=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    kq=''
    while True:
        b=a%16 
        kq=B[b]+kq # lấy B[b] để tìm vị trí thứ b trong list B
        a=a//16
        if a==0: break
    return kq
a=nhap()
c=int(input("So ban thuoc he may:"))
if c==10:
    u=0
    for l in a:
        if l in '0123456789':
            u=1
        else:
            u=0
            print("Khong hop le")
            break
    if u==1:
        print(f"So ban nhap chuyen tu he {c} sang he 16:")
        print(int2hex(int(a)))

elif c==16:
    print(f"So ban nhap chuyen tu he {c} sang he 10:")
    print(hex2int((a)))
else:
    print("khong hop le")