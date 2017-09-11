#!/usr/bin/python3
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("nairsiddharth81@gmail.com","1qwe2asd3zxc")
msg="Hey"
server.sendmail("nairsiddharth81@gmail.com","nairsiddharth81@gmail.com",msg)
print("success")
server.quit()