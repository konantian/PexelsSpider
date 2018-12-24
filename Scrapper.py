import requests
from bs4 import BeautifulSoup
from urllib.request import *
from fake_useragent import UserAgent
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Scrapper:

	def __init__(self,path,amount=None):

		self.agent = UserAgent()
		self.headers = {"User-Agent":self.agent.random}
		self.path = path
		self.linkPattern = re.compile(r'(?<=\").+?(?=\?)', re.S)
		self.namePattern = re.compile(r'\d+',re.S)
		self.amount = amount
		self.imgLinks = []

	def readHtml(self,page):

		url="https://www.pexels.com/?format=js&page={page}".format(page=page)
		req = Request(url = url,headers = self.headers)
		html = urlopen(req,timeout=5)
		bj = BeautifulSoup(html.read(),"lxml")
		content = bj.findAll("img",{"srcset":True})
		for i in content:
			imgLink = self.linkPattern.findall(i['src'])[0]
			self.imgLinks.append(imgLink)
			if len(self.imgLinks) == self.amount:
				return self.imgLinks

		return self.readHtml(page+1)

	def readhtml(self,url):

		req = Request(url = url,headers = self.headers)
		html=urlopen(req,timeout=5)
		bj=BeautifulSoup(html.read(),"lxml")
		content=bj.findAll("img",{"srcset":True})
		for i in content:
			imgLink = self.linkPattern.findall(i['src'])[0]
			self.imgLinks.append(imgLink)

		return self.imgLinks

	def downLoad(self,img):
		number = self.namePattern.findall(img)[0]
		name = number + ".jpeg"

		try:
			req = requests.get(img,headers = self.headers)
			pic = req.content
			with open(self.path+name,'wb') as f:
				f.write(pic)

		except:
			print("Error happened, this picturs has been jumped!")
			pass
		

