import random
def taomatkhau():
    dodai=random.randint(7,10)    
    kytu=[chr(i) for i in range (33,127)] # trả về ký tự tương ứng với mã ASCII
    password=''.join(random.choice(kytu) for i in range (dodai)) # ghép các phần tử của 1 dsach list khác thành một chuỗi. ( '' được thêm vào chuỗi random choice... )
    return password

def kq():
    print("Password:",taomatkhau())
 
if __name__ == '__main__':    # dùng để import from qua các bài khác.      
  kq()

