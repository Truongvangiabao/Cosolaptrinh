n=10
A=[]
for i in range(n):
    j=int(input())
    A.append(j)
B=[]
for i in range(0, n - 1, 2): 
    B.append(A[i + 1])  # giá trị của phần tử nằm ở vị trí thứ i + 1 trong danh sách A sẽ được thêm vào cuối danh sách B
    B.append(A[i])  # giá trị của phần tử nằm ở vị trí thứ i trong danh sách A sẽ được thêm vào cuối danh sách B
for a in B:
    print(a,end=" ")
    