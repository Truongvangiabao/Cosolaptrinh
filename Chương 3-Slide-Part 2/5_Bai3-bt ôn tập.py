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
    
    
    
# n=int(input("n="))      
# m=0
# while n>=10:
#         n=n/10
#         m=m+1      
# print(int(round(n*(10**m),0)),"co",m+1,"chu so")
