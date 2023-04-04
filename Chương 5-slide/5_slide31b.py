A=[]
print('Nhap 10 so nguyen:')
i=1
while i<=10:
    n=int(input())
    i=i+1
    A=A+[n]
x=int(input('x='))
for i in range(len(A)):
    if x in A:
        A.remove(x) # loại bỏ các giá trị chỉ định, còn dell chỉ xóa các chỉ số tương ứng trong list.
print(A)


