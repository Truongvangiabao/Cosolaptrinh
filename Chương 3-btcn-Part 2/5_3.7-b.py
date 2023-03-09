while True :
    n=int(input())
    if n<0 :
        break
    a=1
    for i in range(1,n+1) :
        a=a*i
    print(a)
    