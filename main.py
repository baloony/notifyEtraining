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
    def sendMailPotpisne(date):
        cmd = 'echo E-usavršavanje termin za 8 dana - ' + date + '. Pripremi potpisne liste |  mail -s "E-Usavrsavanje - potpisne liste" ivan.esterajher@ztm.hr '
        os.system(cmd)

    @staticmethod
    def sendMailPotpisne():
        cmd = 'echo E-usavršavanje termin je danas u 13:00h  |  mail -s "E-Usavrsavanje - Termin" ivan.esterajher@ztm.hr '
        os.system(cmd)



class Notify(object):
    def __init__(self, dates):
        self.date = datetime.datetime.today() + datetime.timedelta(days=8)
        self.date = self.date.strftime("%d.%m.%Y")
        self.today = datetime.datetime.today().strftime("%d.%m.%Y")
        if self.date in dates:
            Mail.sendMailPotpisne(self.date)
        if self.today in dates:
            Mail.sendMailObavijest()



def main():
    url = 'http://www.ztm.hr/?q=hr/content/raspored'
    parse_it = Parse(url)
    dates = parse_it.parse()
    notify = Notify(dates)


main()