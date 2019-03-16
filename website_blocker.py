import time
from datetime import datetime as dt     # shortened name as expressions could be fairly long

hosts_temp_path = "hosts"
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
        # with open(hosts_temp_path,'r+') as file:
        with open(hosts_path,'r+') as file:
            content = file.read()
            print(content)      # diagnostic
            for website in website_list:
                if website in content:      # if website listed in hosts already
                    pass
                else:
                    # file.write('\n' + redirect + ' ' + website)
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(hosts_temp_path, 'r+') as file:    # file pointer placed at beginning of file with r+
            content = file.readlines()              # scan line by line
            file.seek(0)                            # put file pointer to very start of file again after read
            print(content)      # diagnostic
            for line in content:
                if not any(website in line for website in website_list):  # video 9-137 06:00
                    file.write(line)
                # for website in website_list:
                #     if website in line:                 # PJ solution - not working
                #         pass
                #     else:
                #         file.write(line)
            file.truncate()                         # remove text after current

        print('Not in working hours')
    time.sleep(5)
