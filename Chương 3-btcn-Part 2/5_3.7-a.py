while True :
    n=int(input())
    i=1
    a=1
    if n<0 :
        break
    while i<=n :
        a=a*i
        i=i+2
    print(a)