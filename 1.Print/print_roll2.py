# In ra dòng chữ "Cộng hòa xã hội chủ nghĩa Việt Nam" xoay vòng
# Dùng vòng lặp while kết hợp với biến xâu 
# Dùng hàm time.sleep() để dừng một chút mỗi lần xoay vòng
# Dùng hàm keyboard.is_pressed() để thoát khi có phím bấm (không cần phải bấm Ctrl + C)
import time
import keyboard
str = "Cộng hòa xã hội chủ nghĩa Việt Nam  "
while True:
    print(f"\r{str}", end = '\0')
    str = str[1:] + str[0]
    time.sleep(1)
    if (keyboard.is_pressed('a')):
        break

