import requests
from bs4 import BeautifulSoup

my_file = open("goros.txt", "w+")
my_file.close()

url1 = 'https://horo.mail.ru/prediction/pisces/today/'
response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text, 'lxml')
quotes1 = soup1.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes1:
    my_file = open("goros.txt", "a+")
    my_file.write('Рыбы: '+ quote.text)
    my_file.close()

url2 = 'https://horo.mail.ru/prediction/aquarius/today/'
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'lxml')
quotes2 = soup2.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes2:
    my_file = open("goros.txt", "a+")
    my_file.write('Водолей: '+ quote.text)
    my_file.close()

url3 = 'https://horo.mail.ru/prediction/aries/today/'
response3 = requests.get(url3)
soup3 = BeautifulSoup(response3.text, 'lxml')
quotes3 = soup3.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes3:
    my_file = open("goros.txt", "a+")
    my_file.write('Овен: '+ quote.text)
    my_file.close()

url4 = 'https://horo.mail.ru/prediction/cancer/today/'
response4 = requests.get(url4)
soup4 = BeautifulSoup(response4.text, 'lxml')
quotes4 = soup4.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes4:
    my_file = open("goros.txt", "a+")
    my_file.write('Рак: ' + quote.text)
    my_file.close()

url5 = 'https://horo.mail.ru/prediction/virgo/today/'
response5 = requests.get(url5)
soup5 = BeautifulSoup(response5.text, 'lxml')
quotes5 = soup5.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes5:
    my_file = open("goros.txt", "a+")
    my_file.write('Дева: ' + quote.text)
    my_file.close()

url6 = 'https://horo.mail.ru/prediction/gemini/today/'
response6 = requests.get(url6)
soup6 = BeautifulSoup(response6.text, 'lxml')
quotes6 = soup6.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes6:
    my_file = open("goros.txt", "a+")
    my_file.write('Близнецы: ' + quote.text)
    my_file.close()

url7 = 'https://horo.mail.ru/prediction/leo/today/'
response7 = requests.get(url7)
soup7 = BeautifulSoup(response7.text, 'lxml')
quotes7 = soup7.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes7:
    my_file = open("goros.txt", "a+")
    my_file.write('Лев: ' + quote.text)
    my_file.close()

url8 = 'https://horo.mail.ru/prediction/scorpio/today/'
response8 = requests.get(url8)
soup8 = BeautifulSoup(response8.text, 'lxml')
quotes8 = soup8.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes8:
    my_file = open("goros.txt", "a+")
    my_file.write('Скорпион: ' + quote.text)
    my_file.close()

url9 = 'https://horo.mail.ru/prediction/sagittarius/today/'
response9 = requests.get(url9)
soup9 = BeautifulSoup(response9.text, 'lxml')
quotes9 = soup9.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes9:
    my_file = open("goros.txt", "a+")
    my_file.write('Стрелец: ' + quote.text)
    my_file.close()

url10 = 'https://horo.mail.ru/prediction/capricorn/today/'
response10 = requests.get(url10)
soup10 = BeautifulSoup(response10.text, 'lxml')
quotes10 = soup10.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes10:
    my_file = open("goros.txt", "a+")
    my_file.write('Козерог: ' + quote.text)
    my_file.close()

url11 = 'https://horo.mail.ru/prediction/taurus/today/'
response11 = requests.get(url11)
soup11 = BeautifulSoup(response11.text, 'lxml')
quotes11 = soup11.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes11:
    my_file = open("goros.txt", "a+")
    my_file.write('Телец: ' + quote.text)
    my_file.close()

url12 = 'https://horo.mail.ru/prediction/libra/today/'


response12 = requests.get(url12)
soup12 = BeautifulSoup(response12.text, 'lxml')
quotes12 = soup12.find_all('div', class_='article__item article__item_alignment_left article__item_html')

for quote in quotes12:
    my_file = open("goros.txt", "a+")
    my_file.write('Весы: ' + quote.text)
    my_file.close()
