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
pyautogui.press('enter') 
time.sleep(1)
entry = pyautogui.locateCenterOnScreen('v1.png')
pyautogui.click(entry)
gamelogic = True
cards = [False] * 52
card_names = []
handcards = [] 
cardsonboard = [False] * 52 
cardyoucanplay = [False] * 52
for i in range(4):
    cardyoucanplay[6+i*13] = True
suits = ['c', 'd', 'h', 's']
for suit in suits:
    for i in range(1, 14):
        card_names.append(suit + str(i))
while True:
    time.sleep(4)
    for i in range(0, 52):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "cards", card_names[i] + '.png')
        try:
            tmp = pyautogui.locateCenterOnScreen(image_path, confidence = rate)
            if tmp is not None:
                cards[i] = 1
                tx, ty = tmp
                if tx > 868 & tx <1706 & ty > 971 & ty <1200:
                    handcards.append(card_names[i])
        except pyautogui.ImageNotFoundException:
            continue
    print("可以出的手牌有:", handcards, '總共有:' , len(handcards), '張')
    playable_cards = [] 
    for i in range(4):
        playable_cards.append(card_names[6+i*13])
    print('可以出的牌有:', playable_cards)
    break