import requests 
import time
from multiprocessing.dummy import Pool
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}

urls = [
    "http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar",
    "http://zjlt.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10229.rar",
    "http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar"
]

def get_content(url):
    print("Crawling: ", url)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content

def parse_content(content):
    pass

def get_page(str):
    print("Downloading: ", str)
    time.sleep(2)
    print("Finished: ", str)

start_time = time.time()
name_list = ["xiaozi","aa","bb","cc"]

# Initialize a thread pool object
pool = Pool(4)

# Pass the function we use to map function for processing
pool.map(get_page, name_list)

end_time = time.time()

print(end_time-start_time)