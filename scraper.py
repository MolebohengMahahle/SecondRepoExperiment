import requests
from bs4 import BeautifulSoup

# Website to scrape
url = "https://news.mandela.ac.za/"

# Send request
response = requests.get(url)

# Create Beautiful Soup object
soup = BeautifulSoup(response.text, "html.parser")

# Find article titles
headings = soup.find_all("h2")

print("Latest news headlines:\n")

for i, heading in enumerate(headings, start=1):
    print(f"{i}. {heading.get_text(strip=True)}")
