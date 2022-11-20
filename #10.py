import requests
from bs4 import BeautifulSoup
import csv


def save():
    with open("buy_cars", 'a') as file:
        file.write(f'{car["title"]} : {car["price"]} - {car["city"]}\n')

def parser():
    url = "https://www.olx.ua/d/uk/transport/legkovye-avtomobili/"

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"
    }

    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.content, 'html.parser')
    items = soup.find_all('div', class_='css-qfzx1y')
    cars = []

    for item in items:
        cars.append({
            'title': item.find('h6', class_ = "css-1pvd0aj-Text eu5v0x0").get_text(strip=True),
            'price': item.find('p', class_ = "css-1q7gvpp-Text eu5v0x0").get_text(strip=True),
            'city': item.find('p', class_ = "css-p6wsjo-Text eu5v0x0").get_text(strip=True)
        })
    global car
    for car in cars:
        print(f'{car["title"]} : {car["price"]} - {car["city"]}')
        save()

parser()
