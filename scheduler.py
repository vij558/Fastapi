from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import subprocess
import sys


scheduler = BlockingScheduler()


def run_analysis():
    print("\n==============================")
    print("Scheduled analysis started")
    print("Time:", datetime.now())

    subprocess.run([sys.executable, "analysis.py"])

    print("Scheduled analysis completed")
    print("==============================\n")


scheduler.add_job(
    run_analysis,
    "interval",
    minutes=1
)


print("Scheduler started. Waiting for jobs...")

scheduler.start()