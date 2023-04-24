def Input():
    L=[]
    n=int(input('n='))
    for i in range(1,n+1):
        a=int(input())
        L=L+[a]
    x=int(input('x='))
    return L,x

def FirstAndLast(L):
    b=L.pop(0)
    c=L.pop(-1)
    print(f'[{b},{c}]')
   

def Search(L,x):
    if x in L:
        return True
    else:
        return False
    
L,x=Input()
FirstAndLast(L)
print(Search(L,x))




# def Input():
#     n=int(input('n='))
#     L=[]
#     i=0
#     while i<n:
#         j=int(input())
#         L=L+[j]
#         i=i+1
#     x=int(input('x='))
#     return n,x,L
    
# def FirstAndLast(L):
#     L1=[L[0],L[-1]]
#     print(L1)
#     return L1

# def Search(L,x):
#     if x in L:
#         print('True')
#     else:
#         print('False')
        
# n,x,L=Input()
# L1=FirstAndLast(L)
# Search(L,x)



    
    