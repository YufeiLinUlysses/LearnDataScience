# This web crawler is based on xpath solely, bs4 and regex would be a similar process.

# For crwaling data
import requests
from lxml import etree

# For read and write data
import json

# Set up a dictionary to convert keys
keyDict = {
    "Average temperature": "AvgTemp",
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

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Anti-UA detection: set up a headers variable for requests methods to disguise the crawler as a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}

# Weather Data from Estes Park,
# it is a get method API, requires one parameter: date
url = "http://www.estesparkweather.net/archive_reports.php"
params = {
    "date": 201012
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
        cur = w.xpath(".//tr")[:-1]
        get = cur[0].xpath(".//text()")
        sp = get[1].split()
        if 'Dec' in sp:
            temp['Day'] = int(sp[1])
            for c in cur[1:]:
                t = c.xpath(".//text()")
                if t[1] == "Average temperature" or t[1] == "Average dewpoint":
                    temp[keyDict[t[1]]] = float(t[2].strip().replace("°F", ""))
                elif t[1] == "Average humidity":
                    temp[keyDict[t[1]]] = float(t[2].strip().replace("%", ""))
                elif t[1] == "Average barometer" or t[1] == "Rainfall for month" or t[1] == "Rainfall for year":
                    temp[keyDict[t[1]]] = float(
                        t[2].strip().replace("in.", ""))
                elif t[1] == "Average gustspeed" or t[1] == "Average windspeed":
                    temp[keyDict[t[1]]] = float(
                        t[2].strip().replace("mph", ""))
                elif t[1] == "Average direction":
                    curr = t[2].strip().split('(')
                    temp["AvgDir"] = curr[1].strip().replace(")","")
                    temp["AvgDirDegree"] = float(curr[0].strip().replace("°",""))
                else:
                    continue
            result.append(temp)

# Save to the json file
json.dump(result, fp=fp)
