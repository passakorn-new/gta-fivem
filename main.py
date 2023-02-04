from models.helper import Helper
from models.fisher import Fisher
from models.action import Action
from constants import *
import schedule

# Prepare
scheduler = schedule.Scheduler()
helper = Helper()

fisher = Fisher(helper=helper)
action = Action(helper=helper)

scheduler.every(1).seconds.do(fisher.set_auto_fishing).tag('fishing')
scheduler.every(10).minutes.do(action.set_keep_item_in_car, [ITEM_OCTOPUS_NAME, ITEM_TUNA_NAME]).tag('item_keep')
# scheduler.every(15).minutes.do(action.set_drop_item, [ITEM_JUNK_NAME]).tag('item_drop')
scheduler.every(18).minutes.do(action.set_take_item_in_car, {ITEM_FISHING_BAIT_NAME: '90'}).tag('item_take')
scheduler.every(40).minutes.do(action.set_eat_and_drink_scheduler).tag('food')

while True:
    scheduler.run_pending()