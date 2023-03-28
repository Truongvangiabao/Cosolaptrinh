import math
def nhap():
    print('Nhap 3 so nguyen:')
    a=float(input('a='))
    b=float(input('b='))
    c=float(input('c='))
    d=b*b-4*a*c
    return a,b,c,d

def giaipt(a,b,c):
    if d==0:
        x1=x2=-b/(2*a)
    elif d>0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
    elif d<0:
        x1=x2=None
    return x1,x2

def inkq(x1,x2):
    if x1==x2==None:
        print('Phuong trinh vo nghiem')
    elif d>0:
        print('Phuong trinh co hai nghiem')
        print('x1=',x1,sep="")
        print('x2=',x2,sep="")
    elif d==0:
        print('Phuong trinh co nghiem kep')
        print('x1=x2=',(-b/(2*a)),sep="")
        
a,b,c,d=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)