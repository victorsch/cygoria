#!/usr/bin/env python
import re
import requests
import urllib
from bs4 import BeautifulSoup
from collections import Counter 


military = ""
russian = ""
Trump = ""
hacker = ""
terrorist = ""
corruption = ""

#data = urllib.urlopen("https://www.rt.com/politics/397312-double-damage-russian-senator-#warns/")
data = urllib.urlopen("article.html")
article = BeautifulSoup(data, 'html.parser')
articleF = article.find_all("p")
articleString = str(articleF)


#words = Counter()
#words.update(str(articleF).split())
#print words.most_common()





beginString = ("Mentions in today's news: ", '<br>')
militaryString = ("Military : ", str(articleF).count('military'), '<br>')
trumpString = ("Trump : ", str(articleF).count('Trump'), '<br>')
terroristString = ("Terrorist : ", str(articleF).count('terrorist'), '<br>')
russianString = ("Russia : ", str(articleF).count('Russia'), '<br>')
hackerString = ("Hacker : ", str(articleF).count('hacker'), '<br>')
corruptionString = ("Corruption : ", str(articleF).count('corruption'), '<br>')



with open("analysis.html", "w") as file:
	file.write('{% extends "personal/header.html" %} {% block content %}')

#The code block below is for determining the numbers in the statistics section
with open("analysis.html", "a") as file:
	file.write(str(beginString))
if (str(articleF).count('military') > 0):
	military = "military" 
	with open("analysis.html", "a") as file:
		file.write(str(militaryString))
if (str(articleF).count('Russian') > 0):
	russian = "Russians"
	with open("analysis.html", "a") as file:
		file.write(str(russianString))
if (str(articleF).count('Trump') > 0):
	Trump = "Trump"
	with open("analysis.html", "a") as file:
		file.write(str(trumpString))
if (str(articleF).count('hacker') > 0):
	with open("analysis.html", "a") as file:
		file.write(str(hackerString))
if (str(articleF).count('corruption') > 0):
	with open("analysis.html", "a") as file:
		file.write(str(corruptionString))
if (str(articleF).count('terrorist') > 0):
	with open("analysis.html", "a") as file:
		file.write(str(terroristString))


#This code block determines the focus of today's news
if (str(articleF).count('military') > 10):
	military = "military" 


if (str(articleF).count('Russian') > 10):
	russian = "Russians"

if (str(articleF).count('Trump') > 10):
	Trump = "Trump"

if (str(articleF).count('hacker') > 10):
	hacker = "Hackers"
if (str(articleF).count('corruption') > 10):
	corruption = "Corruption"

if (str(articleF).count('terrorist') > 10):
	terrorist = "Terrorists"




textString = ("Todays news is focused on ", military, "and", russian, "and", Trump, "and", hacker, "and", corruption, "and", terrorist)
with open("analysis.html", "a") as file:
	file.write(str(textString))
with open("analysis.html", "a") as file:
	file.write('{% endblock %}')

print ("Todays news is focused on ", military, "and", russian, "and", Trump, "and", hacker, "and", corruption, "and", terrorist)


