import sys
sys.path.insert(0, '..')

from models.helper import Helper
from models.farmer import Farmer
from constants import *
import schedule

scheduler = schedule.Scheduler()
helper = Helper()
farmer = Farmer(helper=helper)

scheduler.every(1).seconds.do(farmer.auto_milk).tag('milk')

while True:
    scheduler.run_pending()