import pyautogui
import time
import os
rate = 0.9625
url = "https://laijunbin.github.io/sevens/"
pyautogui.hotkey('win', 'r') #搜尋網頁
time.sleep(0.5)

pyautogui.typewrite(url)
pyautogui.press('enter')
time.sleep(0.8) 
entry = pyautogui.locateCenterOnScreen('v1.png')
pyautogui.click(entry)
cards = [False] * 52
card_names = [] #撲克牌名稱
handcards = []
cardsonboard = [False] * 52 #打在牌池的牌
cardyoucanplay = [False] * 52 #可以出的牌

for i in range(4):
    cardyoucanplay[6+i*13] = True
suits = ['c', 'd', 'h', 's'] # 梅花, 方塊, 愛心, 黑桃
for suit in suits:
    for i in range(1, 14):
        card_names.append(suit + str(i))

cnt = 0
while cnt<5: #玩五次
    delta = 10
    time.sleep(0.8)
    os.system('cls') #清空視窗
    print('這是第', cnt+1, '次遊戲, 進行初始化') 
    time.sleep(0.3)
    cards = [False] * len(cards)
    cardsonboard = [False] * len(cardsonboard)
    cardyoucanplay = [False] * len(cardyoucanplay)
    for i in range(0, 52):
        if(cardsonboard[i]):
            continue
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "cards", card_names[i] + '.png')
        try:
            if i == 7 or i == 8: #c8, c9 太難分辨
                bonus = 0.0165
            else:
                bonus = 0
            tmp = pyautogui.locateCenterOnScreen(image_path, region=(350, 908, 900, 400), confidence = rate + bonus)
            if tmp is not None:
                cards[i] = 1
                handcards.append(card_names[i])
        except pyautogui.ImageNotFoundException:
            continue
    print("可以出的手牌有:", handcards, '總共有:' , len(handcards), '張')
    playable_cards = [] #初始化
    for i in range(4):
        playable_cards.append(card_names[6+i*13])
    while len(handcards)>0:    
        print('')
        delta += 10
        time.sleep(0.2)
        for i in range(0, 52):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, "cards", card_names[i] + '.png')
            try:
                if i == 7 or i == 8:
                    bonus = 0.0165
                else:
                    bonus = 0
                tmp = pyautogui.locateCenterOnScreen(image_path, region=(358, 346 , 1434-383, 905-346+10) ,confidence = rate + bonus - 0.0015)
                if tmp is not None:
                    cardsonboard[i] = True
                    tx, ty = tmp
                    if (i%13+1)<7 and (i%13)!=0: #Ace到6
                        cardyoucanplay[i-1]= True
                        if(card_names[i-1] not in playable_cards):
                            playable_cards.append(card_names[i-1])
                            print('新增:', card_names[i-1])
                    elif (i%13+1)>7 and (i%13)!=12: #8到K
                        cardyoucanplay[i+1]= True
                        if(card_names[i+1] not in playable_cards):
                            playable_cards.append(card_names[i+1])
                            print('新增:', card_names[i+1])
                    elif (i%13+1)==7: #等於7
                        if(card_names[i-1] not in playable_cards):
                            playable_cards.append(card_names[i-1])
                            print('新增:', card_names[i-1])
                        if(card_names[i+1] not in playable_cards):
                            playable_cards.append(card_names[i+1])
                            print('新增:', card_names[i+1])
                        cardyoucanplay[i-1]= True
                        cardyoucanplay[i+1]= True
                else:
                    print(f"未找到圖像: {card_names[i]}")
            except pyautogui.ImageNotFoundException:
                continue
        if playable_cards:
            print('可以出的牌:', playable_cards)
        common = set(playable_cards) & set(handcards)
        common_list = list(common)
        print('共同有的:', common_list)
        if len(common_list)>0:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, "cards", common_list[0] + '.png')
            index = card_names.index(common_list[0])
            try:    
                if index == 7 or index == 8:
                    bonus = 0.0165
                else:
                    bonus = 0
                tmp = pyautogui.locateCenterOnScreen(image_path, region=(350, 857, 900, 400), confidence = rate - 0.015 + bonus)
                if tmp is not None:
                    print('我們決定出這張牌:' ,common_list[0])
                    pyautogui.moveTo(tmp)
                    pyautogui.click(tmp)
                    handcards.remove(common_list[0])
                    cardsonboard[index] = True 
                    if (index%13+1)  < 7 and index%13!=0:
                        cardyoucanplay[index-1]=True
                        if(card_names[index-1] not in playable_cards):
                            playable_cards.append(card_names[index-1])
                            print('新增:', card_names[index-1])
                    elif (index%13+1) > 7 and index%13!=12:
                        cardyoucanplay[index+1]=True
                        if(card_names[index+1] not in playable_cards):
                            playable_cards.append(card_names[index+1])
                            print('新增:', card_names[index+1])
                    elif index%13+1==7:
                        if(card_names[index-1] not in playable_cards):
                            playable_cards.append(card_names[index-1])
                            print('新增:', card_names[index-1])
                        if(card_names[index+1] not in playable_cards):
                            playable_cards.append(card_names[index+1])
                            print('新增:', card_names[index+1])
                        cardyoucanplay[index+1]=True
                        cardyoucanplay[index-1]=True
                    pyautogui.moveTo(300,300)
                else:
                    print('好像找不到欸')
            except pyautogui.ImageNotFoundException:
                print('找不到這張牌:', common_list[0])
                time.sleep(2.5)
        else: #蓋牌
            minimum = 100
            for i in handcards:
                index = card_names.index(i)
                if minimum > index%13: #餘數是0, 蓋的牌是A, 餘數是1, 蓋的牌是2 ...
                    minimum = index%13
                    idx = index
            print("蓋牌啦: ", card_names[idx])
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, "cards", card_names[idx] + '.png')
            try:    
                tmp = pyautogui.locateCenterOnScreen(image_path, region=(350, 857, 800, 400), confidence = 0.9375) #準確率
                if tmp is not None:
                    pyautogui.moveTo(tmp)
                    pyautogui.click(tmp)   
                    handcards.remove(card_names[idx])
                    pyautogui.moveTo(300,300)
                else:
                    print('找不到')
            except pyautogui.ImageNotFoundException:
                print('找不到這張要蓋的牌:', card_names[idx])
                time.sleep(2.5)
        print("手牌有:", handcards, '共:' , len(handcards), '張')
        for i in range(52):
            if cardyoucanplay[i] & (card_names[i] not in playable_cards):
                playable_cards.append(card_names[i])
        time.sleep(0.8)
    cnt+=1
    if(cnt==5):
        print('pause...')
        time.sleep(3)
        os.system('cls')
        print('Congrats, you\'ve already completed five games.')
    time.sleep(3.25)
    pyautogui.click(pyautogui.locateCenterOnScreen('OK.png', confidence=0.95))
    time.sleep(0.8)
    pyautogui.click(pyautogui.locateCenterOnScreen('again.png', confidence=0.9))
    time.sleep(0.6)
    pyautogui.click(pyautogui.locateCenterOnScreen('yes_button.png', confidence=0.9))


    #os.system('cls')
## index = card_names.index(target_card)
##  cardboard