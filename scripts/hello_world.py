import sys
sys.path.insert(0, '..')

from models.helper import Helper
from models.farmer import Farmer
from constants import *
import schedule

# Prepare
scheduler = schedule.Scheduler()
helper = Helper()

farmer = Farmer(helper=helper, name=ITEM_CAT_NAME)

scheduler.every(5).seconds.do(farmer.set_auto_farming).tag('farming')
scheduler.every(40).minutes.do(farmer.set_eat_and_drink_scheduler).tag('food')

while True:
    scheduler.run_pending()