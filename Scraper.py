import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get('https://www.equipmenttrader.com/2015-Any/equipment-for-sale?keyword=336FL&year=2015%3A%2A&sort=relevance%3Adesc', headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
prices = soup.find_all('div', class_='price main')
years = soup.find_all('h3' , class_ = 'sub-title')
i = 0
j = 0
sum = 0
while i < len(prices):
    
    if prices[i].text != "$0":
        j += 1
        print(f'Purchase Price: {prices[i].text}         Year: {years[i].text}')
        clean = int(prices[i].text.replace('$','').replace(',',''))
        sum += clean
        
    i = i + 1
average = sum/j
print(f'Average price: {average}')
    
