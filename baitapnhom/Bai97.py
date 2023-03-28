from bai94 import taomatkhau
from bai96 import kiemthu

def main():
    s=0
    while True:
     p=taomatkhau()
     s=s+1
     
     if kiemthu(p):
      print("Đay là password tốt á:",p)
      print('So lan thu la:',s)
      break
   
if __name__ == "__main__":
  main()
    
