import os
all_cookies=[]

BASE_DIR=os.path.dirname(os.path.abspath())
index=0
def get_cookies():
    global index
    if not all_cookies:
        read_cookies()
    cookie=all_cookies[index]
    index+=1
    index=index % len(all_cookies)
    return cookie
def read_cookies():
    with open(BASE_DIR,'cookie.txt','r') as f:
        for line in f:

            all_cookies.append(line.strip())

