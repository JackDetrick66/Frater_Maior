from db import grab_monitor, update_log
import requests
import time
from datetime import datetime, timedelta
last_check = {}

def start_watching():
    while(True):
        currWatching = grab_monitor()
        for i in currWatching:
            if i[0] not in last_check:
                last_check[i[0]] = datetime.now()

            if datetime.now() - last_check[i[0]] >= timedelta(minutes=i[1]):
                try:
                    r = requests.get(i[2])
                    status = r.status_code
                except requests.exceptions.RequestException:
                    status = "Error" 
                finally:
                    update_log(i[0], status, datetime.now())
                    last_check[i[0]] = datetime.now()
        time.sleep(1)
