import requests
import csv
import os
from dotenv import load_dotenv


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


def api(m, year):
    api_key = os.getenv('API_KEY')
    payload = {
        'api_key': api_key,
        'year': year,
        'make': m,
        'field': 'model',
        'input': 'f'
    }
    url = 'http://api.marketcheck.com/v2/specs/car/auto-complete'
    response = requests.get(url=url, params=payload).content
    print(response)
    exit()


if __name__=="__main__":
    print('-------------- Start ---------------')
    load_dotenv()
    for year in range(2010, 2021):
        for make in makes:
            api(make, year)
    print('-------------- End ----------------')