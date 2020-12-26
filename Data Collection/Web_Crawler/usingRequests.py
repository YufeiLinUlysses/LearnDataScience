# This web crawler is based on xpath solely, bs4 and regex would be a similar process.

# For crwaling data
import requests
from lxml import etree

# For read and write data
import json

# Anti-UA detection: set up a headers variable for requests methods to disguise the crawler as a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}

# Weather Data from Estes Park,
# it is a get method API, requires one parameter: date
url = "http://www.estesparkweather.net/archive_reports.php"
params = {
    "date": 200508
}

# Get the website from the url
resp = requests.get(url=url, params=params, headers=headers)

# Save to a json file
fp = open("weatherData.json", "w", encoding="utf-8")

result = []

# Check if the connection is good and whether we have got the result
if resp.status_code == 200:
    tree = etree.HTML(resp.text)
    weathers = tree.xpath("//*[@id='main-copy']/table")[:-2]
    for w in weathers:
        temp = {}
        cur = w.xpath("./tr")[1:-1]
        for c in cur:
            t = c.xpath(".//text()")
            temp[t[1]] = t[2]
        result.append(temp)
        break
json.dump(result, fp=fp)