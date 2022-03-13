from datetime import datetime
import smtplib
import random 
import pandas

MY_EMAIL = "nikkiferrel2012@gmail.com"
PASSWORD = "Nikkidorw@l2022"

now = datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("./birthday.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL, 
            to_addrs = birthday_person["email"], 
            msg = f"Subject:Happy Birthday\n\n{contents}"
        )
