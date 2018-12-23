#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Scrapper import Scrapper
import os

if __name__ == "__main__":

	tag = input("Please enter the search tag: ")
	path = r"./{tag}/".format(tag=tag)
	if not os.path.exists(path):
		os.makedirs(path)
	scrapper = Scrapper(path)
	url="https://www.pexels.com/search/{tag}/?format=js".format(tag=tag)
	scrapper.readHtml(url)
