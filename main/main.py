from db import init_db, add_site, list_sites, remove_site, toggle_monitor_on, toggle_monitor_off
from pyfiglet import Figlet
import requests
import schedule
import time
from datetime import datetime

def print_sites():

    f = Figlet(font='colossal')
    print(f.renderText("FRATER MAIOR\n"))
    sites = list_sites
    print("Sites:")
    for site in sites:
        if site[2]: status = "ACTIVE"
        else: status = "INACTIVE"
        print(f"{site[0]}. {site[1]} is ({status}) ")
    

def run():
    init_db()
    while True:
        print("\n1. Add Site\n2. Remove Site\n3. Toggle Monitor On\n4 Toggle Monitor Off\n5. List Sites\n6. Exit Monitor")
        choice = input("Make a choice: ")
        
        if choice == "1":
            siteURL = input("\nPlease provide the URL of the website you wish to monitor: ")
            interval = input("\nHow often would you like to check this website? (minutes, default 20): ")
            #add the site, takes user input as the interval, checks if there is a "true" value (>0), otherwise use 5 minutes
            add_site(siteURL, int(interval) if interval else 20)
        elif choice == "2":
            siteURL = input("\nPlease provide the URL of the website you wish to remove from the list: ")
            remove_site(siteURL)
        elif choice == "3":
            siteURL = input("\nPlease provide the URL of the website you wish to begin monitoring: ")
            toggle_monitor_on(siteURL)
        elif choice == "4":
            siteURL = input("\nPlease provide the URL of the website you wish to stop monitoring: ")
            toggle_monitor_off(siteURL)
        elif choice == "5":
            print_sites
        elif choice == "6":
            break
        


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