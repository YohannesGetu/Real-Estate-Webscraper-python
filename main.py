import requests
from bs4 import BeautifulSoup

r = requests.get("http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
print(soup.prettify())
