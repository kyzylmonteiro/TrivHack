# -*- coding: utf-8 -*-
import urllib2
import webbrowser
from bs4 import BeautifulSoup
import os 


def processing_input(Q,options):
	all_options_string=' '.join(map(str, options));
	word_ctr_dict=dict()
	for option in options:
		option=option.split()
		for o in option:
			word_ctr_dict[o]=all_options_string.count(o)
	options='|'.join(map(str, options));
	#print(options)
	for k in word_ctr_dict.keys():
		if word_ctr_dict[k]>1:
			options=options.replace(k,'')
			#print(k)
	options=options.split('|')
	#print(options)
	return Q,options



os.system('gnome-screenshot --file=images/input.png --area')
os.system('python main.py images/ .')
file = open('input.txt', 'r') 
input_data=file.read().lower() 
data=input_data.split('\n')

mode='na'
num_of_options=3
options=[]
Q=''
for i in range(len(data)):

	if len(data[i])>10 and mode=='na':
		Q=data[i]
		mode='q'
	elif mode=='q':
		Q=Q+' '+data[i]
	if (data[i]==' ' or data[i]=='') and mode!='na':
		mode='ans'

	if mode=='ans' and data[i]!='':
		options.append(data[i])
	if len(options)==num_of_options:
		break

Q=Q.split()
print(Q,options)

Q,options=processing_input(Q,options)

search_words=list()
hits=[0,0,0]
options.append('')
for option in options:
	search_words=list()
	search_words.extend(Q)
	search_words.extend(option.split())
	#search_words=map(str.lower,search_words)
	url='https://google.co.in/search?q='+'+'.join(map(str, search_words))
	print(url)
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
	response = urllib2.urlopen(req)
	source_code= response.read()

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

	source_code=soup.get_text(' ',strip=True).lower()

	for i in range(num_of_options):
		indi_hits=list()
		option_words=options[i].split()
		for option_word in option_words:
			indi_hits.append(source_code.count(option_word))
			print(source_code.count(option_word),option_word,option)
		max_count=max(indi_hits)
		print(max_count)
		hits[i]=hits[i]+max_count

print(hits)
if 'not' in ' '.join(map(str,Q)):
	for i in range(len(hits)):
		if hits[i]==min(hits):
			print(options[i])
else:
	for i in range(len(hits)):
		if hits[i]==max(hits):
			print(options[i])




