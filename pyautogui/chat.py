import pyautogui
import cv2
import pyperclip
import time
import keyboard
import os

delta = [0, 124, 654, 217]
target_image_path = 'chatblock.png'


for i in range(0, 10000):
    location = pyautogui.locateOnScreen(target_image_path, confidence=0.7)
    pyautogui.click(location)
    pyperclip.copy("對不起."+'.'*(i+1))
    keyboard.press_and_release('ctrl + v')
    keyboard.press('Enter')
    time.sleep(0.25)
    if location:
        print('傳送成功')
    # 使用 keyboard 模擬 Ctrl + V 粘貼