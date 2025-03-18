import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/audio-video/pr?sid=0pm&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_87b365c5-fa78-44e2-814a-e570c7ac9620_1_372UD5BXDFYS_MC.9JGNW7M0TUHD&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Electronics~Audio~All_9JGNW7M0TUHD&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=9JGNW7M0TUHD")
print(response)
soup=BeautifulSoup(response.content,"html.parser")
print(soup)
names=soup.find_all('a',class_="wjcEIp")
print(names)
name_list = []
for i in names:
    d = i.get_text()
    name_list.append(d)
print(name_list)

prices=soup.find_all('div',class_="Nx9bqj")
price= []
for i in prices:
    d = i.get_text()
    price.append(d)
print(price)

ratings=soup.find_all('div',class_="XQDdHH")
rating= []
for i in ratings:
    d = i.get_text()
    rating.append(float(d))
print(rating)

links=soup.find_all('img',class_="Rza2QY")
link= []
for i in links:
    d ="https://www.flipkart.com/"+ i['src']
    link.append(d)
print(link)

hii={"names":pd.Series(name_list),
      "prices":pd.Series(price),
      "ratings":pd.Series(rating),
      "link":pd.Series(link),
     }
print(data)
df = pd.DataFrame()
df = pd.DataFrame(hii)
df.to_csv("flipkart_item.csv")
