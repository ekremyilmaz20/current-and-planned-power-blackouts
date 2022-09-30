
import requests as req
import json
from bs4 import BeautifulSoup as bs
import pandas as pd



while 1:

    secim=input("Toroslar Anlık için 1,Toroslar Planlı için 2,Niğde için 3,Çıkmak İçin 0 :")
    if int(secim)==3:
        ilce_url=[ 
              "https://cc.meramedas.com.tr/services/publicdata.ashx?m=mrm_gb1&il=51&ilce=1876&mahalle=",
              "https://cc.meramedas.com.tr/services/publicdata.ashx?m=mrm_gb1&il=51&ilce=1201&mahalle=",
              "https://cc.meramedas.com.tr/services/publicdata.ashx?m=mrm_gb1&il=51&ilce=1225&mahalle=",
              "https://cc.meramedas.com.tr/services/publicdata.ashx?m=mrm_gb1&il=51&ilce=1904&mahalle=",
              "https://cc.meramedas.com.tr/services/publicdata.ashx?m=mrm_gb1&il=51&ilce=1544&mahalle=",
              "https://cc.meramedas.com.tr/services/publicdata.ashx?m=mrm_gb1&il=51&ilce=1700&mahalle="]


        with pd.ExcelWriter("NigdeKesinti.xlsx",mode='w', engine="openpyxl") as writer:
            kesintiler=[]
            print("Niğde Planlanan Kesintiler Excel'e Aktarılıyor....")
            for ilce in ilce_url:
                with req.get(ilce) as rq:
                    data = json.loads(rq.text)
                    if data==[]:
                        continue
                    kesintiler.extend(data)
            df = pd.DataFrame(data=kesintiler)
            df.to_excel(writer, index=False)
        print("Niğde Planlı Kesintiler Excel Hazır!")
    elif int(secim)==2:
        ilkodu={'01':['00001757','00001219','00002033','00001329','00001806','00001437','00001443','00001486','00001580','00001588','00002032','00001104','00001687','00001734','00001748'],       
            '27':['00001139','00001415','00001956','00001546','00001974','00001549','00001841','00001844','00001720'],      
            '31':['00001131','00002080','00002081','00001887','00002082','00001289','00001792','00001382','00001413','00001468','00001970','00002083','00001585','00001591','00001721'],
            '79':['00002023','00001476','00002024'],
            '33':['00002064','00001135','00001766','00001779','00001892','00001311','00001366','00002065','00001536','00001621','00001665','00002066','00002067'],
            '80':['00001165','00001743','00002027','0000142','00001560','00002028','00002029']     
           }
        with pd.ExcelWriter("ToroslarElektrik.xlsx",mode='w', engine="openpyxl") as writer:
            kesintiler=[]
            print("Toroslar A.Ş Planlanan Kesintiler Excel'e Aktarılıyor....")
            print("Bu işlem 10 dakika kadar sürebilir...")
            for key,value in ilkodu.items():

                for i in value:
                    url = 'https://online.toroslaredas.com.tr/wkt-sorgulama'

                    kurum='?Kurum=7500&SorguTipi=2&'
                    ik='IlKodu='+key+'&'
                    ilce='IlceKodu='+i
                    url=url+kurum+ik+ilce

                    data=req.post(url)
                    data = json.loads(data.text)
                    data=data['result']
                    data=data['planlananKesintiListe']
                    if data==[]:
                        continue
                    kesintiler.extend(data)
            df = pd.DataFrame(data=kesintiler)            
            df.to_excel(writer, index=False)            
        print("Toroslar A.Ş Planlı Kesşntiler Excel Hazır")    
    elif int(secim)==1:


        ilkodu={'01':['00001757','00001219','00002033','00001329','00001806','00001437','00001443','00001486','00001580','00001588','00002032','00001104','00001687','00001734','00001748'],       
            '27':['00001139','00001415','00001956','00001546','00001974','00001549','00001841','00001844','00001720'],      
            '31':['00001131','00002080','00002081','00001887','00002082','00001289','00001792','00001382','00001413','00001468','00001970','00002083','00001585','00001591','00001721'],
            '79':['00002023','00001476','00002024'],
            '33':['00002064','00001135','00001766','00001779','00001892','00001311','00001366','00002065','00001536','00001621','00001665','00002066','00002067'],
            '80':['00001165','00001743','00002027','0000142','00001560','00002028','00002029']     
           }


        with pd.ExcelWriter("ToroslarElektrik-Anlık.xlsx",mode='w', engine="openpyxl") as writer:
            kesintiler=[]
            print("Toroslar A.Ş Anlık Kesintiler Excel'e Aktarılıyor....")
            print("Bu işlem 10 dakika kadar sürebilir...")
            for key,value in ilkodu.items():

                for i in value:
                    url = 'https://online.toroslaredas.com.tr/wkt-sorgulama'

                    kurum='?Kurum=7500&SorguTipi=2&'
                    ik='IlKodu='+key+'&'
                    ilce='IlceKodu='+i
                    url=url+kurum+ik+ilce

                    data=req.post(url)
                    data = json.loads(data.text)
                    data=data['result']
                    data=data['mevcutKesintiListe']
                    if data==[]:
                        continue
                    kesintiler.extend(data)
            df = pd.DataFrame(data=kesintiler)            
            df.to_excel(writer, index=False)            
        print("Toroslar A.Ş Anlık Kesşntiler Excel Hazır")
        
    elif int(secim)==0:
        print("Programdan Çıkılıyor...")
        break
    else:
        prınt("Lütfen 1,2 yada 3'e basınız...")
        
        

