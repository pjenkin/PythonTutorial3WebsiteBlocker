import time
from datetime import datetime as dt     # shortened name as expressions could be fairly long

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# r prefix for a string literal, to avoid Win path slash separators as escape characters
# could alternatively have used double slash \\
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com']

working_hours_start = 8     # 0800 hours
working_hours_finish = 18   # 1800 hours

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, working_hours_start) < dt.now() \
            < dt(dt.now().year, dt.now().month, dt.now().day, working_hours_finish):
        # is time between working time start and working time finish?
        print('In working hours')        # just to illustrate working loop
    else:
        print('Not in working hours')
    time.sleep(5)
