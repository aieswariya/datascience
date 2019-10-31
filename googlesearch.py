# import requests
# from bs4 import BeautifulSoup
# try: 
#     from googlesearch import search
# except ImportError:  
#     print("No module named 'google' found") 
  

# query = "A computer science portal"
  
# for j in search(query, tld="com", num=10, stop=1, pause=2): 
#     print(j) 


import requests 
import webbrowser
from bs4 import BeautifulSoup

user=input("enter to search:")
print("googleing....")
search=requests.get("https://www.google.com/search?q="+''+user)
soup=BeautifulSoup(search.text,'lxml')
search_results=soup.select(' .kCrYT  a')
for link in search_results[:10]:
    actual_link=link(href)
    webbrowser.open('https://google.com/'+actual_link)


    