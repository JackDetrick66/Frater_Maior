import requests
import schedule
import time
from datetime import datetime


now = datetime.now()
print("Date and Time of initiation: ", now)
print("We're operational...")
def job():
    print("Monitoring...")
    ani_check = requests.get('https://9animetv.to/')
    mang_check = requests.get('https://mangadex.org/')
    print(ani_check.url)
    print(ani_check.status_code)
    print(mang_check.url)
    print(mang_check.status_code)

schedule.every(2).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)