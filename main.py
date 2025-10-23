
import time
import os
import msvcrt

# func imported from other files
from monitoring import start_monitoring, list_status, get_monitoring
from larm import larm_menu, larm_build,get_larm ,controll 
#makes the program more clean, errase text that's not relevant 
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#give information about monotoring, updates every 2 sec  
def start_monitoring_2():
    print("Monotoring started.")
    try:
        while True:
            cpu, ram, disk = get_monitoring()
            print(f"Active")
            print(f"CPU: {cpu}%  RAM: {ram}%  Disk: {disk}%")

            larm_messages = controll  (cpu, ram, disk)
            for message in larm_messages:
                print(message)

            print("Update: 2 sec")
            print("==PRESS ENTER TO RETURN==")
            

            #controll if button have been pressed
            if msvcrt.kbhit():
                msvcrt.getch()
                break

            time.sleep(2)
    except KeyboardInterrupt:
        print("Monitoring interrupted.")

#first menu, when you start the program
def menu():
    while True:
        clear()
        print("==== MONITORING ====")
        print("1. Start monitoring")
        print("2. List active monitoring")
        print("3. Larm menu")
        print("4. Show larm")
        print("5. Start monitoring 2.0")
        print("6. EXIT")
        print("=========================")
        choice_menu = input("Choose between 1-6: ").strip()

        if choice_menu == '1':
            start_monitoring()
            print("Monitoring started")
            time.sleep(1)
        elif choice_menu == '2':
            list_status()
        elif choice_menu == '3':
            larm_menu()
        elif choice_menu == '4':
            get_larm()
        elif choice_menu == '5':
            start_monitoring_2()
        elif choice_menu == '6':
            print("EXIT")
            break
        else:
            print("NOT VALID")
        time.sleep(1)

if __name__ == "__main__":
    menu() 