def nhap():
    n=int(input('n='))
    return n

def inkq(n):
    for i in range(2,n+1,2):
        print(i,end=" ")
    print()
while True:
    n=nhap()
    inkq(n)
    c=str(input('Tiep tuc khong?'))
    if c=='k' or c=='K':
        break
    else:
        continue



