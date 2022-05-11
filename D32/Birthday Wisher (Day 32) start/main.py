import smtplib

my_email = "webtester329@yahoo.com"
password = "gqlgozatktnqsduy"  # yahoo needs the generated app password to access smtp

with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()  # tls: transport layer security - encrypts the message, make it more secure
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="webtestercs102@gmail.com",
        msg="Subject:Hello\n\nThis is the body of email")  # emails without subjects are most likely going to be labelled as spam
