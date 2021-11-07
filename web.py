import requests
from bs4 import BeautifulSoup
import re

file1 = open("web_urls.txt","a", encoding='utf-8')
file2 = open("emails.txt","a", encoding='utf-8')
file3 = open("ph_numbers.txt","a", encoding='utf-8')

def web_crawler():
    url = 'https://nitsri.ac.in/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    #Converting the plain text to beautifulSoup object.
    for link in soup.findAll('a'):
        if (link.get('href') != '#' and link.get('href') != 'None'):
            if (str(link.get('href'))[0:4] != 'http' and str(link.get('href'))[0:4] != 'mail'):
                new_url = "https://nitsri.ac.in/" + str(link.get('href'))
                file1.write(new_url)
                file1.write('\n')
                url_data(new_url) 



def url_data(url):
    source_code = requests.get(url)
    pattern1 = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b') #for emails 
    pattern2 = re.compile(r'((\+)((0[ -])|((91 )))((\d{12})+|(\d{10})+))|\d{5}([- ]*)\d{6}') #for mobile numbers 
    matches1 = re.finditer(pattern1,str(source_code.text))
    matches2 = re.finditer(pattern2,str(source_code.text))
    for match in matches1: #find emails and store in text file
       file2.write(match.group(0))
       file2.write('\n')
    for match in matches2:  #find number and store in etx file 
        file3.write(match.group(0))
        file3.write('\n')
       
web_crawler()

file1.close()
file2.close()
file3.close()

print("websiite scrapeed succuessfullyy \n emails and maoblies numbers are also saved ")