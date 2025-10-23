
import time 
list_larm = []
#menu for setting larm
def larm_menu():
    while True:
        print("===== START LARM =====")
        print("1. CPU usage")
        print("2. MEMORY usage")
        print("3. DISK usage")
        print("4. EXIT")
        choice = input("OPTION: ").strip()

        if choice == '1':
            larm_build("CPU")
        elif choice == '2':
            larm_build("RAM")
        elif choice == '3':
            larm_build("DISK")
        elif choice == '4':
            break
        else:
            print("Not valid option.")
            time.sleep(1)
#structure for func to larm
def larm_build(larm_type):
    while True:
        level = input(f"LEVEL FOR:{larm_type}-larm (1%-100%): ").strip()
        if level.isdigit():
            level = int(level)
            if 1 <= level <= 100:
                list_larm.append({"type": larm_type, "level": level})
                print(f"LARM TO {larm_type} CONFIG TO {level}%")
                return
        print("NOT VALID")

def get_larm():
    if not list_larm:
        print("NO ACTIVE LARM")
    else:
        print("CONFIG LARM:")
        for larm in sorted(list_larm, key=lambda x: x["type"]):
            print(f"{larm['type']} LARM AT: {larm['level']}%")
    input("press any key to return")

def controll(cpu, ram, disk):
    warning = []
    for larm in list_larm:
        if larm["type"] == "CPU" and cpu >= larm["level"]:
            warning.append(f"===CPU WARNING: {cpu}% >= {larm['level']}%====")
        elif larm["type"] == "RAM" and ram >= larm["level"]:
            warning.append(f"===RAM WARNING: {ram}% >= {larm['level']}%===")
        elif larm["type"] == "DISK" and disk >= larm["level"]:
            warning.append(f"===DISK WARNING: {disk}% >= {larm['level']}%===")
    return warning
