import time
from datetime import datetime as dt
host_temp = "hosts"
host_path  = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
#Fill this with your desired files
website_list = ["www.facebook.com" , "www.yahoo.com" , "dub19.mail.live.com" , "www.dub19.live.com"]

while True:

    if (dt(dt.now().year,dt.now().month,dt.now().day,15 ) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,4 )):
        print("working hours...hehehehhahahahahahahaha")
        with open (host_path , "r+") as file:

            content = file.read()
            for websites in website_list:
                if websites in content:
                    pass
                else:
                    file.write(redirect + " " + websites+"\n")

    else:
        #print("go f yourself")
        with open(host_path , "r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content :

                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()




    time.sleep(5)
