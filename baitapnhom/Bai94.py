import random
def taomatkhau():
    dodai=random.randint(7,10)    
    kytu=[chr(i) for i in range (33,127)]
    password=''.join(random.choice(kytu) for i in range (dodai)) 
    return password

def kq():
    print("Password:",taomatkhau())
 
if __name__ == '__main__':          
  kq()

