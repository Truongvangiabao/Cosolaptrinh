a=0 #số dương 
b=0 #số âm
while True:
    n=int(input())
    if n>0 :
        a=a+1
    elif n<0 :
        b=b+1
    else :
        break
print(a,'so duong')
print(b,'so am')