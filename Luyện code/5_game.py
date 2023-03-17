import random
def nguoi():
    n=int(input('(1)Keo,(2)Bua,(3)Bao:'))
    while n<0 or n>=4:
        print('Không hợp lệ, mời nhập lại:',end="")
        n=int(input())
    return n

def may():
    m=random.randint(1,3)
    print('Máy chọn:',m,sep="")
    return m

def Ket_qua(n,m):
    if n==m:
        print('Hòa Nhau')
    elif (n==1 and m==3) or (n==2 and m==1) or (n==3 and m==1):
        print('Chúc mừng!Bạn đã thắng.')
    else:
        print('Rất tiếc!Bạn đã thua.')

while True:
    n=nguoi()
    if n==0:
        break
    m=may()
    Ket_qua(n,m)
