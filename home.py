#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
import os
from Scrapper import Scrapper
from tqdm import tqdm

if __name__ == "__main__":

	urls = []
	numPics = int(input("How many wallpapers do you want to download: "))
	for i in range(1,(numPics//30)+2):
		url="https://www.pexels.com/?format=js&page={page}".format(page=i)
		urls.append(url)

	path = r"./Wallpapers/"
	if not os.path.exists(path):
		os.makedirs(path)
	scrapper = Scrapper(path,numPics)
	imgLinks = scrapper.readHtml(2)
	pool = ThreadPool(20)
	pool.map(scrapper.downLoad,imgLinks)
