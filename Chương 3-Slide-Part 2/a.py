import random
def nguoi():
    n = int(input("(1)Keo,(2)Bua,(3)Bao:"))
    while n >= 4 or n < 0:
        print("Không hợp lệ,mời nhập lại:", end="")
        n = int(input())
    return n
def may():
    m = random.randint(1, 3)
    return m
def gan_bien(n, m):
    i = 0
    if n == m:
        i == 0
    elif (n == 1 and m == 3) or (n == 2 and m == 1) or (n == 3 and m == 2):
        i += 1
    else:
        i -= 1
    return i
def Ket_qua(m, i):
    print("Máy chọn:",m, sep="")
    if i == 0:
        print("Hòa nhau")
    elif i == 1:
        print("Chúc mừng! Bạn đã thắng.")
    else:
        print("Rất tiếc, bạn đã thua.")
while True:
    n = nguoi()
    if n == 0:
        print('Kết thúc.')
        break
    m = may()
    i = gan_bien(n, m)
    Ket_qua(m, i)