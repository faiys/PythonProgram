import schedule

def add():
    print("Run")

schedule.every(3).seconds.do(add)

while True:
    schedule.run_pending()