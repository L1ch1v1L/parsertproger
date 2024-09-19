import requests
import csv
from bs4 import BeautifulSoup

# URL целевой страницы
url = 'https://tproger.ru/'

fulltitles = []
fulldescript = []

# Выполняем HTTP запрос
response = requests.get(url)

# Проверяем, успешный ли запрос
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2', class_='tp-ui-post-card__title')
    description = soup.find_all("p",class_='tp-ui-post-card__description')
    if titles:
        for title in titles:
            link_text = title.get_text(strip=True)
            fulltitles.append(link_text)
    if description:
        for desc in description:
            link_text = desc.get_text(strip=True)
            fulldescript.append(link_text)

for i in range(len(fulltitles)):
    print(str(i+1)+" статья. Название:\n"+fulltitles[i])
    print("Описание:")
    print(fulldescript[i])
    print("\n")
# Указываем имя файла
filename = 'news1.csv'

with open(filename, mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Записываем заголовки
    writer.writerow(['Название', 'Описание'])
    
    # Записываем строки данных
    for item in range(len(fulltitles)):
        writer.writerow([fulltitles[item], fulldescript[item]])
