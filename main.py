import requests
from bs4 import BeautifulSoup

r = requests.get("http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class":"propertyRow"})
all[0].find("h4", {"class":"propPrice"}).text.replace("\n","").replace(" ", "")
