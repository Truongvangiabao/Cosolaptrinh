a=float(input('Tieu thu= '))
if 1<=a<=100:
    print('Phai tra=',a*550+0.1*550*a)
if 101<=a<=150:
    print('Phai tra=',(100*550+(a-100)*750)*1.1)
if 151<=a<=200:
    print('Phai tra=',round((100*550+50*750+(a-150)*950)*1.1,1))
if a>=201:
    print('Phai tra=',round((100*550+50*750+50*950+(a-200)*1350)*1.1,1))