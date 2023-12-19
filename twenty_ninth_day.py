#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

import schedule
import time

def remind():
    print("Don't forget to take a break and stretch!")

# Schedule a reminder every day at a specific time
schedule.every().day.at("10:00").do(remind)

# Infinite loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
