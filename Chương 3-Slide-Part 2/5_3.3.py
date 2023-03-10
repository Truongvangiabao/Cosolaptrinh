# a=1
# while a<10 :
#     x=1
#     while x<10 :
#         print(x*a," ",end="")
#         x=x+1
#     a=a+1
#     print("")
    
    
    
a=1
while a<=9 :
        for i in range (1,10) :
                print(a*i,end="\t")
        if (a*i)%9==0 :
                print("")
        a=a+1