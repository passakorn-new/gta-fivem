import pydirectinput
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

class Farmer:

    def __init__(self, helper):
        self.helper = helper

    def set_auto_farming(self):
        pydirectinput.press(FARM_MANAGER)

        for index in range(5):
            pydirectinput.leftClick(BUY_ANIMAL_POS_X, BUY_ANIMAL_POS_Y)

            pydirectinput.leftClick(ANIMAL_POS_X[index], ANIMAL_POS_Y)
            pydirectinput.leftClick(WATER_POS_X, WATER_POS_Y)

            pydirectinput.leftClick(ANIMAL_POS_X[index], ANIMAL_POS_Y)
            pydirectinput.leftClick(MILK_POS_X, MILK_POS_Y)

            pydirectinput.leftClick(ANIMAL_POS_X[index], ANIMAL_POS_Y)
            pydirectinput.leftClick(LOVE_POS_X, LOVE_POS_Y)