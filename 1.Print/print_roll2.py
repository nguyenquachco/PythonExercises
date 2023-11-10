# In ra dòng chữ "Cộng hòa xã hội chủ nghĩa Việt Nam" xoay vòng
# Dùng vòng lặp while kết hợp với biến xâu 
# Dùng hàm time.sleep() để dừng một chút mỗi lần xoay vòng
# Dùng hàm keyboard.is_pressed() để thoát khi phím space được bấm (không cần phải bấm Ctrl + C)
import time
import keyboard
str = "Cộng hòa xã hội chủ nghĩa Việt Nam  "
tim_cnt = 0
while True:
    if tim_cnt == 0:
        print(f"\r{str}", end = '\0')
        str = str[1:] + str[0]
    time.sleep(0.01)
    tim_cnt = tim_cnt + 1
    if tim_cnt >= 100:
        tim_cnt = 0
    if keyboard.is_pressed('space'):
        break

