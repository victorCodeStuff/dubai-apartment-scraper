import requests
from bs4 import BeautifulSoup
import csv
root = 'https://www.propertyfinder.ae/en/rent/dubai/apartments-for-rent.html' ## to help to scrape muiltiple pages later
website = f'{root}?page=2'

print(website)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/53.6'}
r = requests.get(website ,headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
print(f"Status Code: {r.status_code}")

advantages = soup.find_all('h2', class_='styles-module_content__title__eOEkd')
locations = soup.find_all('p', class_='styles-module_content__location__bNgNM')
prices = soup.find_all('p', class_='styles-module_content__price__SgQ5p')
sizes = soup.find_all('p', class_='styles-module_content__details-item__mlu9B')
links = soup.find_all('a', class_='property-card-module_property-card__link__L6AKb')


print(advantages)
filename = "apartmentsInDubai.csv"
header = ["link","advantages","location","price", "size"]
with open(filename, 'w',encoding='UTF8') as f:
        csvwriter= csv.writer(f)
        csvwriter.writerow(header)
        for advantage,location,price,size,link in zip(advantages,locations,prices,sizes,links):
            dataEachRow =(link.get('href'),advantage.text.strip(),location.text.strip(),price.text.strip(),size.text.strip()) 
            csvwriter.writerow(dataEachRow)






