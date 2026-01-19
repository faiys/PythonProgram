from apscheduler.schedulers.background import BackgroundScheduler
import time

def test(add):
    sum = 5+add
    print("Result:", sum)

schedule = BackgroundScheduler()
schedule.add_job(test, 'interval', seconds=10, args=[5], id="testid")

schedule.start()

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemError):
    schedule.shutdown()
