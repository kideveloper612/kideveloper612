import requests
import csv
import os
from dotenv import load_dotenv
import urllib.parse
import json
import time


makes = [
    'Acura',
    'Audi',
    'BMW',
    'Buick',
    'Cadillac',
    'Chevrolet',
    'Chrysler',
    'Dodge',
    'Fiat',
    'Ford',
    'GMC',
    'Honda',
    'Hyundai',
    'Infiniti',
    'Jeep',
    'Kia',
    'Lexus',
    'Lincoln',
    'Mazda',
    'Mercedes Benz',
    'Nissan',
    'RAM',
    'Subaru',
    'Toyota',
    'Volkswagen',
    'Volvo'
]


csv_header = [['YEAR', 'MAKE', 'MODEL']]


def write_direct_csv(lines, filename):
    with open('output/%s' % filename, 'a', encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(lines)
    csv_file.close()


def write_csv(lines, filename):
    if not os.path.isdir('output'):
        os.mkdir('output')
    if not os.path.isfile('output/%s' % filename):
        write_direct_csv(lines=csv_header, filename=filename)
    write_direct_csv(lines=lines, filename=filename)


def api(m, year):
    api_key = os.getenv('API_KEY')
    payload = {
        'api_key': api_key,
        'year': year,
        'make': m,
        'field': 'model',
        'input': 'f'
    }

    headers = {
        'Host': 'marketcheck-prod.apigee.net'
    }

    url = 'http://api.marketcheck.com/v2/specs/car/terms?' + urllib.parse.urlencode(payload, doseq=True)
    print(url)
    response = requests.get(url=url, headers=headers).content
    data = json.loads(response)
    print(data)
    if 'terms' in data:
        return data['terms']
    elif 'model' in data:
        return data['model']


if __name__ == "__main__":
    print('-------------- Start ---------------')
    load_dotenv()
    for make in makes:
        for year in range(2010, 2021):
            res = api(make.lower(), year)
            time.sleep(10)
            if res:
                for model in res:
                    time.sleep(1)
                    line = [year, make, model]
                    print(line)
                    write_csv(lines=[line], filename='Model_List_Again.csv')
    print('-------------- End ----------------')
