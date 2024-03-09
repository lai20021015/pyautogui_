import pyautogui
import time
import os
rate = 0.958
# 輸入網址
url = "https://hackmd.io/k6XMnrNNTnK4pZnU4RSCpQ#%E9%99%84%E4%BB%B6"
url = "https://laijunbin.github.io/sevens/"
pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.typewrite(url)
pyautogui.press('enter')  # 按下 Enter 鍵
time.sleep(1)  # 等待網頁加載完成
entry = pyautogui.locateCenterOnScreen('v1.png')
pyautogui.click(entry)
# 這裡可以繼續添加 PyAutoGUI 指令，以實現你的需求
# 例如，你可以使用 pyautogui.click()、pyautogui.write() 等指令與網頁進行互動

gamelogic = True
# 初始化布尔数组，表示所有牌都未使用
cards = [False] * 52
# 初始化包含卡片名称的数组
card_names = []
handcards = [] #紀錄可以出的手牌
cardsonboard = [False] * 52 #紀錄屏幕中出現過的手牌
cardyoucanplay = [False] * 52
for i in range(4):
    cardyoucanplay[6+i*13] = True
suits = ['c', 'd', 'h', 's']
for suit in suits:
    for i in range(1, 14):
        card_names.append(suit + str(i))
#判断可以出的牌
while True: #進入迴圈直到遊戲結束
    time.sleep(4)
    for i in range(0, 52):
        #print('目前卡片是:', card_names[i], end=' ')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "cards", card_names[i] + '.png')
        try:
            tmp = pyautogui.locateCenterOnScreen(image_path, confidence = rate)
            if tmp is not None:
                cards[i] = 1
                #print('找到了, 你要的位置是:', tmp)
                #pyautogui.moveTo(i*30, 200)
                tx, ty = tmp
                if tx > 868 & tx <1706 & ty > 971 & ty <1200:
                    #print('加入手牌:',card_names[i],'~~開心!!')
                    handcards.append(card_names[i])
            #else:
                # 未找到图像的处理逻辑
                #print(f"未找到圖像: {card_names[i]}")
        except pyautogui.ImageNotFoundException:
            continue
            # 处理找不到图像的异常
            #print(f"!未找到圖像: {card_names[i]}")
    print("可以出的手牌有:", handcards, '總共有:' , len(handcards), '張')
    playable_cards = [] #紀錄可以打的牌
    for i in range(4):
        playable_cards.append(card_names[6+i*13])
    print('可以出的牌有:', playable_cards)
    break