def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        a=int(input())
        L=L+[a]
    return L

def Search(L):
    L.sort()
    max=L[-1]
    min=L[0]
    return max,min

def Output(max,min):
    print(max,min)
    
L=Input()
max,min=Search(L)
Output(max,min)



# def Input():
#     n=int(input('n='))
#     L=[]
#     i=0
#     while i<n:
#         j=int(input())
#         L=L+[j]
#         i+=1
#     return n,L

# def  Search(L):
#     L.sort(reverse=True)
#     Max=L[0]
#     Min=L[-1]
#     return Max,Min
# def Output(max,min):
#     print(Max,Min)
    
# n,L=Input()
# Max,Min=Search(L)
# Output(max,min)
