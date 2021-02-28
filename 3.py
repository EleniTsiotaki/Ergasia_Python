import urllib.request
from urllib.parse import urlparse
import json
import datetime

def change_date(url):
    u = urlparse(url)
    replaced = u._replace
    path = '/draws/v3.0/1100/draw-date/' + xronos_kai_mhnas +'-' + str(i) + '/' + xronos_kai_mhnas + '-' + str(i)   #allazw thn hmeromhnia kai thn selida kathe fora
    query = '?page=17'
    new_url = "https://api.opap.gr" + path + query
    #print(new_url)
    return new_url

date_and_time = datetime.datetime.now() - datetime.timedelta(days=1) #twrinh hmeromhnia kai wra
shmerinh_hmeromhnia = date_and_time.strftime("%Y-%m-%d") #shmerinh hmeromhnia
mera = int(date_and_time.strftime("%d"))
xronos_kai_mhnas = date_and_time.strftime("%Y-%m")

for i in range(1, mera+2): #klirwseis apo thn 1h tou mhna mexri thn trexousa mera
    if i < 10:
        i = '0' + str(i)
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/{fromDate}/{toDate}/?page=1"
    new_url = change_date(url) #kalw th synarthsh gia na allaksw thn hmeromhnia kai selida sto link
    r = urllib.request.urlopen(new_url)
    html = r.read()
    html = html.decode()
    data = json.loads(html, strict=False)
    prwth_klirosi = data['content'][9]['winningNumbers']['list']
    print(prwth_klirosi)
