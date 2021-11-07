from bs4 import BeautifulSoup
import re
import requests

print("Going through all links ")
html_text = requests.get("https://nitsri.ac.in/").text


li = []
soup = BeautifulSoup(html_text, 'lxml')
for urls in soup.find_all('a'):
    li.append(urls.get('href'))

print(" Phone Numbers are:  ")
for link in li:
    try:
        pg_text1 = requests.get(link).text
        pat1 = '\d\d\d\d\d\d\d\d\d\d'
        match = re.findall(pat1, pg_text1)
        if match == None:
            pass
        else:
            if match!=[]:
                print(match)
    except:
        pass

# for link in li:
#     try:
#         pg_text2=requests.get(link).text
#         pat2='\w+@\w\.\w'
#         match=re.search(pat2,pg_text2)
#         if match==None:
#             pass
#         else:
#             print(match.group())
#     except:
#         pass

try:
    pat1 = '\d\d\d\d\d\d\d\d\d\d'
    match = re.findall(pat1, html_text)
    if match == None:
        pass
    else:
        print(match)
except:
    pass