import csv
from datetime import datetime
import shutil

today = datetime.today().strftime('%Y-%m-%d')
expiredusers = open("expiredusers.txt","w")
emailStart = "Tässä tiedot vanhentuneista käyttäjistä. Tiedot ovat muodossa 'username, name, email,created, expired' \n \n"

with open('tiedot.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)


    expUsers = ' '
 
    expiredusers.write(emailStart)
    for line in csv_reader:
        if line[4] < today and line[4] != "":
            expiredUsersList = expUsers.join(line)
            expiredusers.write(expiredUsersList + "\n")   

    total, used, free = shutil.disk_usage("/")
    expiredusers.write("\n")
    expiredusers.write("Levytilan käyttö:" + "\n")
    expiredusers.write("Yhteensä: %d GB" % (total // (2**30)) + "\n")
    expiredusers.write("Käytetty: %d GB" % (used // (2**30)) + "\n")
    expiredusers.write("Vapaana: %d GB" % (free // (2**30)) + "\n")
