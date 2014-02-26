from xml.dom.minidom import *
import re

xml = parse('messenger_oldictionary.xml')
regsInclude = []
regsExclude = []

# Взять значения по тегу и поместить в список
def getTag(name, listReg):
	dictionary = xml.getElementsByTagName(name)
	for node in dictionary:
	    listReg.append(node.firstChild.nodeValue)

# Вывести список регулярок
def viewRegsList(listReg):
	for i in listReg:
		print(i)

# Поиск по тексту регуляркой
def searchRegText(reg, text):
	match = re.match(reg, text)
	if match:
		print(match.group())

# Перебор всех регулярок из списка
def searchRegs(regs, text):
	for reg in regs:
		for word in text:
			searchRegText(reg, word)

f = open('text.txt', 'r')

# Точно текст
text = f.read()
text = text.lower()
text = text.replace('.', '')
print(text)

# В список по словам текст
text = text.split()



print('То, что забанит:')
getTag('badWordSet', regsInclude)
getTag('include', regsInclude)
print('То, что не забанит как исключение:')
getTag('exclude', regsExclude)

searchRegs(regsInclude, text)