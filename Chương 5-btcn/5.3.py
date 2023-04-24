L=[]
s=0
b=0
c=0
n=int(input('n='))
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
    if a>0:
        s=s+1
    if a%2==0:
        b=b+a
        c=c+1
print(f'SND={s}')
if c!=0:
    print(f'TBC={b/c}')
else:
    print(f'TBC={c}')
    

# n=int(input('n='))
# L=[]
# for i in range(n):
#     j=int(input())
#     L.append(j)
# count=0
# for j in L:
#    if j>0:
#        count+=1
# tong=0
# sochan=0
# for j in L:
#     if j%2==0:
#         sochan=sochan+j
#         tong+=1
# if sochan==0:
#     tbc=0
# else:
#     tbc=sochan/tong
# print('SND=',count,sep="")
# print('TBC=',tbc,sep="") 
