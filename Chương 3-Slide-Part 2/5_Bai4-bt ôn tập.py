while True: #vòng lặp vô hạn.
    a=float(input('a='))
    b=float(input('b='))
    ch=input('Toan tu:')
    if ch=='+' :
            print(a,ch,b,'=',a+b,sep="")
    elif ch=='-' :
            print(a,ch,b,'=',a-b,sep="")
    elif ch=='*' :
            print(a,ch,b,'=',a*b,sep="")
    elif ch=='/' and b!=0 :
            print(a,ch,b,'=',a/b,sep="")
    elif b==0 :
        print('Khong hop le')
    else :
        print('Khong hop le')
    d=str(input('Tiep tuc='))
    if d=='T' or d=='t' :
        break

    
        
        
    
    

        
