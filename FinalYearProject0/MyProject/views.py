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
import aspect_based_sentiment_analysis as absa
modal_list=[]
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
    nlp=absa_analysis()
    url1_url2_dict=scrapping(url1,url2,nlp)

    #  def analysis(){}
    
    
    #barvalues=showbar()
    #spectsdict.update(barvalues)
    
    #print(spectsdict)
    return render(request,'compare.html',url1_url2_dict)



def sortreviews(request) :

    idname = request.GET.get('idname', None)
    print(idname)
    reviewslist=[]
    if(idname=="like0"):
        reviewlist=modal_list[0]
    elif(idname=="dislike0"):
        reviewlist=modal_list[1]
    if(idname=="like1"):
        reviewlist=modal_list[10]
    elif(idname=="dislike1"):
        reviewlist=modal_list[11]
    if(idname=="like2"):
        reviewlist=modal_list[2]
    elif(idname=="dislike2"):
        reviewlist=modal_list[3]
    if(idname=="like3"):
        reviewlist=modal_list[12]
    elif(idname=="dislike3"):
        reviewlist=modal_list[13]
    if(idname=="like4"):
        reviewlist=modal_list[4]
    elif(idname=="dislike4"):
        reviewlist=modal_list[5]
    if(idname=="like5"):
        reviewlist=modal_list[14]
    elif(idname=="dislike5"):
        reviewlist=modal_list[15]
    if(idname=="like6"):
        reviewlist=modal_list[6]
    elif(idname=="dislike6"):
        reviewlist=modal_list[7]
    if(idname=="like7"):
        reviewlist=modal_list[16]
    elif(idname=="dislike7"):
        reviewlist=modal_list[17]
    if(idname=="like8"):
        reviewlist=modal_list[8]
    elif(idname=="dislike8"):
        reviewlist=modal_list[9]
    if(idname=="like9"):
        reviewlist=modal_list[18]
    elif(idname=="dislike9"):
        reviewlist=modal_list[19]
    reviewslist.append(idname)
    reviewslist.append("ChetamNIradwar")
    return JsonResponse(reviewslist,safe=False)

