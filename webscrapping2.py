import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
#import csv
res=requests.get('https://www.houzz.co.uk/professionals/c/Khordha--Orissa--India')
res1=requests.get('https://www.houzz.co.uk/professionals/interior-designers/kyora-interiors-pfvwgb-pf~1763463127')
res2=requests.get('https://www.houzz.co.uk/hznb/professionals/architects-and-building-designers/arcon-design-studio-pfvwin-pf~1991637156')
res3=requests.get('https://www.houzz.co.uk/professionals/architects-and-building-designers/kitsch-interior-pfvwgb-pf~690304459')
res4=requests.get('https://www.houzz.co.uk/hznb/professionals/architects-and-building-designers/iamchandansahoo-pfvwus-pf~153172375')
res5=requests.get('https://www.houzz.co.uk/hznb/professionals/cad-planning/biswaranjan-pfvwin-pf~1169239113')
res6=requests.get('https://www.houzz.co.uk/professionals/architects-and-building-designers/roots-architect-pfvwgb-pf~1704893829')
res7=requests.get('https://www.houzz.co.uk/hznb/professionals/architects-and-building-designers/r-p-infra-pfvwin-pf~973628114')
res8=requests.get('https://www.houzz.co.uk/hznb/professionals/architects-and-building-designers/anukul-pfvwus-pf~596859642')
res9=requests.get('https://www.houzz.co.uk/hznb/professionals/architects-and-building-designers/m-architect-pfvwin-pf~1543819109')
res10=requests.get('https://www.houzz.co.uk/hznb/professionals/cad-planning/stark-industry-pfvwin-pf~1168940913')
res11=requests.get('https://www.houzz.co.uk/hznb/professionals/building-designers-and-architectural-technologists/creative-builder-pfvwin-pf~1292870533')
res12=requests.get('https://www.houzz.co.uk/hznb/professionals/architects-and-building-designers/artisan-house-pfvwin-pf~1166154513')
res13=requests.get('https://www.houzz.co.uk/hznb/professionals/cad-planning/kiran-manna-pfvwin-pf~2016204579')
res14=requests.get('https://www.houzz.co.uk/hznb/professionals/architects-and-building-designers/praveen-pradhan4-pfvwin-pf~1136013370')
res15=requests.get('https://www.houzz.co.uk/hznb/professionals/architects-and-building-designers/blue-arrow-tectonic-pvtltd-pfvwus-pf~505520800')
res16=requests.get('https://www.houzz.co.uk/hznb/professionals/cad-planning/lisha-pfvwin-pf~95497125')
res17=requests.get('https://www.houzz.co.uk/hznb/professionals/architects-and-building-designers/t-and-m-associates-pfvwus-pf~1041351132')
res18=requests.get('https://www.houzz.co.uk/hznb/professionals/interior-designers/ashutosh-samal-pfvwin-pf~599258618')
res19=requests.get('https://www.houzz.co.uk/hznb/professionals/interior-designers/a-b-plywoods-pfvwin-pf~1579577248')
res20=requests.get('https://www.houzz.co.uk/hznb/professionals/interior-designers/interio-dezires-pfvwus-pf~1705003045')
res21=requests.get('https://www.houzz.co.uk/hznb/professionals/interior-designers/sjn-civil-lines-pfvwin-pf~663470016')
res22=requests.get('https://www.houzz.co.uk/hznb/professionals/interior-designers/helios-enterprise-pfvwus-pf~1888914611')
res23=requests.get('https://www.houzz.co.uk/hznb/professionals/interior-designers/sunil-rout-pfvwin-pf~95094093')
res24=requests.get('https://www.houzz.co.uk/hznb/professionals/interior-designers/pilfer-pfvwus-pf~689385147')
res25=requests.get('https://www.houzz.co.uk/hznb/professionals/interior-designers/designers-touch-pfvwus-pf~2015113959')

soup=BeautifulSoup(res.text,'lxml')
soup1=BeautifulSoup(res1.text,'lxml')
soup2=BeautifulSoup(res2.text,'lxml')
soup3=BeautifulSoup(res3.text,'lxml')
soup4=BeautifulSoup(res4.text,'lxml')
soup5=BeautifulSoup(res5.text,'lxml')
soup6=BeautifulSoup(res6.text,'lxml')
soup7=BeautifulSoup(res7.text,'lxml')
soup8=BeautifulSoup(res8.text,'lxml')
soup9=BeautifulSoup(res9.text,'lxml')
soup10=BeautifulSoup(res10.text,'lxml')
soup11=BeautifulSoup(res11.text,'lxml')
soup12=BeautifulSoup(res12.text,'lxml')
soup13=BeautifulSoup(res13.text,'lxml')
soup14=BeautifulSoup(res14.text,'lxml')
soup15=BeautifulSoup(res15.text,'lxml')
soup16=BeautifulSoup(res16.text,'lxml')
soup17=BeautifulSoup(res17.text,'lxml')
soup18=BeautifulSoup(res18.text,'lxml')
soup19=BeautifulSoup(res19.text,'lxml')
soup20=BeautifulSoup(res20.text,'lxml')
soup21=BeautifulSoup(res21.text,'lxml')
soup22=BeautifulSoup(res22.text,'lxml')
soup23=BeautifulSoup(res23.text,'lxml')
soup24=BeautifulSoup(res24.text,'lxml')
soup25=BeautifulSoup(res25.text,'lxml')
name_of_businesss=[]
categorys=[]
websites=[]
phone_numbers=[]

