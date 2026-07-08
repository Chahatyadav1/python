# info = 0
# warning = 0
# error = 0

# with open("app.log", "r") as f:
#     for line in f:
#         if "INFO" in line:
#             info += 1
#         elif "WARNING" in line:
#             warning += 1
#         elif "ERROR" in line:
#             error += 1

# print(f"INFO: {info}")
# print(f"WARNING: {warning}")
# print(f"ERROR: {error}")


#project -2 


# import psutil

# disk=psutil.disk_usage('/')

# print(f"total:{disk.total}")
# print(f"usage:{disk.used}")
# print(f"free:{disk.free}")
# if(disk.percent > 80.0):
#     print("Alert high usage")

# import psutil
# battery = psutil.sensors_battery()
# print(battery)

import os
import shutil
a=os.listdir(path='.')
os.mkdir("Demo")
for i in a:
    if os.path.isfile(i) and not i.endswith(".log"):
        shutil.copy(i, "Demo")


