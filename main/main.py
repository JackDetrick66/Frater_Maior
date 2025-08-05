from db import init_db, add_site, list_sites, remove_site, toggle_monitor_on, toggle_monitor_off, view_logs
from pyfiglet import Figlet
import threading
from db import init_db
from watcher import start_watching

def print_sites():


    sites = list_sites()
    print("Sites:")
    for site in sites:
        if site[2]: status = "ACTIVE"
        else: status = "INACTIVE"
        print(f"Site ID: {site[0]}. {site[1]} is ({status}) ")
    

def run():
    init_db()
    f = Figlet(font='colossal')
    print(f.renderText("FRATER MAIOR\n"))
    print_sites()
    
    spy_watching = False
    
    while True:
        print("\n1. Add Site\n2. Remove Site\n3. Toggle Monitor On\n4 Toggle Monitor Off\n5. List Sites\n6. Start Monitoring\n7. Exit Monitor\n8. View Logs")
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
            print_sites()
        elif choice == "6":
            if spy_watching:
                print("Monitoring is already in progress.")
            else:
                # daemon means that it won't prevent the program from closing when the main thread is closed
                spy = threading.Thread(target=start_watching, daemon=True)
                spy.start() #<- THIS RUNS IT AS A SEPARATE THREAD
                #spy.run() <- THIS RUNS IT IN THE MAIN THREAD
                print("Background monitoring started.")
                spy_watching = True
        elif choice == "7":
            break
        elif choice == "8":
            siteID = input("Please provide the site id: ")
            loggers = (view_logs(siteID))
            for log in loggers:
                if log[0] == "200":
                    print(f"The site was ACTIVE at {log[1]}")
                else:
                    print(f"The site returned {log[0]} at {log[1]}.")


if __name__ == "__main__":
    run()