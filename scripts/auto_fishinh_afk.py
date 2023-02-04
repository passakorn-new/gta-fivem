import sys
sys.path.insert(0, '..')

from models.helper import Helper
from models.fisher import Fisher
from models.action import Action
from constants import *
import schedule
import pyautogui

scheduler = schedule.Scheduler()
helper = Helper()

fisher = Fisher(helper=helper)
action = Action(helper=helper)

scheduler.every(1).seconds.do((fisher.set_auto_fishing_afk)).tag('fishing_afk')
scheduler.every(20).minutes.do(action.set_keep_item_in_car, [ITEM_SALMON_NAME]).tag('item_keep')
scheduler.every(20).minutes.do(action.set_take_item_in_car, {ITEM_FISHING_BAIT_NAME: '80'}).tag('item_take')
scheduler.every(40).minutes.do(action.set_eat_and_drink_scheduler).tag('food')

while True:
    scheduler.run_pending()