#!/usr/bin/env python
import requests
import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen("https://www.rt.com/politics/")
soup = BeautifulSoup(url, 'html.parser')
count = 0



with open("news.html", "w") as file:
	file.write('{% extends "personal/header.html" %} {% block content %}')
with open("news.html", "a") as file:
	for item in soup.find_all("a", {"class" : "link link_hover"}):	
   	 file.writelines((str(str(item).replace('href="', 'href="https://www.rt.com'))+"<br>"))
with open("news.html", "a") as file:
	file.write('{% endblock %}')


