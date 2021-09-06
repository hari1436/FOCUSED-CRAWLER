import requests
from bs4 import BeautifulSoup
import re
import time
import os

def spider(seed_url):
	main_page = 'https://en.wikipedia.org/wiki/Main_Page'
	crawled_count = 0
	max_depth = 1
	frontier_urls = [seed_url]
	seen_urls = []
	newpath = r'Logs' 
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	crawler_log = open("Logs/crawler_log.txt","w")
	crawler_log.write("Seed : "+seed_url+"\n\n")
	crawler_log.write("Depth 1 :\n\n")
	crawled_count+=1
	crawler_log.write(str(crawled_count)+") "+seed_url+"\n\n")
	flag = True
	print("\n----------------------------------------- At depth 1--------------------------------------------------------")
	print(str(crawled_count)+") "+seed_url)
	source_code = requests.get(seed_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")
	for depth in range (2, 7):
		if flag:
			print("\n----------------------------------------- At depth "+str(depth)+"--------------------------------------------------------")
			crawler_log.write("Depth "+str(depth)+" :\n\n")
			extracted_urls = []
			for frontier_url in frontier_urls:
				if flag:
					source_code = requests.get(frontier_url)
					plain_text = source_code.text
					soup = BeautifulSoup(plain_text,"html.parser")
					for link in soup.find_all('a', href=re.compile('^/wiki/')):
						#crawling only 250 url links
						if crawled_count < 250 and flag:
							url_text = link.text
							href_url = link.get('href')
							if ':' not in href_url:
								if '#' not in href_url:
									url = 'https://en.wikipedia.org'+href_url
									if url not in frontier_urls and url not in extracted_urls and url not in seen_urls and url != main_page:
										time.sleep(1)
										source_code = requests.get(url)
										plain_text = source_code.text
										soup = BeautifulSoup(plain_text,"html.parser")
										
										extracted_urls.append(url)
										crawled_count+=1
										crawler_log.write(str(crawled_count)+") "+url+"\n")
										print(str(crawled_count)+") "+url)

								else:
									# Handle URLs with '#'
									hash_pos = href_url.index('#')

									# Trim the URL from the start till index before '#'
									url = 'https://en.wikipedia.org'+href_url[:hash_pos]

									# URL should not be in either of Frontier, Extracted or Seen lists and should not be Wiki Main Page too
									if url not in frontier_urls and url not in extracted_urls and url not in seen_urls and url != main_page:
										
										# Respecting the Politeness Policy
										time.sleep(1)

										# get the soup
										source_code = requests.get(url)
										plain_text = source_code.text
										soup = BeautifulSoup(plain_text,"html.parser")
										extracted_urls.append(url)
										crawled_count+=1
										crawler_log.write(str(crawled_count)+") "+url+"\n")
										print(str(crawled_count)+") "+url)


						else:
							flag = False
							print("Limit of 250Ls reached")
							max_depth = depth
							break
					seen_urls.append(frontier_url)
			if len(extracted_urls) == 0:
				print("No matching URLs at Depth "+str(depth)+"\n")
				crawler_log.write("No matching URLs at Depth "+str(depth)+"\n\n")
				flag = False
				max_depth = depth
				break
			frontier_urls = extracted_urls
			crawler_log.write("\n")

	# Maximum depth of Depth 6 reached		
	if flag:
		print("Searched till max depth 6")
		max_depth = 6

	crawler_log.write("------------------------------------------------------------------------------------\n")
	crawler_log.write("Logistics :\n\n")
	crawler_log.write("Number of matching searches : "+str(crawled_count)+"\n")
	crawler_log.write("Maximum depth reached : Depth "+str(max_depth)+"\n")

seed_url = 'https://en.wikipedia.org/wiki/Tropical_cyclone'
spider(seed_url)