for link in soup.find_all('div' , attrs={'class':'hz-professionals-navigation-tables__table'}):
  name_of_business=link.find('div', attrs={'class':'hz-professionals-navigation-tables__table-header header-6 text-bold mt0 mbm'})
  #first_name_of_business=link.find('div', attrs={'class':'hz-text-clamp__text-node'})
  name_of_businesss.append(name_of_business.getText())
  #first_name_of_businesss.append(first_name_of_business.getText())

for l in soup.find_all('div' , attrs={'class':'hz-professionals-navigation-tables__column col-sm-3'}):
  category=l.find('span', attrs={'class':'hz-color-link__text'})
  categorys.append(category.getText())


for n in soup1.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website.get('value'))

for i in soup1.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number.getText())

for n in soup2.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website1=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website1.get('value'))

for i in soup2.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number1=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number1.getText())


for n in soup3.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website2=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website2.get('value'))

for i in soup3.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number2=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number2.getText())

for n in soup4.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website3=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website3.get('value'))

for i in soup4.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number3=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number3.getText())

for n in soup5.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website4=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website4.get('value'))

for i in soup5.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number4=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number4.getText())

for n in soup6.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website5=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website5.get('value'))

for i in soup6.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number5=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number5.getText())

for n in soup7.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website6=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website5.get('value'))

for i in soup7.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number6=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number6.getText())

for n in soup8.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website7=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website7.get('value'))

for i in soup8.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number7=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number7.getText())

for n in soup9.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website8=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website8.get('value'))

for i in soup9.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number8=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number8)

for n in soup10.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website9=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website9.get('value'))

for i in soup10.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number9=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number9.getText())

for n in soup11.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website10=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website10.get('value'))

for i in soup11.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number11=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number11.getText())

for n in soup12.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website11=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website11.get('value'))

for i in soup12.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number11=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number11.getText())  

for n in soup13.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website12=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website12.get('value'))

for i in soup13.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number12=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number12.getText())

for n in soup14.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website13=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website13.get('value'))

for i in soup14.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number13=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number13.getText())

for n in soup15.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website14=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website14.get('value'))

for i in soup15.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number14=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number14.getText())

for n in soup16.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website15=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website15.get('value'))

for i in soup16.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number15=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number15.getText())

for n in soup17.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website16=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website16.get('value'))

for i in soup17.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number16=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number16.getText())

for n in soup18.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website17=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website17.get('value'))

for i in soup18.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number17=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number17.getText())

for n in soup19.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website18=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website18.get('value'))

for i in soup19.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number18=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number18.getText())

for n in soup20.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website19=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website19.get('value'))

for i in soup20.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number19=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number19)

for n in soup21.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website20=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website20.get('value'))

for i in soup21.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number20=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number20.getText())

for n in soup22.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website21=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website21.get('value'))

for i in soup22.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number21=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number21.getText())

for n in soup23.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website22=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website22.get('value'))

for i in soup23.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number22=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number22.getText())

for n in soup24.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website23=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website23.get('value'))

for i in soup24.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number23=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number23.getText())

for n in soup25.find_all('div' ,  attrs={'class':'profile-url-share text-center'}):
  website24=n.find(attrs={'class':'profile-url-share__url-input'})
  websites.append(website24.get('value'))

for i in soup25.find_all('div' ,  attrs={'class':'hz-profile-header__contact-info text-right mrm'}):
  phone_number24=i.find('a', attrs={'class':'hz-profile-header__contact-method hz-track-me'})
  phone_numbers.append(phone_number24.getText())


# df = pd.DataFrame({ 'Name of Business':[name_of_businesss],'Category':[category] ,'Website':[website] ,'phone_number':[phone_number]}) 
# df.to_csv('usa1.csv',index=False)

#print(name_of_businesss)
#print(categorys)
#print(websites)
#print(phone_numbers)
# print(ratings)
#df = pd.DataFrame({ 'Name of Business':name_of_businesss , 'category':categorys }) 
#df.to_csv('usa.csv',index=False)

a = {'Name of Business':name_of_businesss , 'category':categorys ,'website':websites ,'Phone_Number':phone_numbers }
df = pd.DataFrame.from_dict(a,orient='index')
df.transpose()
df.to_csv('uk1.csv')



