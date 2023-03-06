n=int(input('n='))
chuso=0     #biến đếm có bao nhiêu chữ số
i=1   #biến chia
if 0<=n<=9999:
    while True:
        if n//i!=0:
            chuso+=1
            i*=10
        else:
            break
    print(n,'co',chuso,'chu so')
else :
    print ('Khong hop le')