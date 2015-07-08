
# coding: utf-8

# In[ ]:

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
'''
df = pd.DataFrame({'a': ['gab'],
    'b':['gh'],
                       'c': ['gbb'],
                      'd' : ['gso'],
                       
                   'e':['gslg'],
                    'f':['ghbp'],'g':['gsf'],'h':['gip'],
         'i': ['ger'],
   'j': ['hab'],
    'k':['hh'],
                       'l': ['hbb'],
                      'm' : ['hso'],
                       
                   'n':['hslg'],
                    'o':['hhbp'],'p':['hsf'],'q':['hip'],
         'r': ['her'],'s':['url']       
                  
                  
                  
                  })

df.to_csv("mlb_boxscore_2015.csv",header=False,index=False)
'''
def boxscore(x):
    url='http://www.baseball-reference.com'+x
    h = requests.get(url)
    text=h.content.decode('utf8')
    soup=BeautifulSoup(text)
    b=soup.find_all('tr',{'class':'normal_text stat_total'})
    b1=soup.find_all('tbody')
    gab=b[0].text.split('\n')[2] #gab
    gh=b[0].text.split('\n')[4] #gh
    gbb=b[0].text.split('\n')[6] #gbb
    gso=b[0].text.split('\n')[7] #gso
    gslg=b[0].text.split('\n')[11] #gslg
    #ghbp=sum(map(lambda x: x=='HBP',','.join(map(lambda x: x.text,BeautifulSoup(str(b1[0])).find_all('td',{'align':''}))).split(','))) #ghbp
    #gsf=sum(map(lambda x: x=='SF',','.join(map(lambda x: x.text,BeautifulSoup(str(b1[0])).find_all('td',{'align':''}))).split(','))) #gsf
    o=','.join(map(lambda x: x.text,BeautifulSoup(str(b1[0])).find_all('td',{'align':''}))).split(',')
    for i in o:
        if i.find(u'\xb7SF')!=-1:
        
            o.remove(i)
            for j in range(int(i.split(u'\xb7')[0])):
                o.append(u'SF')
    for i in o:
        if i.find(u'\xb7HBP')!=-1:
        
            o.remove(i)
            for j in range(int(i.split(u'\xb7')[0])):
                o.append(u'HBP') 
    ghbp=sum(map(lambda x: x=='HBP',o))   
    gsf=sum(map(lambda x: x=='SF',o)) 
    gip=b[2].text.split('\n')[2].strip() #gip
    ger=b[2].text.split('\n')[5] #ger
    hab=b[1].text.split('\n')[2] #hab
    hh=b[1].text.split('\n')[4] #hh
    hbb=b[1].text.split('\n')[6] #hbb
    hso=b[1].text.split('\n')[7] #hso
    hslg=b[1].text.split('\n')[11] #hslg
    #hhbp=sum(map(lambda x: x=='HBP',','.join(map(lambda x: x.text,BeautifulSoup(str(b1[1])).find_all('td',{'align':''}))).split(','))) #hhbp
    #hsf=sum(map(lambda x: x=='SF',','.join(map(lambda x: x.text,BeautifulSoup(str(b1[1])).find_all('td',{'align':''}))).split(','))) #hsf
    o=','.join(map(lambda x: x.text,BeautifulSoup(str(b1[1])).find_all('td',{'align':''}))).split(',')
    for i in o:
        if i.find(u'\xb7SF')!=-1:
        
            o.remove(i)
            for j in range(int(i.split(u'\xb7')[0])):
                o.append(u'SF')
    for i in o:
        if i.find(u'\xb7HBP')!=-1:
        
            o.remove(i)
            for j in range(int(i.split(u'\xb7')[0])):
                o.append(u'HBP') 
    hhbp=sum(map(lambda x: x=='HBP',o))   
    hsf=sum(map(lambda x: x=='SF',o)) 
    hip=b[3].text.split('\n')[2].strip() #hip
    her=b[3].text.split('\n')[5] #her
    df = pd.DataFrame({'a': [gab],
    'b':[gh],
                       'c': [gbb],
                      'd' : [gso],
                       
                   'e':[gslg],
                    'f':[ghbp],'g':[gsf],'h':[gip],
         'i': [ger],
   'j': [hab],
    'k':[hh],
                       'l': [hbb],
                      'm' : [hso],
                       
                   'n':[hslg],
                    'o':[hhbp],'p':[hsf],'q':[hip],
         'r': [her],'s':[x]       
                  
                  
                  
                  })
    df.to_csv("mlb_boxscore_2015.csv",mode='a',header=False,index=False)     

f=open("mlb_schedule_2015.csv")
ex=[]
for row in csv.reader(f):
    ex.append('shane'.join(row))
source=[i.split('shane')[1] for i in ex][1:]
source=list(set(source))
f=open("mlb_boxscore_2015.csv")
exx=[]
for row in csv.reader(f):
    exx.append('shane'.join(row).split('shane')[18])
source= filter(lambda x: x not in exx,source)   
    
j=0
for i in source:
    try:
        boxscore(i)
    except Exception as e:
        print(e)    
    j=j+1
    print j, len(source)

