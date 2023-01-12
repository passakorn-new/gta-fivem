import cv2
import pytesseract
import pyautogui
from constants import *
from models.coordinate import Coordinate

class Helper:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD_PATH

    def __init__(self):
        pass

    def find_img_in_screen(self, img_path, confidence=0.8):
        position = pyautogui.locateOnScreen(img_path, confidence=confidence)
        return position

    def detect_text_from_img(self, coodinate, temp_path, config=None):
        im = pyautogui.screenshot(region=(coodinate.pos_x, coodinate.pos_y, coodinate.width, coodinate.height))
        im.save(temp_path)

        img = cv2.imread(temp_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return pytesseract.image_to_string(img, config=config)
