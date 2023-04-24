def kiemthu(i):
    if len(i)>=8 and any(c.islower() for c in i) and any(c.isupper() for c in i) and any(c.isdigit() for c in i):
        return True
    else:
        return False

def main():
    i=input("nhập pass đi: ")
    if kiemthu(i):
        print('Mat khau tot.')
    else:
        print('Mat khau khong tot.')        
if __name__ == '__main__':
  main()