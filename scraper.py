import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from typing import List


@dataclass
class ThrillistEvent:
    title: str
    link: str
    date: List[str] = field(metadata={"transform": "parse_data"})
    description: str
    price: str

    def __post_init__(self):
        if self.date.find("-"):
            self.date = self.date.split("-")
        else:
            self.date = [self.date]


LA_URL = "https://www.thrillist.com/events/los-angeles/things-to-do-in-los-angeles-this-weekend"

# BASE_URL = "https://www.thrillist.com"
# LOST_ANGELES_URL = "https://www.thrillist.com/los-angeles"

# page = requests.get(LOST_ANGELES_URL)

# soup = BeautifulSoup(page.content, "html.parser")

# events_headline = soup.find("h2", {"data-testid": "ucc-headline"})

# print(events_headline.find_parent()["href"])

# LA_events_url = BASE_URL + events_headline.find_parent()["href"]

# print(LA_events_url)


page = requests.get(LA_URL)

soup = BeautifulSoup(page.content, "html.parser")

title_tags = soup.find_all("h2")  # Every event title is wrapped in an h2

events = []

for tag in title_tags:
    title = tag.find("strong")
    link = None if not tag.find("a") else tag.find("a").get("href")

    print(f"The link is: {link}")
    if title:
        event_wrapper_div = title.find_parent("div")
        description = event_wrapper_div.find_next_sibling("p")

        date = description.find("strong").text
        location = description.find("em")
        price = description.find_all(string=True)[-1]

        # print(price)

        event = ThrillistEvent(title, link, date, location, price)

        print(event.date)

        # print(f"\n{description.find(text=True, recursive=False)}\n")
        # print(description)

        # print(date)
    # print(tag.find("strong"))

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)

# print(page.text)

# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(id="ResultsContainer")

# # print(results.prettify())

# job_elements = results.find_all("div", class_="card-content")

# for job_element in job_elements:
#     print(job_element, end="\n" * 2)
