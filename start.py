#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib.request import*
from fake_useragent import UserAgent
from multiprocessing.dummy import Pool as ThreadPool
import re

class Scrapper:

	def __init__(self):

		self.agent = UserAgent()
		self.headers = {"User-Agent":self.agent.random}
		self.path = r'/Users/wangyuan/Wallpaper/'
		self.pattern = re.compile(r'(?<=\").+?(?=\?)', re.S)

	def readHtml(self,url):

		req = Request(url = url,headers = self.headers)
		html=urlopen(req,timeout=5)
		bj=BeautifulSoup(html.read(),"lxml")
		content=bj.findAll("img",{"srcset":True})
		for i in content:
			imgLink = self.pattern.findall(i['src'])[0]
			self.downLoad(imgLink)

	def downLoad(self,img):

		name="/" + img.replace(':', '@').replace('/', '_')
		req = requests.get(img,headers = self.headers)
		pic = req.content
		with open(self.path+name,'wb') as f:
			f.write(pic)


if __name__ == "__main__":

	urls = []
	firstPage = int(input("Please enter first page: "))
	endPage = int(input("Please enter end page: "))
	for i in range(firstPage,endPage+1):
		url="https://www.pexels.com/?format=js&page={page}".format(page=i)
		urls.append(url)

	scrapper = Scrapper()
	pool = ThreadPool(20)
	pool.map(scrapper.readHtml,urls)
