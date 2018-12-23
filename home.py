#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
import os
from Scrapper import Scrapper

if __name__ == "__main__":

	urls = []
	firstPage = int(input("Please enter first page: "))
	endPage = int(input("Please enter end page: "))
	for i in range(firstPage,endPage+1):
		url="https://www.pexels.com/?format=js&page={page}".format(page=i)
		urls.append(url)

	path = r"./Wallpapers/"
	if not os.path.exists(path):
		os.makedirs(path)
	scrapper = Scrapper(path)
	pool = ThreadPool(20)
	pool.map(scrapper.readHtml,urls)
