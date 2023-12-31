# 9.1
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
print(sign(8))  # 1
print(sign(-8))  # -1
print(sign(0))   # 0

#9.2
def duong_lich_to_amlich(nam):
    # Danh sách Can
    can_list = ["Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm"]

    # Danh sách Chi
    chi_list = ["Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất"]

    # Tính năm Âm lịch
    can = can_list[(nam + 6) % 10]
    chi = chi_list[(nam  + 8) % 12]

    return "{can} {chi}"

# Sử dụng hàm
nam_duong_lich = 2023
nam_am_lich = duong_lich_to_amlich(nam_duong_lich)
print("Năm Dương lịch" ,nam_duong_lich, "chuyển sang Âm lịch là:", nam_am_lich)

# 9.3
def bmi(can_nang,chieu_cao):
    bmi = can_nang  / (chieu_cao ** 2)
    if bmi < 18.5:
        return "Gầy"
    elif 18.5 <= bmi <= 24.99:
        return "Bình thường"
    else:
        return "Thừa cân"
#Nhập chiều cao,can nặng
can_n=int(input("Nhập cân nặng:"))
chieu_c= float(input("Nhập chiều cao:"))
print(bmi(can_n,chieu_c))

#9.4
def tinh_s(n, x):
    return (x ** 2 + 1) ** n
#Nhập giá trị 

print(tinh_s(2, 3))  # S = (3^2 + 1)^2

#9.5
def tinh_a(n, x):
    return (x ** 2 + x + 1) ** n + (x ** 2 - x + 1) ** n

#Nhập giá trị biểu thức
print(tinh_a(3, 2))  # A = (2^2 + 2 + 1)^3 + (2^2 - 2 + 1)^3

#9.6
def so_nguyen_to(x):
    if x <2:
        return "không là số nguyên tố"
    for i in range(2, int(x**0.5) + 1):#key 
        if x % i == 0:
            return "không là số nguyên tố"
    return "là số nguyên tố"

#Nhập số bất kỳ
a=int(input("Nhập vào số bất kỳ:"))
print(so_nguyen_to(a))

#9.7
def chia_so_nguyen(v, e):
    return v * (e ** 2) // 1
#Nhập giá trị
a=int(input("Nhập giá trị của a:"))
b=int(input("Nhạp giá trị của b:"))
print(chia_so_nguyen(a,b)) 

#9.8
def so_hoan_hao(x):
    tong_uoc = sum(i for i in range(1, x) if x % i == 0)
    return tong_uoc == x

#Nhập số bất kỳ
a=int(input("Nhập giá trị của a:"))
print(so_hoan_hao(a))  


