import sys, time, pyautogui, pyperclip, os
sys.path.insert(0, '..')

from pathlib import Path
from models.browser import Browser
from models.helper import Helper
from models.system import System
from datetime import datetime
from tkinter import messagebox

# COMPAT ONLY WINDOWN 10
GROUPS_PROMOTE_ID = [
    '255834148328219', #https://www.facebook.com/groups/255834148328219/
    '686633655307229', #https://www.facebook.com/groups/686633655307229/
    '364167337464759', #https://www.facebook.com/groups/364167337464759/
    '289008456634964', #https://www.facebook.com/groups/289008456634964/
    '626366348241524', #https://www.facebook.com/groups/626366348241524/
    '793534421289727', #https://www.facebook.com/groups/793534421289727/
    '163451981054318', #https://www.facebook.com/groups/163451981054318/
]
163451981054318
helper = Helper()
system = System(helper=helper)
chrome = Browser(
    web_browser='chrome',
    path_to_browser_exec='C://Program Files//Google//Chrome//Application//chrome.exe'
)

CONTENT = 'มาเล่นกันจ้า \n#athenatown #athena #townที่ดีที่สุด\n DC : https://discord.gg/athenatown'
DIRECTORY_SCREENSHOT = f"{Path.home()}/screenshot-fivem"
SCREENSHOT_NAME = datetime.now().strftime("%d-%m-%Y")
RECENTLY_POST_LINK = f"https://www.facebook.com/me/allactivity?activity_history=false&category_key=GROUPPOSTS&manage_mode=false&should_load_landing_page=false"

try:
    # First ScreenShot
    if messagebox.askyesno("Take ScreenShot", "Press Enter to confirm...?"):
        time.sleep(2)
        system.makedirs(DIRECTORY_SCREENSHOT)
        active_window = pyautogui.getActiveWindow()
        left, top, right, bottom = active_window.left, active_window.top, active_window.right, active_window.bottom
        trim_right_window = right - left
        trim_bottom_window = bottom - top
        system.take_screenshot(SCREENSHOT_NAME, DIRECTORY_SCREENSHOT, region=(left, top, trim_right_window, trim_bottom_window))
    else:
        exit()

    # Post to groups
    for group_id in GROUPS_PROMOTE_ID:   
        chrome.open_link(f'https://www.facebook.com/groups/{group_id}')
        time.sleep(5)

        system.search_text('เขียนอะไรสักหน่อย....')
        system.type('esc')
        system.type('enter')
        time.sleep(2)

        system.write_text(CONTENT)
        attach_img_icon_pos = helper.find_img_in_screen(r'..\asset\fb-attach-img.png', confidence=0.8, gray_scale=True)
        system.click_by_position(attach_img_icon_pos)
        system.search_text('เพิ่มรูปภาพ/วิดีโอ')
        system.type('esc')
        system.type('enter')

        tab_to_search_box = system.tab(5)
        system.type('enter')
        system.write_text(DIRECTORY_SCREENSHOT)
        system.type('enter', presses=4)
        system.write_text(SCREENSHOT_NAME)
        system.type('enter')

        post_btn_img = helper.find_img_in_screen(r'..\asset\fb-post-btn.png', confidence=0.6)
        if messagebox.askyesno("Confirmation", "Press Enter to Post...?"):
            system.click_by_position(post_btn_img)
        else:
            exit()

    # # Capture posted
    time.sleep(10)
    chrome.open_link(RECENTLY_POST_LINK)
    time.sleep(5)

    for index in range(5):
        print(CONTENT.split()[0])
        system.search_text(CONTENT.split()[0])
        system.type('enter', presses=index)
        system.type('esc')
        system.type('enter')
        time.sleep(3)
        system.mouse_scroll_down()
        time.sleep(1)
        system.take_screenshot(f"{SCREENSHOT_NAME}-confirm-{index + 1}", DIRECTORY_SCREENSHOT)
        system.back_previous_page()
        time.sleep(2)

    # Post Story
    chrome.open_link('https://www.facebook.com/')
    time.sleep(3)

    system.search_text('สร้างสตอรี่')
    system.type('esc')
    system.type('enter')
    time.sleep(2)

    system.search_text('สร้างสตอรี่รูปภาพ')
    system.type('esc')
    system.type('enter')
    time.sleep(2)

    tab_to_search_box = system.tab(5)
    system.type('enter')
    system.write_text(DIRECTORY_SCREENSHOT)
    system.type('enter', presses=4)
    system.write_text(SCREENSHOT_NAME)
    system.type('enter')
    time.sleep(2)

    system.search_text('เพิ่มข้อความ')
    system.type('esc')
    system.type('enter')
    time.sleep(2)

    system.write_text(CONTENT)
    system.type('enter', presses=10)
    system.type('esc')
    time.sleep(3)

    system.search_text('แชร์ไปยังสตอรี่')
    system.type('enter')
    system.type('esc')
    system.type('enter')

    system.search_text('สตอรี่ของคุณ')
    system.type('enter')
    system.type('esc')
    system.type('enter')

    success_time = datetime.now().strftime("%d-%m-%Y %H:%M")
    DISCORD_MESSAGE = f"- ไอดี : xxx\n - ชื่อ IC : Amorn Roy\n - วันและเวลาที่ทำกิจกรรม: {success_time}\n - รูปภาพหลักฐาน: "
    system.copy_text_to_clipboard(DISCORD_MESSAGE)
except KeyboardInterrupt:
    print("Script cancelled by user")
finally:
    exit()
