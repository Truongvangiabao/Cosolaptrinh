x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=='+' :
    print(x,ch,y,'=',round(x+y,1),sep="")
elif ch=='-' :
    print(x,ch,y,'=',round(x-y,1),sep="")
elif ch=='*' :
    print(x,ch,y,'=',round(x*y,1),sep="")
elif ch=='/' and y>0 :
    print(x,ch,y,'=',round(x/y,1),sep="")
elif y==0 :
        print('Khong hop le')
else :
    print('Khong hop le')