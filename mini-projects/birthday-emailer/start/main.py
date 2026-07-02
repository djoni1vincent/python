import smtplib
import datetime as dt
import random


with open("quotes.txt", "r") as data:
    quotes_list = data.readlines()

def send_email():
    my_email = "djoni7vincent@gmail.com"
    my_password = "hmoy oigo ktcm uqrq"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pythoncourse46@yahoo.com",
            msg=f"Subject:Motivational Quote\n\n{random.choice(quotes_list)}"
        )

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    send_email()
