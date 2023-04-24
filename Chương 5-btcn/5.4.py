A=[]
n=int(input('n='))
for i in range(1,n+1):
    a=int(input())
    A=A+[a]
B=A.copy()
B.reverse()
print(B)
B.sort()
print(B)


# n=int(input('n='))
# A=[]
# for i in range(n):
#     j=int(input())
#     A.append(j)
# B=A[::-1]
# print(B) 
# B.sort()
# print(B)

