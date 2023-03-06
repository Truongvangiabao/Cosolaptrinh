a=int(input('Canh a= '))
b=int(input('Canh b= '))
c=int(input('Canh c= '))
s=(a+b+c)/2
import math
print('Dien tich cua mot tam giac theo bien la: ',math.sqrt(s*(s-a)*(s-b)*(s-c)))