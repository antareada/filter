from xml.dom.minidom import *
import re

xml = parse('messenger_oldictionary.xml')
regs = []

# Взять значения по тегу и поместить в список
def getTag(name):
	dictionary = xml.getElementsByTagName(name)
	for node in dictionary:
	    regs.append(node.firstChild.nodeValue)

# Вывести список регулярок
def viewRegsList():
	for i in regs:
		print(i)

# Поиск по тексту регуляркой
def searchRegText(reg, text):
	match = re.match(reg, text)
	if match:
		print(match.group())

# Перебор всех регулярок
def searchRegs(regs, text):
	for reg in regs:
		for word in text:
			searchRegText(reg, word)

f = open('text.txt', 'r')

# Точно текст
text = f.read()
text = text.lower()
# В список по словам текст
text = text.split()

getTag('badWordSet')
getTag('include')
getTag('exclude')

searchRegs(regs, text)