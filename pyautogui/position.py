import pyautogui
import time

time.sleep(1)
for i in range (8):
    time.sleep(1)
    print('第', i+1, '次')
    print(pyautogui.position())

# for i in range(0, 52):
#     tmp = pyautogui.locateCenterOnScreen(card_names[i] + '.png')