import random 
def biensoxe():
    if random.random()<0.5: #tỷ lệ biển cũ biển mới là 50/50
        a=random.randint(0,9) #random.randint(0,9) là chọn ngẫu nhiên 1 số trong khoảng từ 0 đến 9.
        b=random.randint(0,9)
        c=random.randint(0,9)
        d=random.randint(0,9)
        x=random.choice("qwertyuiopasdfghjklzxcvbnm") #random.choice(...) là chọn ngẫu nhiên 1 ký tự trong list đã cho.
        y=random.choice("qwertyuiopasdfghjklzxcvbnm")
        z=random.choice("qwertyuiopasdfghjklzxcvbnm")
        print(a,b,c,d,x,y,z,sep="")
    else:
        a=random.randint(0,9)
        b=random.randint(0,9)
        c=random.randint(0,9)
        x=random.choice("qwertyuiopasdfghjklzxcvbnm")
        y=random.choice("qwertyuiopasdfghjklzxcvbnm")
        z=random.choice("qwertyuiopasdfghjklzxcvbnm")
        print(x,y,z,a,b,c,sep="")
        
biensoxe()