def scrapping(url1,url2,nlp) :
    
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
        #print(srcV1.get('src'))
        key_spects.append('url1_image')
        spects.append(url1_image)
        url1_spects_img_dict=dict(zip(key_spects,spects))
        #print(url1_spects_img_dict)

        #reviews scrapping
        # driver.execute_script('window.scroll(0,3500)')
        # sleep(1)
        # for t in soup1.findAll('a',attrs=({'href':re.compile("/product-reviews/")})) :
        #     q = t.get('href')
        #     link.append(q)
        # #print(link)

        # f_url=link.pop()
        # l_url=('https://www.flipkart.com'+str(f_url))
        # i=1
        # while i<=4:
        #     ss=driver.get(str(l_url)+'&page='+str(i))
        #     qq=driver.current_url
        #     r2=rq.get(qq)
        #     soup=BeautifulSoup(r2.text,'html.parser')
        #     for co in soup.find_all('div',{'class':'t-ZTKy'}) :
        #         cc=co.get_text()
        #         cl=cc.replace('READ MORE','')
                
        #         comment.append(cl)
        #     i=i+1
        driver.execute_script('window.scroll(0,3500)')
        link=[]
        comment=[]
        for t in soup1.findAll('a',attrs=({'class':'col-3-12 hXkZu- _1pxF-h','href':re.compile("/product-reviews/")})) :
            q = t.get('href')
            link.append(q)
        print(link)
        camera_link=link[0]
        battery_link=link[1]
        display_link=link[2]
        vfm_link=link[3]

        # print(camera_link)
        # print(vfm_link)
        camera_reviews=[]
        battery_reviews=[]
        display_reviews=[]
        vfm_reviews=[]
        performance_reviews=[]
         
        url1_camera_reviews=flipkart_scapper(camera_link,driver)
        url1_battery_reviews=flipkart_scapper(battery_link,driver)
        url1_display_reviews=flipkart_scapper(display_link,driver)
        url1_vfm_reviews=flipkart_scapper(vfm_link,driver)
        qq=driver.current_url
        r2=rq.get(qq)
        soup=BeautifulSoup(r2.text,'html.parser')
        per_review=soup.find('div',{'class':'_33iqLu'})
        for x in per_review.find_all('a',{'class':''}):
            # print(x)
            x = x.get('href')

        # print(x)
        performance_link=x

        url1_performance_reviews=flipkart_scapper(performance_link,driver)
        # print(url1_performance_reviews)
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
        # print(spects_set)
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
        
        # print(key_spects_set)
        #print(RAM1)
        

        #IMAGE sCRAPPING
        src=soup1.find('div',{'id':'dpx-btf-hlcx-comparison_feature_div'})
        src=src.find('div',{'class':'a-row a-spacing-top-medium'})
        #print(src)
        srcV1=src.find('img',{'class':'a-lazy-loaded'})
        srcV2=srcV1.get('data-src')
        spects_set.append('url1_image')
        key_spects_set.append(srcV2)
        

        url1_spects_img_dict=dict(zip(spects_set,key_spects_set))
        # print(url1_spects_img_dict)


        #reviews Scrapping
        driver.execute_script('window.scroll(0,3500)')
        for t in soup1.findAll('a',attrs={'data-hook':"see-all-reviews-link-foot"}):
            link.append(t['href'])
       
       
        #print('done')
        #print(link)
        f_url=link.pop()
        l_url=('https://www.amazon.in'+str(f_url))
        i=1
        while i<=4:
            ss=driver.get(str(l_url)+'&pageNumber='+str(i))
            qq=driver.current_url
            r2=rq.get(qq)
            soup=BeautifulSoup(r2.text,'html.parser')
            for co in soup.find_all('span',{'class':'a-size-base review-text review-text-content'}) :
                cc=co.get_text()
                comment.append(cc)
        i=i+1
        amz_all_reviews=comment
        cam=['camera','image','picture','photo','video','photography']
        bat=['battery','backup','drain','charging','mah']
        disp=['display','screen','density','resolution','ips','amoled']
        value_for_money =['value','price','money','cost','expensive']
        perfor=['processor','performance','game','graphic','COD']
        
        for text in amz_all_reviews:
            text=text.lower()
            if any(word in text for word in cam):
                url1_camera_reviews=text
            if any(word in text for word in bat):
                url1_display_reviews=text
            if any(word in text for word in disp):
                url1_battery_reviews=text
            if any(word in text for word in value_for_money):
                url1_vfm_reviews=text
            if any(word in text for word in perfor):
                url1_performance_reviews=text   
    # df=pd.DataFrame([comment]).transpose()
    # df.to_excel(r'C:\Users\Chetan Niradwar\ChetanProject\Documents\\reviews_url1.xlsx')
   
    # sentiment Classification
    url1_camera_list=sentiment_classify(url1_camera_reviews,'Camera',nlp)
    url1_battery_list=sentiment_classify(url1_battery_reviews,'Battery',nlp)
    url1_display_list=sentiment_classify(url1_display_reviews,'Display',nlp)
    url1_vfm_list=sentiment_classify(url1_vfm_reviews,'Money',nlp)
    url1_performance_list=sentiment_classify(url1_performance_reviews,'Performance',nlp)
    modal_list.append(url1_camera_list[0])
    modal_list.append(url1_camera_list[1])
    modal_list.append(url1_battery_list[0])
    modal_list.append(url1_battery_list[1])
    modal_list.append(url1_display_list[0])
    modal_list.append(url1_display_list[1])
    modal_list.append(url1_vfm_list[0])
    modal_list.append(url1_vfm_list[1])
    modal_list.append(url1_performance_list[0])
    modal_list.append(url1_performance_list[1])
    url1_dict={"url1_camera_per_pos_count":url1_camera_list[2],
    "url1_camera_per_neg_count":url1_camera_list[3],
    "url1_camera_pos_count":url1_camera_list[4],
    "url1_camera_neg_count":url1_camera_list[5],
    "url1_battery_per_pos_count":url1_battery_list[2],
    "url1_battery_per_neg_count":url1_battery_list[3],
    "url1_battery_pos_count":url1_battery_list[4],
    "url1_battery_neg_count":url1_battery_list[5],
    "url1_display_per_pos_count":url1_display_list[2],
    "url1_display_per_neg_count":url1_display_list[3],
    "url1_display_pos_count":url1_display_list[4],
    "url1_display_neg_count":url1_display_list[5],
    "url1_vfm_per_pos_count":url1_vfm_list[2],
    "url1_vfm_per_neg_count":url1_vfm_list[3],
    "url1_vfm_pos_count":url1_vfm_list[4],
    "url1_vfm_neg_count":url1_vfm_list[5],
    "url1_performance_per_pos_count":url1_performance_list[2],
    "url1_performance_per_neg_count":url1_performance_list[3],
    "url1_performance_pos_count":url1_performance_list[4],
    "url1_performance_neg_count":url1_performance_list[5]
    }


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
        
        # print(srcV1.get('src'))
        key_spects1.append('url2_image1')
        spects1.append(url2_image1)

        url2_spects_img_dict=dict(zip(key_spects1,spects1))
        #print(url2_spects_img_dict)
        #reviews scrapping
        # driver.execute_script('window.scroll(0,3500)')
        # sleep(1)
        # for t in soup1.findAll('a',attrs=({'href':re.compile("/product-reviews/")})) :
        #     q = t.get('href')
        #     link1.append(q)
        # #print(link)

        # f_url=link1.pop()
        # l_url=('https://www.flipkart.com'+str(f_url))
        # i=1
        # while i<=4:
        #     ss=driver.get(str(l_url)+'&page='+str(i))
        #     qq=driver.current_url
        #     r2=rq.get(qq)
        #     soup=BeautifulSoup(r2.text,'html.parser')
        #     for co in soup.find_all('div',{'class':'t-ZTKy'}) :
        #         cc=co.get_text()
        #         cl=cc.replace('READ MORE','')
                
        #         comment1.append(cl)
        #     i=i+1
        driver.execute_script('window.scroll(0,3500)')
        link=[]
        comment=[]
        for t in soup1.findAll('a',attrs=({'class':'col-3-12 hXkZu- _1pxF-h','href':re.compile("/product-reviews/")})) :
            q = t.get('href')
            link.append(q)
        # print(link)
        camera_link=link[0]
        battery_link=link[1]
        display_link=link[2]
        vfm_link=link[3]

        # print(camera_link)
        # print(vfm_link)
        camera_reviews=[]
        battery_reviews=[]
        display_reviews=[]
        vfm_reviews=[]
        performance_reviews=[]
 
        url2_camera_reviews=flipkart_scapper(camera_link,driver)
        url2_battery_reviews=flipkart_scapper(battery_link,driver)
        url2_display_reviews=flipkart_scapper(display_link,driver)
        url2_vfm_reviews=flipkart_scapper(vfm_link,driver)
        qq=driver.current_url
        r2=rq.get(qq)
        soup=BeautifulSoup(r2.text,'html.parser')
        per_review=soup.find('div',{'class':'_33iqLu'})
        for x in per_review.find_all('a',{'class':''}):
            # print(x)
            x = x.get('href')

        # print(x)
        performance_link=x

        url2_performance_reviews=flipkart_scapper(performance_link,driver)
        # print(url2_performance_reviews)
    
        
    else :
        header= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

        driver=webdriver.Chrome(executable_path=r"C:\Users\Chetan Niradwar\Downloads\chromedriver.exe")
        driver.maximize_window()
        driver.get(url2)
        r1=rq.get(url2,headers=header)
        soup1 =BeautifulSoup(r1.text,'html.parser')
        imgscrp1=BeautifulSoup(driver.page_source,'html.parser')
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
        

        url2_spects_img_dict=dict(zip(spects_set1,key_spects_set1))
        # print(url2_spects_img_dict)

        #reviews Scrapping
        driver.execute_script('window.scroll(0,3500)')
        
        for t in soup1.findAll('a',attrs={'data-hook':"see-all-reviews-link-foot"}):
            link1.append(t['href'])
        #print(link1) 
        f_url=link1.pop()
        l_url=('https://www.amazon.in'+str(f_url))  #chetan
        i=1
        while i<=4:
            ss=driver.get(str(l_url)+'&pageNumber='+str(i))
            qq=driver.current_url
            r2=rq.get(qq)
            soup=BeautifulSoup(r2.text,'html.parser')
            for co in soup.find_all('span',{'class':'a-size-base review-text review-text-content'}) :
                cc=co.get_text()
                comment1.append(cc)
            i=i+1
        amz_all_reviews=comment1
        cam=['camera','image','picture','photo','video','photography']
        bat=['battery','backup','drain','charging','mah']
        disp=['display','screen','density','resolution','ips','amoled']
        value_for_money =['value','price','money','cost','expensive']
        perfor=['processor','performance','game','graphic','COD']
        
        for text in amz_all_reviews:
            text=text.lower()
            if any(word in text for word in cam):
                url2_camera_reviews=text
            if any(word in text for word in bat):
                url2_display_reviews=text
            if any(word in text for word in disp):
                url2_battery_reviews=text
            if any(word in text for word in value_for_money):
                url2_vfm_reviews=text
            if any(word in text for word in perfor):
                url2_performance_reviews=text
    url2_camera_list=sentiment_classify(url2_camera_reviews,'Camera',nlp)
    url2_battery_list=sentiment_classify(url2_battery_reviews,'Battery',nlp)
    url2_display_list=sentiment_classify(url2_display_reviews,'Display',nlp)
    url2_vfm_list=sentiment_classify(url2_vfm_reviews,'Money',nlp)
    url2_performance_list=sentiment_classify(url2_performance_reviews,'Performance',nlp)
    modal_list.append(url2_camera_list[0])
    modal_list.append(url2_camera_list[1])
    modal_list.append(url2_battery_list[0])
    modal_list.append(url2_battery_list[1])
    modal_list.append(url2_display_list[0])
    modal_list.append(url2_display_list[1])
    modal_list.append(url2_vfm_list[0])
    modal_list.append(url2_vfm_list[1])
    modal_list.append(url2_performance_list[0])
    url2_dict={"url2_camera_per_pos_count":url2_camera_list[2],
    "url2_camera_per_neg_count":url2_camera_list[3],
    "url2_camera_pos_count":url2_camera_list[4],
    "url2_camera_neg_count":url2_camera_list[5],
    "url2_battery_per_pos_count":url2_battery_list[2],
    "url2_battery_per_neg_count":url2_battery_list[3],
    "url2_battery_pos_count":url2_battery_list[4],
    "url2_battery_neg_count":url2_battery_list[5],
    "url2_display_per_pos_count":url2_display_list[2],
    "url2_display_per_neg_count":url2_display_list[3],
    "url2_display_pos_count":url2_display_list[4],
    "url2_display_neg_count":url2_display_list[5],
    "url2_vfm_per_pos_count":url2_vfm_list[2],
    "url2_vfm_per_neg_count":url2_vfm_list[3],
    "url2_vfm_pos_count":url2_vfm_list[4],
    "url2_vfm_neg_count":url2_vfm_list[5],
    "url2_performance_per_pos_count":url2_performance_list[2],
    "url2_performance_per_neg_count":url2_performance_list[3],
    "url2_performance_pos_count":url2_performance_list[4],
    "url2_performance_neg_count":url2_performance_list[5]
    }        
    # df=pd.DataFrame([comment1]).transpose()
    # df.to_excel(r'C:\Users\Chetan Niradwar\ChetanProject\Documents\\reviews_url2.xlsx')
    url1_spects_img_dict.update(url2_spects_img_dict)
    url1_dict.update(url1_spects_img_dict)
    url1_dict.update(url2_dict)
    
    return url1_dict
    

     

