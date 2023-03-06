a=int(input('M1='))
b=int(input('M2='))
c=int(input('M3='))
s=int(input('S='))
if s<=100 :
    print('Phai tra:',s*a,sep="")
if 101<=s<=150 :
    print('Phai tra:',100*a+(s-100)*b,sep="")
if s>=151 :
    print('Phai tra:',100*a+50*b+(s-150)*c,sep="")