# This web crawler is based on xpath solely, bs4 and regex would be a similar process.

# For crwaling data
import requests
from lxml import etree

# For read and write data
import json

# Set up a dictionary to convert keys
keyDict = {
    "Average Temperature": "AvgTemp",
    "Average gustspeed": "AvgGust",
    "Average humidity": "AvgHum",
    "Average dewpoint": "AvgDew",
    "Average barometer": "AvgBaro",
    "Average windspeed": "AvgWind",
    "Average direction": "AvgDir",
    "Rainfall for month": "RfMonth",
    "Rainfall for year": "RfYear",
    "Maximum rain per minute": "maxRPM",
    "Maximum temperature": "maxTemp",
    "Minimum temperature": "minTemp",
    "Minimum pressure": "minPres",
    "Maximum pressure": "maxPres",
    "Maximum windspeed": "maxWind",
    "Maximum gust speed": "maxGust",
    "Maximum humidity": "maxHum",
    "Minimum humidity": "minHum",
    "Maximum heat index": "maxHeat"
}

# Anti-UA detection: set up a headers variable for requests methods to disguise the crawler as a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}

# Weather Data from Estes Park,
# it is a get method API, requires one parameter: date
url = "http://www.estesparkweather.net/archive_reports.php"
params = {
    "date": 200501
}

# Get the website from the url
resp = requests.get(url=url, params=params, headers=headers)

# Save to a json file
fp = open("weatherData.json", "w", encoding="utf-8")

result = []

# Check if the connection is good and whether we have got the result
if resp.status_code == 200:
    # Convert html to tree
    tree = etree.HTML(resp.text)
    # Search through xpath on the given html
    weathers = tree.xpath("//*[@id='main-copy']/table")[:-2]
    for w in weathers:
        temp = {}
        cur = w.xpath(".//tr")[1:-1]
        for c in cur:
            t = c.xpath(".//text()")
            temp[t[1]] = t[2]
        result.append(temp)

# Save to the json file
json.dump(result, fp=fp)
