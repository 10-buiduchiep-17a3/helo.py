#8.12
n = int(input("Nhập số n = "))
flag = True 
if n < 2 :
    print(n, "Không nguyên tố !!!")
else:
    for i in range(2, n):
        if n%i == 0:
            flag = False
            break
    if flag:
        print(n, " là số nguyên tố")
    else:
        print(n, " không phải là số nguyên tố!!!")


#8.14
a = int(input("nhập số nguyên N: "))
b = 0
for i in range(1, a+1):
    print("nhập số hạng thứ:", i)
    b1 = int(input())
    b = b + b1
print("tổng",a,"số hạng là ", b)

#8.15
a = True
S = 0
while a:
    print("nhập số nguyên N: ")
    b = int(input())
    S = S + b
    if b ==0:
        a = False
        break
print("tổng số hạng vừa nhập là: ",S)


#8.16
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
while(a*b!=0):
    if a>b:
        a%=b
    else:
        b%=a
print(a+b)

#8.17
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = a*b
for i in range (b, c+1):
    if i%a == 0 and i%b == 0:
        d = i
        break
print(i)

#8.18
print("Nhập vào số N lớn hơn 0: ")
n = int(input())
tong = 0
for i in range(1, n):
    if (n % i == 0):
        tong += i
if (tong == n):
    print(n, " là số hoàn hảo")
else:
    print(n, " không phải là số hoàn hảo")

#8.19
n = 20
for i in range(n, 0, -1):
    if i % 2 != 0:
        print(i, end= " ")