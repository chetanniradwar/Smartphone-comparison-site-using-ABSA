from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import numpy
from selenium import webdriver
from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
from time import sleep
import re

# Create your views here.
def home(request):
    return render(request, 'home.html')

def compare(request) :
    return render(request,'compare.html')

def about(request):
    return render(request,'about.html')

def outputcompare(request):
    url1=request.POST['url1']
    url2=request.POST['url2']
    spectsdict=scrapping(url1,url2)

    #  def analysis(){}
    
    
    barvalues=showbar()
    spectsdict.update(barvalues)
    
    #print(spectsdict)
    return render(request,'compare.html',spectsdict)



def sortreviews(request) :
    idname = request.GET.get('idname', None)
    print(idname)
    reviewslist=[]
    reviewslist.append(idname)
    reviewslist.append("ChetamNIradwar")
    return JsonResponse(reviewslist,safe=False)

def scrapping(url1,url2) :
    
    comment=[]
    comment1=[]
    link=[]
    link1=[] 
    spects=[]
    key_spects=[]
    key_spects1=[]
    spects1=[]
    if "flipkart.com" in url1 :
        driver=webdriver.Chrome(executable_path=r"C:\Users\Chetan Niradwar\Downloads\chromedriver.exe")
        driver.maximize_window()
        driver.get(url1)
        
        r1=rq.get(url1)
        soup1 =BeautifulSoup(r1.text,'html.parser')
        imgscrp=BeautifulSoup(driver.page_source,'html.parser')
        #specifications scrapping
        RAM= soup1.find_all('li',{'class':'_21lJbe'})
        for ele in RAM:
            ram=ele.get_text()
            spects.append(ram)
        Keys=soup1.find_all('td',{'class':'_1hKmbr col col-3-12'})
        for key in Keys:
            k=key.get_text()
            k=k.replace(" ","")
            key_spects.append(k)
        #print(key_spects)
        #dict1=dict(zip(key_spects,spects))
       
        #image scrapping
        src=imgscrp.find('div',{'class':'_1BweB8'})
        srcV1=src.find('img',{'class':'_396cs4 _2amPTt _3qGmMb _3exPp9'})
        url1_image=srcV1.get('src')
        print(srcV1.get('src'))
        key_spects.append('url1_image')
        spects.append(url1_image)
        dict1=dict(zip(key_spects,spects))
        #print(dict1)
        #reviews scrapping
        driver.execute_script('window.scroll(0,3500)')
        sleep(1)
        for t in soup1.findAll('a',attrs=({'href':re.compile("/product-reviews/")})) :
            q = t.get('href')
            link.append(q)
        #print(link)

        f_url=link.pop()
        l_url=('https://www.flipkart.com'+str(f_url))
        i=1
        while i<=1:
            ss=driver.get(str(l_url)+'&page='+str(i))
            qq=driver.current_url
            r2=rq.get(qq)
            soup=BeautifulSoup(r2.text,'html.parser')
            for co in soup.find_all('div',{'class':'t-ZTKy'}) :
                cc=co.get_text()
                cl=cc.replace('READ MORE','')
                
                comment.append(cl)
            i=i+1
        
    else :
        header= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        driver=webdriver.Chrome(executable_path=r"C:\Users\Chetan Niradwar\Downloads\chromedriver.exe")
        driver.maximize_window()
        driver.get(url1)
        r1=rq.get(url1,headers=header)
        soup1 = BeautifulSoup(r1.text,'html.parser')
        soup1 =BeautifulSoup(driver.page_source,'html.parser')
        #spects scrapping
        RAM1= soup1.find_all('div',{'class':'attribute-heading-label'})
        spects=[]
        for ele1 in RAM1:
                    ram1=ele1.get_text()
                    newram=ram1.replace("\n","")
                    spects.append(newram)
        spects_set = [] 
        for i in spects: 
            if i not in spects_set: 
                spects_set.append(i)
        spects_set[0]="PrimaryCamera"
        spects_set[3]="ResolutionType"
        spects_set[4]="BatteryCapacity"
        spects_set[6]="InternalStorage"
        spects_set[8]="ProcessorType"
        spects_set[10]="WarrantySummary"
        spects_set[15]="OtherFeatures"
       
        
        #print(spects_set)
        key_spects=[]
        RAM2= soup1.find_all('td',{'class':'base-item-column'})
        for ele1 in RAM2:
                    ram1=ele1.get_text()
                    newram=ram1.replace("\n","")
                    key_spects.append(newram)
        

        key_spects_set = [] 
        for i in key_spects: 
            if i not in key_spects_set: 
                key_spects_set.append(i)
        
        #print(key_spects_set)
        #print(RAM1)
        

        #IMAGE sCRAPPING
        src=soup1.find('div',{'id':'dpx-btf-hlcx-comparison_feature_div'})
        src=src.find('div',{'class':'a-row a-spacing-top-medium'})
        #print(src)
        srcV1=src.find('img',{'class':'a-lazy-loaded'})
        srcV2=srcV1.get('data-src')
        spects_set.append('url1_image')
        key_spects_set.append(srcV2)
        

        dict1=dict(zip(spects_set,key_spects_set))
        print(dict1)


        #reviews Scrapping
        driver.execute_script('window.scroll(0,3500)')
        for t in soup1.findAll('a',attrs={'data-hook':"see-all-reviews-link-foot"}):
            link.append(t['href'])
       
       
        #print('done')
        #print(link)
        f_url=link.pop()
        l_url=('https://www.amazon.in'+str(f_url))
        i=1
        while i<=1:
            ss=driver.get(str(l_url)+'&pageNumber='+str(i))
            qq=driver.current_url
            r2=rq.get(qq)
            soup=BeautifulSoup(r2.text,'html.parser')
            for co in soup.find_all('span',{'class':'a-size-base review-text review-text-content'}) :
                cc=co.get_text()
                comment.append(cc)
            i=i+1
    df=pd.DataFrame([comment]).transpose()
    df.to_excel(r'C:\Users\Chetan Niradwar\ChetanProject\Documents\\reviews_url1.xlsx')

    if "flipkart.com" in url2 :
        driver=webdriver.Chrome(executable_path=r"C:\Users\Chetan Niradwar\Downloads\chromedriver.exe")
        driver.maximize_window()
        driver.get(url2)
        
        r1=rq.get(url2)
        soup1 =BeautifulSoup(r1.text,'html.parser')
        imgscrp1=BeautifulSoup(driver.page_source,'html.parser')

        RAM1= soup1.find_all('li',{'class':'_21lJbe'})
        for ele1 in RAM1:
            ram1=ele1.get_text()
            spects1.append(ram1)
        Keys1=soup1.find_all('td',{'class':'_1hKmbr col col-3-12'})
        for key1 in Keys1:
            k=key1.get_text()
            k=k.replace(" ","")
            k=k+"1"
            key_spects1.append(k)
        #print(key_spects1)
        
        #image scrapping
        src=imgscrp1.find('div',{'class':'_1BweB8'})
        srcV1=src.find('img',{'class':'_396cs4 _2amPTt _3qGmMb _3exPp9'})
        url2_image1=srcV1.get('src')
        
        print(srcV1.get('src'))
        key_spects1.append('url2_image1')
        spects1.append(url2_image1)

        dict2=dict(zip(key_spects1,spects1))
        #print(dict2)
        #reviews scrapping
        driver.execute_script('window.scroll(0,3500)')
        sleep(1)
        for t in soup1.findAll('a',attrs=({'href':re.compile("/product-reviews/")})) :
            q = t.get('href')
            link1.append(q)
        #print(link)

        f_url=link1.pop()
        l_url=('https://www.flipkart.com'+str(f_url))
        i=1
        while i<=2:
            ss=driver.get(str(l_url)+'&page='+str(i))
            qq=driver.current_url
            r2=rq.get(qq)
            soup=BeautifulSoup(r2.text,'html.parser')
            for co in soup.find_all('div',{'class':'t-ZTKy'}) :
                cc=co.get_text()
                cl=cc.replace('READ MORE','')
                
                comment1.append(cl)
            i=i+1
        
    else :
        header= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

        driver=webdriver.Chrome(executable_path=r"C:\Users\Chetan Niradwar\Downloads\chromedriver.exe")
        driver.maximize_window()
        driver.get(url2)
        r1=rq.get(url2,headers=header)
        soup1 =BeautifulSoup(r1.text,'html.parser')
        imgscrp1=BeautifulSoup(driver.page_source,'htmal.parser')
        #spects scrapping
        RAM1= soup1.find_all('div',{'class':'attribute-heading-label'})
        spects1=[]
        for ele1 in RAM1:
                    ram1=ele1.get_text()
                    newram=ram1.replace("\n","")
                    newram=newram+"1"
                    spects1.append(newram)
        spects_set1 = [] 
        for i in spects1: 
            if i not in spects_set1: 
                spects_set1.append(i)
        spects_set1[0]="PrimaryCamera1"
        spects_set1[3]="ResolutionType1"
        spects_set1[4]="BatteryCapacity1"
        spects_set1[6]="InternalStorage1"
        spects_set1[8]="ProcessorType1"
        spects_set1[10]="WarrantySummary1"
        spects_set1[15]="OtherFeatures1"
       
        
        #print(spects_set)
        key_spects1=[]
        RAM2= soup1.find_all('td',{'class':'base-item-column'})
        for ele1 in RAM2:
                    ram1=ele1.get_text()
                    newram=ram1.replace("\n","")
                    key_spects1.append(newram)
        

        key_spects_set1 = [] 
        for i in key_spects1: 
            if i not in key_spects_set1:
                key_spects_set1.append(i)
        
        #print(key_spects_set)
        #print(RAM1)
        

        #IMAGE sCRAPPING
        src=imgscrp1.find('div',{'id':'dpx-btf-hlcx-comparison_feature_div'})
        src=src.find('div',{'class':'a-row a-spacing-top-medium'})
        #print(src)
        srcV1=src.find('img',{'class':'a-lazy-loaded'})
        srcV2=srcV1.get('data-src')
        spects_set1.append('url1_image')
        key_spects_set1.append(srcV2)
        

        dict2=dict(zip(spects_set1,key_spects_set1))
        print(dict2)

        #reviews Scrapping
        driver.execute_script('window.scroll(0,3500)')
        
        for t in soup1.findAll('a',attrs={'data-hook':"see-all-reviews-link-foot"}):
            link1.append(t['href'])
        #print(link1) 
        f_url=link1.pop()
        l_url=('https://www.amazon.in'+str(f_url))
        i=1
        while i<=3:
            ss=driver.get(str(l_url)+'&pageNumber='+str(i))
            qq=driver.current_url
            r2=rq.get(qq)
            soup=BeautifulSoup(r2.text,'html.parser')
            for co in soup.find_all('span',{'class':'a-size-base review-text review-text-content'}) :
                cc=co.get_text()
                comment1.append(cc)
            i=i+1
    df=pd.DataFrame([comment1]).transpose()
    df.to_excel(r'C:\Users\Chetan Niradwar\ChetanProject\Documents\\reviews_url2.xlsx')
    dict1.update(dict2)
    return dict1

     

#def analysis():

 #   return 

def showbar():
    likes=10
    dislikes=50
    total=likes+dislikes
    perlikes=(likes/total)*100
    perdislikes=(dislikes/total)*100
    url1_aspect1_percentageLikes= 'style="width:'+str(perlikes)+'%;"'
    url1_aspect1_percentageDislikes= 'style="width:'+str(perdislikes)+'%;"'
    likes=230
    dislikes=500
    total=likes+dislikes
    perlikes=(likes/total)*100
    perdislikes=(dislikes/total)*100
    url2_aspect1_percentageLikes= 'style="width:'+str(perlikes)+'%;"'
    url2_aspect1_percentageDislikes= 'style="width:'+str(perdislikes)+'%;"'

    barvalue={"url1_aspect1_percentageLikes":url1_aspect1_percentageLikes, "url1_aspect1_percentageDislikes":url1_aspect1_percentageDislikes,
    "url2_aspect1_percentageLikes":url2_aspect1_percentageLikes, "url2_aspect1_percentageDislikes":url2_aspect1_percentageDislikes}
    return barvalue