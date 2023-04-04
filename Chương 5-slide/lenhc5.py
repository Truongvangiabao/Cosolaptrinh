# in 1 chuỗi theo cách phạm vi lớn:
# L=[x for x in range(1,11,2)]
# print(L) --> [1,3,5,7,9]

#list:
# char=list('Python')
#print(char) --> ['P','y','t','h','o','n']

#index:
# A=[1,2,3,4,5]
# A[2] --> 3
# A[-1] --> 5.
# Index bắt đầu từ số 0 - phần tử thứ (n-1)
# A[0:3] --> [1,2,3]
# A[0:-1] --> [1,2,3,4]
# A=[[1,2,3],[4,5,6],[7,8,9]]
# A[2][2] --> 6.


# remove và dell:
# remove loại bỏ các giá trị chỉ định, còn dell chỉ xóa các chỉ số tương ứng trong list.


# append và insert:
# append thêm phần tử x vào cuối list.
# insert thêm phần tử x vào vị trí chỉ định.
# A=[1,2,3]
# A.append('hello') --> [1,2,3,'hello']
# A.insert(1,'hello') --> [1,'hello',2,3]


# sort(): sắp xếp tham số tăng dần.
# sort(reverse=True) : săp xếp tham số giảm dần.
# A=[1,3,2,-5]
# A.sort() --> [-5,1,2,3]
# A.sort(reverse=True) --> [3,2,1,-5]



# upper và lower:
# upper: viết hoa các ký tự trong chuỗi, lower: viết thường các ký tự trong chuỗi.
# A=[Hello World]
# print(A.upper()) --> 'HELLO WORLD'
# print(A.lower()) --> 'hello world'


#capitalize() và title():
# capitalize(): viết hoa ký tự đầu tiên của chuỗi và giữ nguyên các ký tự còn lại.
# title(): viết hoa các chữ cái đầu tiên của các từ trong chuỗi và giữ nguyên các chữ cái còn lại.


# clear(): xóa tất cả các phần tử trong list.
# A=[1,2,3,4,5]
# A.clear()
# print(A) --> []


# count(x): đếm số phần tử x xuất hiện trong list. 
# A=[1,2,3,4,5,5,6]
# print(A.count(5)) --> 2
# print(A.count(7)) --> 0


# copy():
# A=[1,2,3]
# A.copy() --> [1,2,3]
#              [1,2,3]


# pop(i): Xóa và lấy ra giá trị của phần tử có số chỉ mục i trong list. 
# A=[1,2,3,4]
# x=A.pop(2) --> A=[1,2,4] , x=3
# Nếu pop() --> lấy giá trị cuối của list. 
# x=A.pop() --> A=[1,2,3] , X=4  