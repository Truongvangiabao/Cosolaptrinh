def Nhap():
    n=int(input('n='))
    return n

def giaithua(n):
    import math
    X=math.factorial(n)
    return X

def inkq(n,X):
    print(n,'!=',X,sep="")

n=Nhap()
X=giaithua(n)
inkq(n,X)
    