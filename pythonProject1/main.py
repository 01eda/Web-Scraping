import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
""""
conn=sqlite3.connect('N11.db')
c=conn.cursor()
#c.execute('''CREATE TABLE pro (link TEXT,isim TEXT,fiyat TEXT,bellek kapasitesi TEXT) ''')
#toplamUrunSayisi =0
for sayfaNumarasi in range(1,6):
   # headers={Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36}
    url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?m=Lenovo-Asus-HP-Dell-Msi-Monster-Apple-Casper-Acer-Huawei&ipg=" +str(sayfaNumarasi)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    urunler =soup.find_all("li", attrs={"class":"column"})


    for urun in urunler:
       urunAdi=urun.a.get("title")
       urunLink=urun.a.get("href")
       urunFiyati = urun.ins.text
       #print("Ürün Adı:{}".format(urunAdi))
       #print("Ürün Linki:{}".format(urunLink))
       #print("Ürün Fiyatı:{}".format(urunFiyati))

       try:
           urun_r = requests.get(urunLink)
       except Exception:
           print("urun detayi bulunamadi")

       urunDetayı_soup1 = BeautifulSoup(urun_r.content, "lxml")

       n11ozellikDetaylari = urunDetayı_soup1.find_all("li",attrs={"class":"unf-prop-list-item"})

       for n11Ozellik in n11ozellikDetaylari.find_all("p", attrs={"class": "unf-prop-list-title"},text="Bellek Kapasitesi"):
           print( n11Ozellik.find("p", attrs={"class": "unf-prop-list-prop"}))

       temp_list = ['Optik Sürücü','USB (Type-C)','Pil Gücü','USB','Ekran Kartı Türü','Bluetooth Desteği','İşlemci Çekirdek Sayısı','İşlemci Hızı',
                    'Bellek Türü','Ürün Tipi','Ekran Çözünürlüğü','İşlemci Modeli','Ekran Kartı Belleği','HDMI','Parmak izi Okuyucu','Ağırlık']
       temp_dict = {}
       count = 0
       for n11Ozellik in n11ozellikDetaylari:
           baslık1 = n11Ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text
           ozellik1 =n11Ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text
           if baslık1 not in temp_list:
                temp_dict[baslık1] = ozellik1
                if len(temp_dict) > 1:
                    count += 1
                print("{}:{}".format(list(temp_dict.keys())[count], list(temp_dict.values())[count]))

  --------------------------------------------------------------------------------------------
    for ozellik in ozellikler:
        print(ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text,end=":")
        print(ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text)
    print("--------------")

    urunPuan = urun_soup.find_all("div",attrs={"class":"unf-review-rating"}).select
    for puan in urunPuan:
       print(puan.find("strong", attrs={"class":"ratingScore"}))

   # print("puan", end=":")
   #print(urunPuan)

#conn=sqlite3.connect('vatan1.db')
#c=conn.cursor()
#c.execute('''CREATE TABLE pro(link TEXT,isim TEXT,fiyat TEXT,pil TEXT,islemci TEXT) ''')
"""
for sayfaNumarasi3 in range(1,3):
   # headers={Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36}
    url3 = "https://www.vatanbilgisayar.com/notebook/?page=" +str(sayfaNumarasi3)
    response3 = requests.get(url3)
    soup3 = BeautifulSoup(response3.content, "lxml")
    urunler3 =soup3.find_all("div", attrs={"class":"product-list product-list--list-page"})

    for vatanurun in urunler3:
        vatanUrunLink=vatanurun.a.get("href")
        vatanUrunLinkBasi="https://www.vatanbilgisayar.com/"
        vatanLinkTamami=vatanUrunLinkBasi+vatanUrunLink
        vatanUrunAdi=vatanurun.h3.text
        vatanUrunFiyat=vatanurun.find("span", attrs={"class":"product-list__price"}).text
        print("Ürün Adı:{}".format(vatanUrunAdi))
        print("Ürün link:{}".format(vatanLinkTamami))
        print("Ürün Fiyat:{}".format(vatanUrunFiyat))

        try:
            urun_r3 = requests.get(vatanLinkTamami)
        except Exception:
            print("urun detayi bulunamadi")

        urunDetayı_soup3 = BeautifulSoup(urun_r3.content, "lxml")

        ozellikDetaylari3 = urunDetayı_soup3.find_all("table", attrs={"class": "product-table"})
        #hepsi=urunDetayı_soup3.find_all("tr",attrs={"data-count":"0"})
        


        temp_list = ['İşlemci Hızı','İşlemci Numarası','İşlemci Çekirdek Sayısı','Ram Tipi','Full HD','HD','TN','Dokunmatik Ekran',
                     'IPS','Ekran Yenileme Hızı','Ekran Özellikleri','Çözünürlük (Piksel)']
        temp_dict = {}
        count = 0
        for ozellik in ozellikDetaylari3:
            a = ozellik.td.text
            b = ozellik.p.text
            if a not in temp_list:
                temp_dict[a] = b
                if len(temp_dict) > 1:
                    count += 1
                print("{}:{}".format(list(temp_dict.keys())[count], list(temp_dict.values())[count]))
                
        print("--------------")

"""
    #c.execute('''INSERT INTO pro VALUES(?,?,?,?,?)''',(vatanLinkTamami, vatanUrunAdi, vatanUrunFiyat, a,b))
    #conn.commit()


conn = sqlite3.connect('vatan.db')
c = conn.cursor()
c.execute('''CREATE TABLE prod(link TEXT,isim TEXT,fiyat TEXT) ''')
#c.execute('''INSERT INTO prod VALUES (?,?,?)''',(vatanUrunAdi,vatanLinkTamami,vatanUrunFiyat))
conn.commit()
"""