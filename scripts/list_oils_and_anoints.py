import requests
import json
from bs4 import BeautifulSoup

base_url = "poewiki.net"
list_of_anointments = requests.get("https://www.poewiki.net/wiki/List_of_anointments")

soup = BeautifulSoup(list_of_anointments.text, "html.parser")
tables = soup.find_all("table")

only_from_anointments = tables[0]
other_anointments = tables[1]

anoints = only_from_anointments.tbody.find_all("tr")
anoints.pop(0)
other_anointments = other_anointments.find_all("tr")
other_anointments.pop(0)

every_anoint = anoints + other_anointments

all_anoints = []

print(f"Titles:")
table_titles = only_from_anointments.tbody.find_all("tr")
for titles in table_titles[0]:
    print(titles.text)

print(f"Exctracting anointment info...")
for anoint in every_anoint:
    print("Extracting new anointment...")
    count = 0
    oils = []
    description = []
    outcome = []
    img_link = []
    for td in anoint:
        for a in td:
            if count < 3:
                oils.append(a.text)
            elif count == 3:
                outcome.append({"name": a.text})
                if td.img:
                    outcome.append({"img_link": base_url + td.img.get("src")})
            else:
                if a.text:
                    description.append(a.text)
            count += 1
    outcome.append({"description": description})
    anoint = {"oils": oils, "outcome": outcome}
    all_anoints.append(anoint)


print("Done extracting anoints!")

with open("data/all_anointments.json", "w") as file:
    file.write(json.dumps(all_anoints))
