import re
import pydirectinput
from constants import *
from models.coordinate import Coordinate

class Fisher:
    IMG_TEMP_PATH = r'C:\Users\newso\workspace\fivem\asset\temp_fishing.png'
    FISHING_CHAR_COORDINATE = Coordinate(
        FISHING_RANDOM_CHAR_POS_X,
        FISHING_RANDOM_CHAR_POS_Y,
        FISHING_RANDOM_CHAR_WIDTH,
        FISHING_RANDOM_CHAR_HEIGHT
    )

    def __init__(self, helper):
        self.helper = helper

    def set_auto_fishing(self):
        pydirectinput.press(ROD_FISH)
        charactor_finded = self.helper.detect_text_from_img(self.FISHING_CHAR_COORDINATE, self.IMG_TEMP_PATH, "--psm 10").lower()
        x = re.search(r"^[mefrckg]{1}$", charactor_finded)
        
        if x != None:
            print(f'DETECT {charactor_finded[0]} !!')
            pydirectinput.typewrite([charactor_finded[0], charactor_finded[0], charactor_finded[0], charactor_finded[0], charactor_finded[0]], interval=0.20)
