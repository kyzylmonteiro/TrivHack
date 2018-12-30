# -*- coding: utf-8 -*-
import urllib2
import webbrowser
from bs4 import BeautifulSoup
search_words=raw_input("Google Search: ").split()
#search_words=['']
search_words=	map(str.lower,search_words)
#print(search_words)
url='https://google.co.in/search?q='+'+'.join(map(str, search_words))
#print(url)
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
response = urllib2.urlopen(req)
source_code= response.read()
#print(source_code)


'''for opening a copy of the search'''
file = open('searched_page.html','w') 
file.write(source_code)
file.close()
#webbrowser.open("ws.html")


soup = BeautifulSoup(source_code, 'html.parser')
#print(soup.get_text())


cites=soup.find_all('cite')

for i in range(len(cites)):
	soup.cite.replace_with(' ')

scripts=soup.find_all('script')

for i in range(len(scripts)):
	soup.script.replace_with(' ')

styles=soup.find_all('style')

for i in range(len(styles)):
	soup.style.replace_with(' ')

source_code=soup.get_text('|',strip=True).lower()
print("----------------------------------------------")
print(source_code)
print("----------------------------------------------")

source_code=(source_code.lower()).encode('utf-8',"replace")
all_words=source_code.split()
separtors=[' ','<','>','/',':',';','=','?','+','"','|','\\','.']
for sep in separtors:
	all_words=sep.join(all_words)
	all_words=all_words.split(sep)


my_dict={}
my_dict['other']=0
res_words=['search','cached','google','others','list']
res_words.extend(search_words)
for word in all_words:
	if len(word)>3 and (word not in res_words):
		my_dict[word] = source_code.count(word)


#print(my_dict)
answer=list()
my_dict_copy=dict(my_dict)
print("\t\t\t\t\t\t\tAnswer is from:")
count=5
for c in range(count):
	buf=max(my_dict_copy, key=my_dict_copy.get)
	answer.append(buf)
	del my_dict_copy[max(my_dict_copy, key=my_dict_copy.get)]

for ans in answer:
	print("\t\t\t\t\t\t\t\t"+ans+" "+str(my_dict[ans]))

#If wrong ans
'''try:
	real_ans=raw_input("Real Ans:")
	print("Hits:"+str(my_dict[real_ans]))
except :
	print("Doesnt Exist! Please check spelling")'''
'''
#giving options
answer=[]
print("Please enter 3 options:") 
count=3
for c in range(count):
	answer.append(raw_input("option "+str(c)+": ").lower())

for ans in answer:
	try:
		print("\t\t\t\t\t\t\t\t"+ans+" "+str(my_dict[ans]))
	except:
		pass'''
