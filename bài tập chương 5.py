#5.1
print("** ** ******    **      **     ** ****" )
print("** ** **        **      **     **   **")
print("***** ******    **      **     **   **")
print("** ** **        **      **     **   **")
print("** ** ** ****   ******  ******  ******")


#5.2
x=10
y=5
tong=x+y
hieu=5
tich=x*y
thuong=x/y
print('Tổng của hai số    ', x, '+', y, '=',tong)
print('Hiệu của hai số    ', x, '-', y, '=',hieu)
print('Tích của hai số    ', x, '*', y, '=',tich)
print('Thuong của hai số  ', x, '/', y, '=',thuong)

#5.3
ten_hang = "Sữa hộp Vinamilk"
so_luong = 5
don_gia = 25000
tien_phai_tra = so_luong * don_gia
print("Tên hàng:", ten_hang)
print("Số lượng:", so_luong)
print("Tiền phải trả:", tien_phai_tra)


#5.4
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Diện tích tam giác là:", s)