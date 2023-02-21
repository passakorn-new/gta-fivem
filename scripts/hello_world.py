import sys
sys.path.insert(0, '..')

from models.helper import Helper
from models.farmer import Farmer
from constants import *
import schedule
import pyautogui
# Prepare
scheduler = schedule.Scheduler()
helper = Helper()

farmer = Farmer(helper=helper, name=ITEM_CAT_NAME)

# scheduler.every(3).seconds.do(farmer.auto_milk).tag('milk')
scheduler.every(5).seconds.do(farmer.set_auto_farming).tag('farming')
scheduler.every(40).minutes.do(farmer.set_eat_and_drink_scheduler).tag('food')
pyautogui.mouseInfo()

while True:
    scheduler.run_pending()