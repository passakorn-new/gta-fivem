import pydirectinput, time, pyautogui, pyperclip
from constants import *

BUY_ANIMAL_POS_X = 690
BUY_ANIMAL_POS_Y = 735

WATER_POS_X = 865
WATER_POS_Y = 600

MILK_POS_X = 960
MILK_POS_Y = 600

LOVE_POS_X = 1055
LOVE_POS_Y = 600

ANIMAL_POS_X = [696, 828, 959, 1090, 1222]
ANIMAL_POS_Y = 770

OPEATOR_ANIMAL_POS_X = [737, 867, 997, 1127, 1257]
OPERATOR_ANIMAL_POS_Y = 800

DEFAULT_COLOUR = (55, 55, 55)
GREEN_COLOUR = (0, 210, 140)
WHITE_COLOUR = (255, 255, 255)

class Farmer:
    def __init__(self, helper):
        self.total = 30
        self.helper = helper
        self.animals = []

    def auto_milk(self):
        pydirectinput.press('e')

    def buy_animal(self, times=1):
        for _ in range(times):
            pydirectinput.leftClick(BUY_ANIMAL_POS_X, BUY_ANIMAL_POS_Y)
            time.sleep(2)
    
    def set_eat_and_drink_scheduler(self):
        pydirectinput.press(FOOD_KEYBIND)
        time.sleep(30)
        pydirectinput.press(DRINK_KEYBIND)
        time.sleep(20)  

    def set_keep_and_take_item_in_car(self):
        pydirectinput.press('esc')
        time.sleep(1)
        pydirectinput.typewrite(['e', 'e', 'e'], interval=0.2)
        pydirectinput.leftClick(1099, 795)
        time.sleep(2)

        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        pyperclip.copy(ITEM_CAT_NAME)
        pyautogui.hotkey('ctrl', 'v')
        
        # drag to car
        pyautogui.moveTo(FIRST_ITEM_CAR_POS_X, FIRST_ITEM_CAR_POS_Y, 0.5)
        pyautogui.dragTo(FIRST_FIND_ITEM_CAR_POS_X, FIRST_FIND_ITEM_CAR_POS_Y, 1)

        # click max and confirm button
        pydirectinput.leftClick(AMOUNT_TEXT_INVENTORY_POS_X, AMOUNT_TEXT_INVENTORY_POS_Y)
        pydirectinput.typewrite('5')
        pydirectinput.leftClick(INVENTORY_CONFIRM_POS_X, INVENTORY_CONFIRM_POS_Y)
        
        # pydirectinput.leftClick(INVENTORY_MAX_POS_X, INVENTORY_MAX_POS_Y)
        # pydirectinput.leftClick(INVENTORY_CONFIRM_POS_X, INVENTORY_CONFIRM_POS_Y)
        
        # clear text search
        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        pyautogui.hotkey('ctrlleft', 'a', 'del')

        # take item!!!
        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        
        for item_name in [ITEM_RICE_NAME, ITEM_MILK_NAME]:
            pyperclip.copy(item_name)
            pyautogui.hotkey('ctrl', 'v')
            
            # drag to bag 
            pyautogui.moveTo(FIRST_FIND_ITEM_CAR_POS_X, FIRST_FIND_ITEM_CAR_POS_Y, 0.5)
            pyautogui.dragTo(FIRST_ITEM_CAR_POS_X, FIRST_ITEM_CAR_POS_Y, 1)

            # click amount box and fill number confirm
            pydirectinput.leftClick(AMOUNT_TEXT_INVENTORY_POS_X, AMOUNT_TEXT_INVENTORY_POS_Y)
            pydirectinput.typewrite('13')
            pydirectinput.leftClick(INVENTORY_CONFIRM_POS_X, INVENTORY_CONFIRM_POS_Y)
            
            # clear text search
            pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
            pyautogui.hotkey('ctrlleft', 'a', 'del')

        pydirectinput.press('esc')
        
    
    def feed_animal(self, index):
        # fix case delete index
        if index >= len(self.animals):
            return

        if pyautogui.pixelMatchesColor(OPEATOR_ANIMAL_POS_X[index], OPERATOR_ANIMAL_POS_Y, DEFAULT_COLOUR) == False:
            if self.animals[index] < 4:
                print(f"feeded {index + 1}")
                self.animals[index] += 1
                pydirectinput.leftClick(ANIMAL_POS_X[index], ANIMAL_POS_Y)
                pydirectinput.leftClick(WATER_POS_X, WATER_POS_Y)

                pydirectinput.leftClick(ANIMAL_POS_X[index], ANIMAL_POS_Y)
                pydirectinput.leftClick(MILK_POS_X, MILK_POS_Y)

                pydirectinput.leftClick(ANIMAL_POS_X[index], ANIMAL_POS_Y)
                pydirectinput.leftClick(LOVE_POS_X, LOVE_POS_Y)

                # keep
                time.sleep(1)
                print((self.animals[index]), " ::: round")
                if self.animals[index] == 4:
                    print(f"taked {index + 1}")
                    pydirectinput.leftClick(ANIMAL_POS_X[index], 830)
                    del self.animals[index]
                    time.sleep(1)
        else:
            print(pyautogui.pixel(OPEATOR_ANIMAL_POS_X[index], OPERATOR_ANIMAL_POS_Y), ":: color not match")
                   
    def set_auto_farming(self):
        print("start..")
        print("total : ", self.total)
        if self.total <= 0:
            import subprocess
            subprocess.call(["shutdown", "/s"])
            exit()
        
        pydirectinput.press(FARM_MANAGER)
        time.sleep(1)
        self.buy_animal(times=5)
        self.animals = [0, 0, 0, 0, 0]

        while len(self.animals) > 0:
            print(len(self.animals), " ::: len")
            print(self.animals)
            time.sleep(1)
            for index in range(len(self.animals)):
                self.feed_animal(index)

        time.sleep(3)
        self.set_keep_and_take_item_in_car()
        self.total -= 5
