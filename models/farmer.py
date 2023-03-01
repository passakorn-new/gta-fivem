import pydirectinput, time, pyautogui, pyperclip, subprocess
from constants import *
from models.coordinate import Coordinate

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

OPEATOR_ANIMAL_POS_X = [737, 867, 997, 1127, 1258]
OPERATOR_ANIMAL_POS_Y = 800

DEFAULT_COLOUR = (55, 55, 55)
GREEN_COLOUR = (0, 210, 140)
WHITE_COLOUR = (255, 255, 255)

class Farmer:
    COUNT_ANIMAL = Coordinate(1236, 725, 40, 20)
    IMG_TEMP_PATH = r'..\asset\temp_count_animal_test.png'

    def __init__(self, helper, name):
        subprocess.call(["shutdown", "/a"])
        self.total = 40
        self.animal_name = name
        self.feed_1 = ITEM_MILK_NAME
        self.feed_2 = ITEM_RICE_NAME if name == ITEM_CAT_NAME else ITEM_CORN_NAME
        self.helper = helper
        subprocess.call(["shutdown", "/s", "/t", f'{int(self.total / 5 * 20 * 60)}'])
        # self.animals = []
        # subprocess.call(["shutdown", "/a"])

    def auto_milk(self):
        pydirectinput.press('e')

    def auto_coca(self):
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
        time.sleep(2)
        pydirectinput.typewrite(['e', 'e', 'e', 'e'], interval=0.2)
        pydirectinput.leftClick(1099, 795)
        time.sleep(2)

        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        pyperclip.copy(self.animal_name)
        pyautogui.hotkey('ctrl', 'v')
        
        # drag to car
        pyautogui.moveTo(FIRST_ITEM_CAR_POS_X, FIRST_ITEM_CAR_POS_Y, 0.5)
        pyautogui.dragTo(FIRST_FIND_ITEM_CAR_POS_X, FIRST_FIND_ITEM_CAR_POS_Y, 1)

        # click max and confirm button
        pydirectinput.leftClick(AMOUNT_TEXT_INVENTORY_POS_X, AMOUNT_TEXT_INVENTORY_POS_Y)
        pydirectinput.typewrite('5')
        pydirectinput.leftClick(INVENTORY_CONFIRM_POS_X, INVENTORY_CONFIRM_POS_Y)
        
        # clear text search
        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        pyautogui.hotkey('ctrlleft', 'a', 'del')

        # take item!!!
        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        
        for item_name in [self.feed_1, self.feed_2]:
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
        
    def check_animal_success(self):
        animal_empty_pos = self.helper.find_img_in_screen(r'..\asset\empty_animal_slot.png', confidence=0.9)
        return animal_empty_pos != None
    
    def feed_animal(self):
        for index in range(5):
            pydirectinput.leftClick(ANIMAL_POS_X[index], ANIMAL_POS_Y)
            pydirectinput.leftClick(WATER_POS_X, WATER_POS_Y)

            pydirectinput.leftClick(ANIMAL_POS_X[index], ANIMAL_POS_Y)
            pydirectinput.leftClick(MILK_POS_X, MILK_POS_Y)

            pydirectinput.leftClick(ANIMAL_POS_X[index], ANIMAL_POS_Y)
            pydirectinput.leftClick(LOVE_POS_X, LOVE_POS_Y)

            time.sleep(1)
            pydirectinput.leftClick(ANIMAL_POS_X[index], 830)
                   
    def set_auto_farming(self):
        print("start..")
        print("total : ", self.total)
        if self.total <= 0:
            import subprocess
            subprocess.call(["shutdown", "/a"])
            time.sleep(3)
            subprocess.call(["shutdown", "/s"])
            exit()
        
        pydirectinput.press(FARM_MANAGER)
        time.sleep(1)
        self.buy_animal(times=5)

        while True:
            self.feed_animal()
            if self.check_animal_success():
                break

        time.sleep(3)
        self.total -= 5
        self.set_keep_and_take_item_in_car()
