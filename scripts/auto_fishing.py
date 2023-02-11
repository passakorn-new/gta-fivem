import sys, time
sys.path.insert(0, '..')

from models.helper import Helper
from models.fisher import Fisher
from constants import *
import schedule
import pyautogui

# Prepare
# pyautogui.mouseInfo()
scheduler = schedule.Scheduler()
helper = Helper()

fisher = Fisher(helper=helper)

scheduler.every(1).seconds.do(fisher.set_auto_fishing).tag('fishing')
scheduler.every(15).minutes.do(fisher.set_keep_item_in_car, [ITEM_OCTOPUS_NAME, ITEM_TUNA_NAME, ITEM_JUNK_NAME]).tag('item_keep')
scheduler.every(40).minutes.do(fisher.set_eat_and_drink_scheduler).tag('food')
# scheduler.every(15).minutes.do(action.set_take_item_in_car, {ITEM_FISHING_BAIT_NAME: '50'}).tag('item_take')
# scheduler.every(20).minutes.do(action.set_drop_item, [ITEM_JUNK_NAME]).tag('item_drop')

while True:
    scheduler.run_pending()
    time.sleep(1)