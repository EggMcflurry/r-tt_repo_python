import psutil

monitoring_active = False
latest_status = {}

def start_monitoring():
    global monitoring_active, latest_status
    monitoring_active = True

    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    latest_status = {
        "CPU": cpu,
        "RAM": {"percent": ram.percent, "used": ram.used, "total": ram.total},
        "Disk": {"percent": disk.percent, "used": disk.used, "total": disk.total}
    }

def list_status():
    if not monitoring_active or not latest_status:
        print("\nNO ACTIVE MONITORING.")
    else:
        print("\n====ACTIVE MONITORING====")
        print(f"CPU USAGE: {latest_status['CPU']}%")
        
        ram = latest_status["RAM"]
        print(f"MEMORY USAGE: {ram['percent']}% "
              f"({ram['used'] // (1024**3)} GB of {ram['total'] // (1024**3)} GB)")

        disk = latest_status["Disk"]
        print(f"DISK USAGE: {disk['percent']}% "
              f"({disk['used'] // (1024**3)} GB of {disk['total'] // (1024**3)} GB)")

    input("\n----PRESS ENTER TO RETURN----.")

def get_monitoring():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return cpu, ram.percent, disk.percent
