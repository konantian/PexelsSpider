#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Scrapper import Scrapper
import os
from multiprocessing.dummy import Pool as ThreadPool

if __name__ == "__main__":

	tag = input("Please enter the search tag: ")
	path = r"./{tag}/".format(tag=tag)
	if not os.path.exists(path):
		os.makedirs(path)
	scrapper = Scrapper(path)
	url = "https://www.pexels.com/search/{tag}/?format=js".format(tag=tag)
	imgLinks = scrapper.readhtml(url)
	pool = ThreadPool(20)
	pool.map(scrapper.downLoad,imgLinks)

