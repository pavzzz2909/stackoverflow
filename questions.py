import requests
import time
import datetime
from pprint import pprint

def time_stamp(date):
    return int(time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()))

def date():
    date_now = str(datetime.datetime.now()).split(' ')[0]
    Ynow, Mnow, Dnow = date_now.split('-')
    Dpred = int(Dnow) - 2
    if Dpred <= 0:
        Mpred = int(Mnow)
        Mpred = Mpred-1
        if Mpred == 0:
            Dpred +=31
            pred_date = str(int(Ynow)-1)+"-"+str(12)+"-"+str(Dpred)
            return time_stamp(date_now),time_stamp(pred_date)
        else:
            if Mpred==4 and Mpred==6 and Mpred==9 and Mpred==11:
                Dpred +=30
            elif Mpred==2 and Ynow % 4 != 0:
                Dpred +=28
            elif Mpred==2 and Ynow % 4 == 0:
                Dpred +=29
            else:
                Dpred +=31
            pred_date = str(Ynow)+"-"+str(Mpred)+"-"+str(Dpred)
            return time_stamp(date_now),time_stamp(pred_date)
    else:
        pred_date = str(Ynow)+"-"+str(Mnow)+"-"+str(Dpred)
        return time_stamp(date_now),time_stamp(pred_date)


api = 'https://api.stackexchange.com/'
tag = 'Python'
to_date, from_date = date()
url = api + f'2.3/questions??fromdate={from_date}todate={to_date}&order=desc&sort=activity&tagged={tag}&site=stackoverflow'

response = requests.get(url = url).json()



pprint(response)
