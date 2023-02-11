import cv2
import pytesseract
import pyautogui
import numpy as np

from constants import *

class Helper:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD_PATH

    def __init__(self):
        pass

    def find_img_in_screen(self, img_path, confidence=0.8, gray_scale=False):
        try:
            if gray_scale:
                original_img = cv2.imread(img_path)
                gray_image = cv2.cvtColor(np.array(original_img), cv2.COLOR_RGB2GRAY)
                img_path = f'{img_path}-gray'
                cv2.imwrite(img_path, gray_image)

            position =pyautogui.locateOnScreen(img_path, confidence=confidence)
            print("Image found at", position)
        except pyautogui.ImageNotFoundException:
            print("Image not found on screen")
        return position

    def detect_text_from_img(self, coodinate, temp_path, config=None):
        im = pyautogui.screenshot(region=(coodinate.pos_x, coodinate.pos_y, coodinate.width, coodinate.height))
        im.save(temp_path)

        img = cv2.imread(temp_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return pytesseract.image_to_string(img, config=config)
