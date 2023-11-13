#4.1
a =int(input("Nhập vào giá trị của a :"))
if a>0 :
 binh_phuong = a*a
 print("Giá trị bình phương của a  là:",binh_phuong)
else:
  print("a là số âm")

  #4.2
n=int(input("Nhập vào giá trị n :"))
for i in range (1,n):
    print("Dãy số từ 1-n là :",i)
  

#4.3
m=int (input("Nhập vào giá trị m:"))
n=int(input("Nhập vào giá trị n :"))
for i in range (1,n):
        if i%m==0:
            print (i)

#4.4
m,n,p=map(int,input("Nhập vào 3 số tự nhiên :").split())
print("Số lớn nhất trong 3 chữ số là :", max (m,n,p))


#4.5
a=int(input("Nhập vào số nguyên a :"))
b=int(input("Nhập vào số nguyên b :"))
x,y=a,b
while x != y :
    if x > y : x = x-y
    else : y = y - x
print ("Bội chung nhỏ nhất của 2 số",a,"va",b,"la :",a*b//x)