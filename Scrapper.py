import requests
from bs4 import BeautifulSoup
from urllib.request import*
from fake_useragent import UserAgent
import re

class Scrapper:

	def __init__(self,path):

		self.agent = UserAgent()
		self.headers = {"User-Agent":self.agent.random}
		self.path = path
		self.linkPattern = re.compile(r'(?<=\").+?(?=\?)', re.S)
		self.namePattern = re.compile(r'\d+',re.S)

	def readHtml(self,url):

		req = Request(url = url,headers = self.headers)
		html = urlopen(req,timeout=5)
		bj = BeautifulSoup(html.read(),"lxml")
		content = bj.findAll("img",{"srcset":True})
		for i in content:
			imgLink = self.linkPattern.findall(i['src'])[0]
			self.downLoad(imgLink)

	def downLoad(self,img):
		number = self.namePattern.findall(img)[0]
		name = number + ".jpeg"
		req = requests.get(img,headers = self.headers)
		pic = req.content
		with open(self.path+name,'wb') as f:
			f.write(pic)
