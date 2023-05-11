import bs4
import requests

# You can use any link of BBC news india article. To get text from blog.

headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
URL = "https://www.bbc.com/news/world-asia-india-65481927"
page = requests.get(URL, headers=headers)
# page = requests.get(URL, headers=headers, timeout=5)
# html = page.content

html = page.text
soup = bs4.BeautifulSoup(html,'html.parser')
# Only this thing is giving problem, I can see code on browser copy it manually,
# but not able to copy using request. I SOLVED IT.(HTTP Error 406: Not Acceptable)
# It looks at the requests (where it comes from) and if it determines that it is a bot
# you get a 406 error.The solution was to ask for the server IP to be whitelisted,
# or to send a special header to all server communication.

passage = ""
for p in soup.find_all('p'):
	# passage = passage + str(p)
	# passage = passage + p.text + "\n"
	passage = passage + p.text + "\n"

print(passage)
# print(passage[0])
# print(passage[0].text)

file = open("blog_text.txt", "w+")
for i in passage:
	file.write(i)
file.close()
