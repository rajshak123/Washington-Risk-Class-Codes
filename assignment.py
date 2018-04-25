import requests
import re
url='http://apps.leg.wa.gov/wac/default.aspx?cite=296-17A&full=true'
import bs4
page=requests.get(url)
soup=bs4.BeautifulSoup(page.content,"lxml")
d=soup.select("#ctl00_ContentPlaceHolder1_dlSectionContent > span")
d2=[str(i) for i in d]
d3=[bs4.BeautifulSoup(i,"lxml") for i in d2]
pattern=re.compile(r'(\d{4}-\d{2})(.*)')
a={}
for j in d3:
    k=j.find_all("span",attrs={"style": "font-weight:bold;text-indent:0in;"})   
    for l in k:
        if len(l)>0:
             mat=re.match(pattern,str(l.contents[0]))
             if mat:
                a[mat.group(1)]=mat.group(2)


file = open('output.txt','w') 
file.write(str(a))
file.close()
