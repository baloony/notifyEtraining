#! python3
import re, requests, datetime, smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Parse(object):
    def __init__(self, url):
        self.r = requests.get(url)
        self.data = self.r.text

    def parse(self):
        self.regex = re.compile(r'[0-9]{1,2}\.[0-9]{1,2}\.\d{4}')
        return self.regex.findall(self.data)

class Mail(object):
    @staticmethod
    def sendMail(date):
        cmd = 'echo E-usavršavanje termina za 8 dana - ' + date + ' |  mail -s "E-Usavrsavanje - Termin" ivan.esterajher@ztm.hr '
        os.system(cmd)
        #os.system('echo "E-usavršavanje termin za 8 dana - ' + date + '" | mail -s "E-Usavrsavanje - Termin" ivan.esterajher@ztm.hr ')


class Notify(object):
    def __init__(self, dates):
        self.date = datetime.datetime.today() #+ datetime.timedelta(days=8)
        self.date = self.date.strftime("%d.%m.%Y")  # Mora ici plus 8 dana jos
        if self.date in dates:
            Mail.sendMail(self.date)


def main():
    url = 'http://www.ztm.hr/?q=hr/content/raspored'
    parse_it = Parse(url)
    dates = parse_it.parse()
    notify = Notify(dates)


main()