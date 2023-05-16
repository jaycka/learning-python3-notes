import sys
import re
import urllib.request
import datetime as dt
from pathlib import Path
import random
import time
from tqdm import tqdm

max_day = 1
if len(sys.argv)==2:
    max_day = int(sys.argv[1])+1

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

wallpaper=Path('wallpaper')
if not wallpaper.exists():
    wallpaper.mkdir()

for i in tqdm(range(max_day)):
    cur_date = (dt.datetime.now()-dt.timedelta(i)).strftime('%Y%m%d')
    webpage = f"https://bing.wallpaper.pics/us/{cur_date}.html"
    print(webpage)
    webpage_url = urllib.request.Request(webpage, headers=headers)
    with urllib.request.urlopen(webpage_url, timeout=20) as f:
        response = f.read().decode('utf-8')
    result = re.search('www.*.jpg', response)
    pic_url = "http://"+response[result.start():result.end()]
    pic_name = pic_url.split('.')
    pic_name = '.'.join((pic_name[3],pic_name[5]))
    if not (wallpaper / pic_name).exists():
        urllib.request.urlretrieve(pic_url,wallpaper/pic_name)
    time.sleep(random.randint(1,5))
