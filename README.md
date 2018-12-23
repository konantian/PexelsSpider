# PexelsSpider
A spider for downloading wallpapers from pexels.com

## Reinforcement learning Second edition Chapter8 Example 8.1 implementation
[home.py](https://github.com/konantian/PexelsSpider/blob/master/home.py) This file is for downloading wallpapers from the home page<br />
[search.py](https://github.com/konantian/PexelsSpider/blob/master/search.py)This file is for downloading wallpapaers by specific tags<br />

Before start
------------
```
python3
```

Required Moduls 
------------
```
requests
BeautifulSoup
fake_useragent
```

How to start
------------
1. Clone this project: `git clone https://github.com/konantian/PexelsSpider.git`
2. Enter the project: `cd PexelsSpider`
3. Start the program without tag: `python3.6 home.py`
> * Enter the first page
> * Enter the last page
4.  Start the program with tag:  `python3.6 search.py`
> * Enter the tag

## Program introduction
This program is for you to download the beautiful wallpapers from www.pexels.com by just type the first page and the last page. If you want wallpapers under specific tags, you can instead by typing the tag only.After the program finish, it will create a folder called "Wallpapers" inside the current working path or it just called your tag.

## Wallpapers screenshot
![alt text](https://github.com/konantian/PexelsSpider/blob/master/screenshot.png)
