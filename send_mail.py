# send mail

import smtplib
# msg = "Pryuvet lunatikam"

"""
def send_mail(mail_from, pasword_mail_from, mail_to):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail_from, pasword_mail_from)
    server.sendmail(mail_from, procent83@ukr.net, msg)
    server.quit()

send_mail('d.protsiuk@gmail.com', '05111994', 'procent83@ukr.net')
"""

def send_mail(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('d.protsiuk@gmail.com', '05111994')
    server.sendmail('d.protsiuk@gmail.com', procent83@ukr.net, msg)
    server.quit()



send_mail('Pryuvet lunatikam')
