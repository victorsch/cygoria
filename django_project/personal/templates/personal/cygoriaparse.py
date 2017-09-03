#!/usr/bin/env python
import re
import requests
import urllib
from bs4 import BeautifulSoup
import os
import sys

n = 1

html = urllib.urlopen('http://127.0.0.1:8000/news/')
soup = BeautifulSoup(html, 'html.parser')
text = ""

file = open("links.html", "w")
for item in soup.find_all("a", {"class" : "link link_hover"}):
	for links in re.findall(r'(https?://[^\s]+)', str(item)):
		file.writelines(str(links)+'\n')
file.close()


#with open('links.txt', 'r') as file
	#link = file.readlines()
	#print (file.readlines())
	#data = urllib.urlopen(str(link))
	#article = BeautifulSoup(data, 'html.parser')
	#articleF = open("article.txt", "a")
	#for articleText in article.find_all("p"):
	#	articleF.write(str(articleText))
	#n = n + 1
	#file.close()

f = open("text5.txt", "w")
f.write('{% extends "personal/header.html" %} {% block content %}')
for itema in soup.find_all("a", {"class" : "link link_hover"}):
	for linksa in re.findall(r'(https?://[^\s]+)', str(itema)):
		soupa = BeautifulSoup(urllib.urlopen(str(linksa)), 'html.parser')
		f.write(str(soupa.find_all("p")))
f.write('{% endblock %}')
f.close()

os.rename('text5.txt', 'article.html')

	





