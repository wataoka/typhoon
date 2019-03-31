import re
import csv
import json
import urllib
from bs4 import BeautifulSoup

data = {}
id = 1

for year in range(1999, 2020):
    url = "https://ja.wikipedia.org/wiki/" + str(year) + "%E5%B9%B4%E3%81%AE%E5%8F%B0%E9%A2%A8"

    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    data[year] = []
    number = 1

    headline_list = soup.find_all("span", attrs={"class": "mw-headline"})
    headline_list = list(map(lambda x: x.string, headline_list))
    headline_list = [x for x in headline_list if x is not None]
    headline_list = [x for x in headline_list if ('台風' and '号') in x]

    r = re.compile('（.+?）|\(.+?\)')
    for x in headline_list:
        m = r.search(x)
        data[year].append({
            'id': id,
            'number': number,
            'name': x[m.start()+1 : m.end()-1]
        })
        id += 1
        number += 1

    number = 1
    table_bottom_list = soup.find_all("tr", style="border-bottom: 1px solid #aaa")
    for table_bottom in table_bottom_list:
        if number > len(data[year]):
            break
        table_bottom = str(table_bottom)

        index = table_bottom.index("</small>")
        if table_bottom[index+16] == '1':
            data[year][number-1]['pressure'] = table_bottom[index+16 : index+20]
            number += 1
        else:
            data[year][number-1]['pressure'] = table_bottom[index+16 : index+19]
            number += 1

f = open('data/test.json', 'w')
json.dump(data, f)