def absa_analysis():
    name = 'absa/classifier-lapt-0.2'
    recognizer = absa.aux_models.BasicPatternRecognizer()
    nlp = absa.load(name,pattern_recognizer=recognizer)
    return nlp
 #   return 

def sentiment_classify(review_list,aspect,nlp):

    positive_count=0
    negative_count=0
    pos_review=[]
    neg_review=[]
    dis_per_pos_count=""
    dis_per_neg_count=""
    total_reviews=len(review_list)
    for each_review in review_list:
        completed_task = nlp(each_review, aspects=['Design',aspect])
        design,target= completed_task.examples
        sent=target.sentiment
        sentV2=str(sent)
        sentV3=sentV2[10:]
        if (sentV3=="positive"):
            positive_count=positive_count + 1
            pos_review.append(each_review)
        else:
            negative_count=negative_count + 1
            neg_review.append(each_review)
    per_pos_count=(positive_count/total_reviews)*100
    per_neg_count=100-per_pos_count
    #to Display in html format
    dis_per_pos_count= 'style="width:'+str(per_pos_count)+'%;"'
    dis_per_neg_count= 'style="width:'+str(per_neg_count)+'%;"'
    return [pos_review,neg_review,dis_per_pos_count,dis_per_neg_count,positive_count,negative_count]

def flipkart_scapper(apsect_link,driver):
    review_list=[]
    l_url=('https://www.flipkart.com'+str(apsect_link))
    i=1
    while i<=1:
        ss=driver.get(str(l_url)+'&page='+str(i))
        qq=driver.current_url
        r2=rq.get(qq)
        soup=BeautifulSoup(r2.text,'html.parser')
        for co in soup.find_all('div',{'class':'t-ZTKy'}) :
            cc=co.get_text()
            cc=cc.replace('...','')
            cl=cc.replace('READ MORE','')

            
            review_list.append(cl)
        i=i+1
    return review_list
