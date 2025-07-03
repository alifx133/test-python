# รับอุณหภูมิจากผู้ใช้
temp = float(input("ป้อนอุณหภูมิ (°C): "))

# ตรวจสอบช่วงอุณหภูมิ
if temp < 0:
    print("หนาวจัด")
elif temp <= 15:
    print("หนาว")
elif temp <= 30:
    print("ปกติ")
elif temp <= 39:
    print("ร้อน")
else:
    print("ร้อนมาก")
