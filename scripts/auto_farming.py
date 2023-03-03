import sys, time
sys.path.insert(0, '..')

from models.helper import Helper
from models.farmer import Farmer
from constants import *
import schedule
import tkinter as tk
from tkinter import messagebox

def start_farming():
    try:
        helper = Helper()
        total = int(amount.get())
        farmer = Farmer(helper=helper, name=ITEM_CAT_NAME, total=total, is_shutdown=is_shutdown.get())
        scheduler.every(5).seconds.do(farmer.set_auto_farming).tag('farming')
        scheduler.every(40).minutes.do(farmer.set_eat_and_drink_scheduler).tag('food')
        window.destroy()
    except ValueError:
        messagebox.showerror(title=None, message='ใส่เลขไอโง่')

# Prepare
window = tk.Tk()
window.title('Auto Farm')
window.geometry('250x100')

scheduler = schedule.Scheduler()
is_shutdown = tk.BooleanVar()

amount_label = tk.Label(window, text = "Enter amount: ")
amount_label.grid(row = 1, column = 0)
amount = tk.Entry(window)
amount.grid(row = 1, column = 1)

cb_shutdown = tk.Checkbutton(window, text='shutdown?',variable=is_shutdown, onvalue=True, offvalue=False)
cb_shutdown.grid(row = 3, column = 1)

confirm_button = tk.Button(window, text="Start", command=start_farming, width=10)
confirm_button.grid(row = 4, column = 1)
window.mainloop()

while True:
    scheduler.run_pending()
    