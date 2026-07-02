##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random


EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"

now = dt.datetime.now()
today_day = now.day
today_month = now.month

df = pd.read_csv("birthdays.csv")
dict_csv = df.to_dict(orient="records")
birthsday_today = [person for person in dict_csv if person["day"] == today_day and person["month"] == today_month]

if birthsday_today:
    for person in birthsday_today:
        file = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(f"{file}", "r") as data:
            letter = data.read()
            format_letter = letter.replace("[NAME]", person["name"])

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday\n\n{format_letter}"
            )
