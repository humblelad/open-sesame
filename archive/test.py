import requests
import csv
from bs4 import BeautifulSoup

no = 0
convert = []
for i in range(0, 429):

    print("Collecting page " + str(i + 1))
    URL = 'http://h1.nobbd.de/index.php?start=' + str(no)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='reports-all')
    test = results.find_all(class_='title')

    for o in test:
        s = o['href']
        print(s)

        convert.append(s)

    no += 20

with open("copy.txt", "w") as outfile:
    outfile.write("\n".join(convert))

    # This is the default code used to scrape allt the publlicly disclosed reports.
    # regex i used to filter only https:// from awesome bug bounty writeups by asemodus (something lol) repo:
    # [-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)
