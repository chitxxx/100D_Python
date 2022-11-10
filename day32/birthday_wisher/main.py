import smtplib
import json
import random
import pandas as pd
import datetime as dt

# Setup Email
with open("send_email.json", "r") as datafile:
    data = json.load(datafile)
EMAIL_SENDER = data["email"]
PASSWORD_SENDER = data["password"]

# Check Today's Date
now = dt.datetime.now()
today_month = now.month
today_day = now.day

# Load People List
df_people = pd.read_csv("birthdays.csv")


# Construct Email
def construct_email(name):
    random_email = random.choice([1, 2, 3])
    with open(f"letter_templates/letter_{random_email}.txt", "r") as datafile:
        template = datafile.readlines()
    template = "".join(template)
    email_body = template.replace("[NAME]", name)
    return email_body


for _, row in df_people.iterrows():
    name = row["name"]
    email = row["email"]
    day = row["day"]
    month = row["month"]

    if (today_month == month) & (today_day == day):
        # construct email
        email_body = construct_email(name)

        # send email
        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as conn_smtp:
            conn_smtp.ehlo()
            conn_smtp.starttls()
            conn_smtp.login(user=EMAIL_SENDER,
                            password=PASSWORD_SENDER)
            conn_smtp.sendmail(from_addr=EMAIL_SENDER,
                               to_addrs=email,
                               msg=email_body)
