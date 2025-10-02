import urllib.request
from urllib.parse import urlparse
import json
import datetime

def dataa(r):
    html = r.read()
    html = html.decode()
    data = json.loads(html, strict=False)
    return data

date_and_time = datetime.datetime.now() - datetime.timedelta(days=1) #twrinh hmeromhnia kai wra
shmerinh_hmeromhnia = date_and_time.strftime("%Y-%m-%d") #shmerinh hmeromhnia
mera = int(date_and_time.strftime("%d"))
mhnas = date_and_time.strftime("%m")
xronos = date_and_time.strftime("%Y")

for i in range(1, mera + 2): #klirwseis apo thn 1h tou mhna mexri thn trexousa mera
    if i < 10:
        i = '0' + str(i)
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/2020-01-02/2020-01-02/?page=1"    
    u = urlparse(url)
    replaced = u._replace
    path = '/draws/v3.0/1100/draw-date/' + xronos +'-' + mhnas +'-' + str(i) + '/' + xronos +'-' + mhnas + '-' + str(i)   #allazw thn hmeromhnia kai thn selida kathe fora
    r = urllib.request.urlopen("https://api.opap.gr" + path)
    data = dataa(r)
    x = str(data['totalPages']-1) #epeidh oi selides ksekinoun apo 0 sthn arithmisi
    query = '?page=' + x
    new_url = "https://api.opap.gr" + path + query    
    r = urllib.request.urlopen(new_url)
    data =dataa(r)
    len_cont = len(data['content'])
    prwth_klirosi = data['content'][len_cont-1]['winningNumbers']['list']
    print("H prwth klirosh gia",xronos,"-",mhnas,"-", i , "einai:",prwth_klirosi)

