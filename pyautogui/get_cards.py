from PIL import Image
import pyautogui
import time

# 假設牌的寬度和高度都是 card_width 和 card_height
card_width = 131
card_height = 187.5

# 假設整個頁面截圖是 screenshot
# 這裡需要根據實際情況替換 screenshot
screenshot = Image.open("screenshot1.png")

# 設定起始位置
start_x = 815
start_y = 185

# 切割並保存每張牌的圖片
for i in range(1):  # 假設有 5 張牌 # 計算每張牌的區域
    left = start_x + i * card_width 
    top = start_y + card_height 
    right = left + card_width
    bottom = top + card_height 
 
    # 切割牌的區域
    card_image = screenshot.crop((left, top, right, bottom))

    # 保存切割後的牌的圖片 (可選)
    card_image.save(f"撲克牌_{0}.png")

    # 顯示切割後的牌的圖片 (可選)
    #card_image.show()
