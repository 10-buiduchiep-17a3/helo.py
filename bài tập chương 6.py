#6.4
yeu_cau_1 = (5 - 3) // 2
print("(5-3)//2", "=", yeu_cau_1)
yeu_cau_2 = (8-3*2)-(1+1)
print("(8-3*2)-(1+1)", "=", yeu_cau_2)

#6.5
So_luong= int(input("Nhập số lượng:"))
Don_gia= int(input("Nhâp đơn giá:"))
print("Thành tiền=", So_luong, "*", Don_gia, "=", So_luong*Don_gia)


#6.6
alice_candies=121
bob_candies=77
carol_candies=109
to_smash=(alice_candies+bob_candies+carol_candies)%3
print("số kẹo phải đập là =",to_smash)

#6.7
Nhiet_do = float(input("Nhập nhiệt độ: "))
Do_F = ((Nhiet_do) * 9/5) + 32
print(f"{Nhiet_do:.2f} độ C = {Do_F:.2f} độ F")

#6.8
s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")
s3 = input("Nhập chuỗi s3: ")
index = int(input("Nhập chỉ mục index: "))
chieu_dai_s1 = len(s1)
chieu_dai_s2 = len(s2)
chieu_dai_s3 = len(s3)
print(f"Chiều dài của chuỗi s1: {chieu_dai_s1}")
print(f"Chiều dài của chuỗi s2: {chieu_dai_s2}")
print(f"Chiều dài của chuỗi s3: {chieu_dai_s3}")
s4 = s1[index:]
lap_lai_chuoi_s2 = s2 * 2
print(f"Chuỗi con s4 từ index đến hết: {s4}")
print(f"Chuỗi s2 lặp lại 2 lần: {lap_lai_chuoi_s2}")