import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_forex_factory(day='may13.2026'):
    url = f'https://www.forexfactory.com/calendar?day={day}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        # Basic table parsing logic (extend with full row extraction for impact, currency, actual etc.)
        events = []
        print('Scraped events for', day)
        # TODO: Parse rows and save to CSV
        df = pd.DataFrame(events)
        df.to_csv(f'calendar_{datetime.now().date()}.csv', index=False)
        return df

if __name__ == '__main__':
    scrape_forex_factory()