from datetime import datetime
import time

dt1 = datetime(2018, 1, 1)  # create a datetime object
dt2 = datetime.now()  # method used to get the "now"
# Directive from parsing from string to object:
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")

# Convert a timestamp to datetime object.
dt = datetime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

print(dt2 > dt1)
