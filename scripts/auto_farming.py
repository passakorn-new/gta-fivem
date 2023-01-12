import sys
sys.path.insert(0, '..')

from models.helper import Helper
from models.farmer import Farmer
from models.action import Action
from constants import *
import schedule

# Prepare
scheduler = schedule.Scheduler()
helper = Helper()

action = Action(helper=helper)
farmer = Farmer(helper=helper)

scheduler.every(1).seconds.do(farmer.set_auto_farming).tag('farming')
scheduler.every(4).minutes.do(action.set_keep_item_in_car, [ITEM_CAT_NAME]).tag('item_keep')
scheduler.every(4).minutes.do(action.set_take_item_in_car, {ITEM_FISHING_BAIT_NAME: '12'}).tag('item_take')

while True:
    scheduler.run_pending()