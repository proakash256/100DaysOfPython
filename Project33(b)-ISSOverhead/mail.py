import smtplib

MY_EMAIL = "EMAIL"
PASSWORD = "PASSWORD"


def send_email():
    with smtplib.SMTP("smtp.gmail.com", 578) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg="Subject:Hurry Up!!\n\nThe International Space Station is overhead.\n\nGo Fast!!")
