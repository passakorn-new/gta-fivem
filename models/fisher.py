import re, time, pyperclip, pyautogui
import pydirectinput
from constants import *
from models.coordinate import Coordinate

class Fisher:
    IMG_TEMP_PATH = r'..\asset\temp_fishing.png'
    FISHING_CHAR_COORDINATE = Coordinate(
        FISHING_RANDOM_CHAR_POS_X,
        FISHING_RANDOM_CHAR_POS_Y,
        FISHING_RANDOM_CHAR_WIDTH,
        FISHING_RANDOM_CHAR_HEIGHT
    )

    def __init__(self, helper):
        self.helper = helper

    def cancel_current_action(self, delay=10):
        pydirectinput.typewrite(['x', 'x', 'x', 'x', 'x', 'x'], interval=0.20)
        time.sleep(delay)

    def set_eat_and_drink_scheduler(self, delay=2):
        print("set_eat_and_drink_scheduler")
        self.cancel_current_action(delay=15)
        pydirectinput.press(FOOD_KEYBIND)
        time.sleep(30)
        pydirectinput.press(DRINK_KEYBIND)
        time.sleep(20)  


    def set_auto_fishing(self):
        pydirectinput.press(ROD_FISH)
        charactor_finded = self.helper.detect_text_from_img(self.FISHING_CHAR_COORDINATE, self.IMG_TEMP_PATH, "--psm 10").lower()
        x = re.search(r"^[mefrckg]{1}$", charactor_finded)
        
        if x != None:
            print(f'DETECT {charactor_finded[0]} !!')
            pydirectinput.typewrite([charactor_finded[0], charactor_finded[0], charactor_finded[0], charactor_finded[0]], interval=0.10)

    def set_auto_fishing_afk(self):
        pydirectinput.press(ROD_FISH)

    def set_keep_item_in_car(self, item_name_list):
        print("set_keep_item_in_car")
        self.cancel_current_action(delay=15)

        pydirectinput.press(UNLOCK_CAR)
        time.sleep(2)
        pydirectinput.press(OPEN_CAR_INVENTORY)
        time.sleep(2)

        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        
        for item_name in item_name_list:
            pyperclip.copy(item_name)
            pyautogui.hotkey('ctrl', 'v')
            
            # drag to car
            pyautogui.moveTo(FIRST_ITEM_CAR_POS_X, FIRST_ITEM_CAR_POS_Y, 0.5)
            pyautogui.dragTo(FIRST_FIND_ITEM_CAR_POS_X, FIRST_FIND_ITEM_CAR_POS_Y, 1)

            # click max and confirm button
            pydirectinput.leftClick(INVENTORY_MAX_POS_X, INVENTORY_MAX_POS_Y)
            pydirectinput.leftClick(INVENTORY_CONFIRM_POS_X, INVENTORY_CONFIRM_POS_Y)
            
            # clear text search
            pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
            pyautogui.hotkey('ctrlleft', 'a', 'del')
        
        pydirectinput.press('esc')
        pydirectinput.press(UNLOCK_CAR)

    def set_take_item_in_car(self, item_name_dict):
        print("set_take_item_in_car")
        self.cancel_current_action(delay=15)

        pydirectinput.press(UNLOCK_CAR)
        time.sleep(2)
        pydirectinput.press(OPEN_CAR_INVENTORY)
        time.sleep(2)

        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        
        for item_name in item_name_dict:
            pyperclip.copy(item_name)
            pyautogui.hotkey('ctrl', 'v')
            
            # drag to bag 
            pyautogui.moveTo(FIRST_FIND_ITEM_CAR_POS_X, FIRST_FIND_ITEM_CAR_POS_Y, 0.5)
            pyautogui.dragTo(FIRST_ITEM_CAR_POS_X, FIRST_ITEM_CAR_POS_Y, 1)

            # click amount box and fill number confirm
            pydirectinput.leftClick(AMOUNT_TEXT_INVENTORY_POS_X, AMOUNT_TEXT_INVENTORY_POS_Y)
            pydirectinput.typewrite(list(item_name_dict[item_name]), interval=0.2)
            pydirectinput.leftClick(INVENTORY_CONFIRM_POS_X, INVENTORY_CONFIRM_POS_Y)
            
            # clear text search
            pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
            pyautogui.hotkey('ctrlleft', 'a', 'del')

        pydirectinput.press('esc')
        pydirectinput.press(UNLOCK_CAR)
