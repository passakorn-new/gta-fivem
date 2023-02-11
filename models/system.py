import pyautogui, os, pyperclip, time
from constants import *

class System:
    def __init__(self, helper):
        self.helper = helper
        pass

    def makedirs(self, path):
        try:
            os.makedirs(path)
        except FileExistsError:
            print("Directory already exists")

    def take_screenshot(self, img_name, img_path, region=None):
        screenshot = pyautogui.screenshot(region=region)
        path_to_save_img = f"{img_path}\\{img_name}.png"
        screenshot.save(path_to_save_img)

    def type(self, key, presses=1):
        pyautogui.press(key, presses=presses, interval=0.1)

    def tab(self, times=1):
        for _ in range(times):
            pyautogui.press('tab')

    def search_text(self, text):
        pyautogui.hotkey('ctrl', 'f')
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')

    def copy_text_to_clipboard(self, text):
        print(text)
        pyperclip.copy(text)

    def write_text(self, text):
        pyperclip.copy(text)
        print(text)
        pyautogui.hotkey('ctrl', 'v')

    def click_by_position(self, position):
        x, y = pyautogui.center(position)
        pyautogui.click(x, y)

    def back_previous_page(self):
        pyautogui.hotkey('alt', 'left')
    
    def mouse_scroll_down(self):
        pyautogui.scroll(-200)

