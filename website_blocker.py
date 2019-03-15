import time

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# r prefix for a string literal, to avoid Win path slash separators as escape characters
# could alternatively have used double slash \\
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com']

while True:
    print(1)        # just to illustrate working loop
    time.sleep(5)
# is time between working time start and working time finish?
