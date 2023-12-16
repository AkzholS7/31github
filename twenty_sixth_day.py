#!/usr/bin/env C:\Users\user\AppData\Local\Programs\Python\Python311\python.exe

from crontab import CronTab

def create_cron_job():
    # Create a new cron job
    cron = CronTab(user=True)  # Use user=True for the current user's cron tab

    # Add a new job to the cron tab
    job = cron.new(command='python /path/to/your_script.py')

    # Set the schedule for the job (every day at 3 AM)
    job.minute.on(0)
    job.hour.on(3)

    # Write the job to the cron tab
    cron.write()

if __name__ == "__main__":
    create_cron_job()
