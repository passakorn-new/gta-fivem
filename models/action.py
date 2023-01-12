import re
import pydirectinput
import time
from constants import *
import pyautogui

class Action:
    SEARCH_BOX_IMG_PATH = r'C:\Users\newso\workspace\fivem\asset\search_item.png'
    REMOVE_CAR_IMG_PATH = r'C:\Users\newso\workspace\fivem\asset\remove_car.png'

    def __init__(self, helper):
        self.helper = helper

    def switch_lang(self):
       pyautogui.hotkey('win', 'space')

    def cancel_current_action(self, delay=10):
        pydirectinput.typewrite(['x', 'x', 'x', 'x', 'x', 'x'], interval=0.20)
        time.sleep(delay)

    def set_eat_and_drink_scheduler(self):
        print("set_eat_and_drink_scheduler")
        self.cancel_current_action()
        pydirectinput.press(FOOD_KEYBIND)
        time.sleep(10)
        pydirectinput.press(DRINK_KEYBIND)
        time.sleep(10)  

    def set_drop_item(self, item_name_list):
        print("set_drop_item")
        self.cancel_current_action()
        pydirectinput.press(OPEN_INVENTORY)
        time.sleep(2)

        # click search box and switch to thai lang
        pydirectinput.leftClick(SEARCH_INVENTORY_POS_X, SEARCH_INVENTORY_POS_Y)
        self.switch_lang()

        for item_name in item_name_list:
            pydirectinput.typewrite(list(item_name))
            
            # drag to bin 
            pyautogui.moveTo(FIRST_ITEM_POS_X, FIRST_ITEM_POS_Y, 0.2)
            pyautogui.dragTo(INVENTORY_BIN_POS_X, INVENTORY_BIN_POS_Y, 1)

            # click max and confirm button
            pydirectinput.leftClick(INVENTORY_MAX_POS_X, INVENTORY_MAX_POS_Y)
            pydirectinput.leftClick(INVENTORY_CONFIRM_POS_X, INVENTORY_CONFIRM_POS_Y)
            
            # clear text search
            pydirectinput.leftClick(780, 300)
            pyautogui.hotkey('ctrlleft', 'a', 'del')
        
        self.switch_lang()
        pydirectinput.press('esc')

    def set_keep_item_in_car(self, item_name_list):
        print("set_keep_item_in_car")
        self.cancel_current_action(delay=15)
        pydirectinput.press('s')
        time.sleep(5)
        pydirectinput.press(UNLOCK_CAR)
        time.sleep(2)
        pydirectinput.press(OPEN_CAR_INVENTORY)
        time.sleep(2)

        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        self.switch_lang()
        
        for item_name in item_name_list:
            pydirectinput.typewrite(list(item_name))
            
            # drag to car
            pyautogui.moveTo(FIRST_ITEM_CAR_POS_X, FIRST_ITEM_CAR_POS_Y, 0.5)
            pyautogui.dragTo(FIRST_FIND_ITEM_CAR_POS_X, FIRST_FIND_ITEM_CAR_POS_Y, 1)

            # click max and confirm button
            pydirectinput.leftClick(INVENTORY_MAX_POS_X, INVENTORY_MAX_POS_Y)
            pydirectinput.leftClick(INVENTORY_CONFIRM_POS_X, INVENTORY_CONFIRM_POS_Y)
            
            # clear text search
            pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
            pyautogui.hotkey('ctrlleft', 'a', 'del')
        
        self.switch_lang()
        pydirectinput.press('esc')
        pydirectinput.press(UNLOCK_CAR)

    def set_take_item_in_car(self, item_name_dict):
        print("set_take_item_in_car")
        self.cancel_current_action(delay=15)
        pydirectinput.press('s')
        time.sleep(5)
        pydirectinput.press(UNLOCK_CAR)
        time.sleep(2)
        pydirectinput.press(OPEN_CAR_INVENTORY)
        time.sleep(2)

        pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
        self.switch_lang()
        
        for item_name in item_name_dict:
            pydirectinput.typewrite(list(item_name))
            
            # drag to bag 
            pyautogui.moveTo(FIRST_FIND_ITEM_CAR_POS_X, FIRST_FIND_ITEM_CAR_POS_Y, 0.5)
            pyautogui.dragTo(FIRST_ITEM_CAR_POS_X, FIRST_ITEM_CAR_POS_Y, 1)

            # click amount box and fill number confirm
            pydirectinput.leftClick(AMOUNT_TEXT_INVENTORY_POS_X, AMOUNT_TEXT_INVENTORY_POS_Y)
            self.switch_lang()
            pydirectinput.typewrite(list(item_name_dict[item_name]), interval=0.2)
            self.switch_lang()
            pydirectinput.leftClick(INVENTORY_CONFIRM_POS_X, INVENTORY_CONFIRM_POS_Y)
            
            # clear text search
            pydirectinput.leftClick(SEARCH_CAR_INVENTORY_POS_X, SEARCH_CAR_INVENTORY_POS_Y)
            pyautogui.hotkey('ctrlleft', 'a', 'del')

        self.switch_lang()
        pydirectinput.press('esc')
        pydirectinput.press(UNLOCK_CAR)

    def keep_milk(self):
        pydirectinput.press('e')