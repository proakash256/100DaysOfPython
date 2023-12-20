import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = "EMAIL"
PASSWORD = "PASSWORD"
TODAY = (dt.datetime.now().month, dt.datetime.now().day)

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in birthdays.iterrows()}
if TODAY in birthdays_dict:
    letter_format = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_format) as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", birthdays_dict[TODAY]["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{birthdays_dict[TODAY].email}",
                                msg=f"Subject:Happy Birthday!!\n\n{letter_content}")
