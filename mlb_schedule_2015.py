
# coding: utf-8

# In[124]:
tn=["ARI",
"ATL",
"BAL",
"BOS",
"CHC",
"CHW",
"CIN",
"CLE",
"COL",
"DET",
"HOU",
"KCR",
"LAA",
"LAD",
"MIA",
"MIL",
"MIN",
"NYM",
"NYY",
"OAK",
"PHI",
"PIT",
"SDP",
"SEA",
"SFG",
"STL",
"TBR",
"TEX",
"TOR",
"WSN"]
import os
import urllib2
import time
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv
import requests
df = pd.DataFrame({'a': ['rk'],
    'b':['boxscore'],
                       'c': ['tm'],
                      'd' : ['ha'],
                       
                   'e':['opp'],
                    'f':['r'],'g':['ra'],'h':['inn']})
df.to_csv("mlb_schedule_2015.csv",header=False,index=False)
def schedule(x):
    url='http://www.baseball-reference.com/teams/'+x+'/2015-schedule-scores.shtml'
    h = requests.get(url)
    text=h.content.decode('utf8')
    soup=BeautifulSoup(text)
    id=[];bs=[];tm=[];op=[];sc=[];osc=[];ip=[];hg=[]
    b=soup.find_all('tr',{'class':''})
    for i in b:
        if i.text.find('boxscore')!=-1:
            id.append(str(i).split('</td>')[1][str(i).split('</td>')[1].find('>')+1:])# id
            bs.append(str(i).split('</td>')[3][str(i).split('</td>')[3].find('<a href="/boxes/')+9:str(i).split('</td>')[3].find('">boxscore</a>')])#boxscore
            tm.append(str(i).split('</td>')[4].replace('<td align="left">','').replace('\n',''))#team
            hg.append(str(i).split('</td>')[5].replace('<td align="left">','').replace('\n',''))#host or guest
        
            op.append(str(i).split('</td>')[6][8+str(i).split('</td>')[6].find('.shtml">'):str(i).split('</td>')[6].find('</a>')])# o team
            sc.append(str(i).split('</td>')[8].replace('<td align="right">','').replace('\n','')) #score
            osc.append(str(i).split('</td>')[9].replace('<td align="right">','').replace('\n','')) #o score
            ip.append(str(i).split('</td>')[10][2+str(i).split('</td>')[10].find('">'):]) #ip

    df = pd.DataFrame({'a': id,
                       'b':bs,
                       'c':tm,
                      'd' :hg,
                   'e':op,
                   'f':sc,'g':osc,'h':ip                     
                       })
    df.to_csv("mlb_schedule_2015.csv",mode='a',header=False,index=False)     


# In[127]:

for i in tn:
    schedule(i)
    print i

