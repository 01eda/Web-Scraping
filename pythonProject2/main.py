import requests
from bs4 import BeautifulSoup
import pandas as pd
"""""#toplamUrunSayisi =0
for sayfaNumarasi in range(1,2):
#headers={Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36}
    url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?ipg="+str(sayfaNumarasi)
    response = requests.get(url)
    #html_icerigi = response.content
    soup = BeautifulSoup(response.content, "lxml")
    urunler =soup.find_all("li", attrs={"class":"column"})


for urun in urunler:
    urunAdi=urun.a.get("title")
    urunLink=urun.a.get("href")
    print(urunAdi)
    print(urunLink)
    try:
        urun_r = requests.get(urunLink)
        #toplamUrunSayisi +=1
    except Exception:
        print("urun detayi bulunamadi")

    urun_soup = BeautifulSoup(urun_r.content, "lxml")
    ozellikler = urun_soup.find_all("li",attrs={"class":"unf-prop-list-item"})

    for ozellik in ozellikler:
        print(ozellik.find("p",attrs={"class":"unf-prop-list-title"}).text,end=":")
        print(ozellik.find("p",attrs={"class":"unf-prop-list-prop"}).text)
    print("--------------")

    urunPuan = urun_soup.find_all("div",attrs={"class":"unf-review-rating"}).select
    for puan in urunPuan:
       print(puan.find("strong", attrs={"class":"ratingScore"}))

   # print("puan", end=":")
   #print(urunPuan)

#print("toplam ürün sayısı}".format(toplamUrunSayisi) )

for sayfaNumarasi1 in range(1,4):
    url1 ="https://www.trendyol.com/sr?wb=102323%2C101606%2C101849%2C104964%2C105536%2C103505%2C101470%2C102324%2C103502%2C107655%2C794&wc=103108&pi="+str(sayfaNumarasi1)
    response1 = requests.get(url1)
    soup1 = BeautifulSoup(response1.content, "lxml")
    urunler1 = soup1.find_all("div", attrs={"class":"p-card-wrppr with-campaign-view"})

#header ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    for urun1 in urunler1:
        urunLink1 = urun1.find_all("div", attrs={"class":"p-card-chldrn card-border"})
        link= urun1.a.get("href")
        linkBasi="https://www.trendyol.com/"
        linkTamami= linkBasi+link
       # print(linkTamami)
        trendyolUrunAdi=urun1.find("div", attrs={"class":"prdct-desc-cntnr"}).text
        trendyolUrunFiyati=urun1.find("div", attrs={"class":"prc-box-dscntd"}).text
        trendyolUrunMarka=urun1.find("span", attrs={"class":"prdct-desc-cntnr-ttl"}).text

        print("Ürün Adı:{}".format(trendyolUrunAdi))
        print("Ürün Markası:{}".format(trendyolUrunMarka))
        print("Ürün Fiyatı: {}".format(trendyolUrunFiyati))
        print("Ürün Linki: {}".format(linkTamami))

        try:
            urunDetayı=requests.get(linkTamami)
        except Exception:
            print("ürün yok")

        urunDetayı_soup= BeautifulSoup(urunDetayı.content, "lxml")
        TrendyolOzellikDetayları = urunDetayı_soup.find_all("li", attrs={"class": "detail-attr-item"})

        temp_list = ['Garanti Tipi', 'Çözünürlük', 'Kullanım Amacı', 'Cihaz Ağırlığı','Ekran Kartı','Ekran Yenileme Hızı','Ekran Kartı Tipi',
                     'Ekran Kartı Hafızası','Çözünürlük Standartı','İşlemci Çekirdek Sayısı','Hard Disk Kapasitesi','Dokunmatik Ekran','Optik Sürücü Tipi','Garanti Süresi',
                     'Çözünürlük Standartı','Klavye','Bağlantılar','Ekran Kartı Bellek Tipi','Arttırılabilir Azami Bellek','Panel Tipi']
        temp_dict = {}
        count = 0
        for TrendyolOzellik in TrendyolOzellikDetayları:
            baslık=TrendyolOzellik.span.text
            ozellik=TrendyolOzellik.b.text
            if baslık not in temp_list:
                temp_dict[baslık] = ozellik
                if len(temp_dict) > 1:
                    count += 1
                print("{}:{}".format(list(temp_dict.keys())[count],list(temp_dict.values())[count]))
        print("--------------")

"""


for sayfaNumarasi in range(1,3):
  headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
  urlHepsiburada = requests.get("https://www.hepsiburada.com/ara?q=bilgisayar&filtreler=MainCategory.Id:98&markalar=asus,lenovo,hp,dell,acer,monster,msi,casper&kategori=2147483646_3000500_98&sayfa=2"+str(sayfaNumarasi),headers=headers)
  soupH=BeautifulSoup(urlHepsiburada.content,"lxml")
  HepsiburadaSt=soupH.find_all("li",attrs={"class":"productListContent-zAP0Y5msy8OHn5z7T_K_"})

  for hepsiburadaUrun in HepsiburadaSt:
    urunH=hepsiburadaUrun.find_all("div", attrs={"class":"moria-ProductCard-joawUM crKXus suniny6gqv9"})
    hepsiburadaLink=hepsiburadaUrun.a.get("href")
    hepsiburadaLinkBası="https://www.hepsiburada.com/"
    hepsiburadaLinkTamamı=hepsiburadaLinkBası+hepsiburadaLink
    hepsiburadaUrunAdı=hepsiburadaUrun.a.get("title")
    print(hepsiburadaLinkTamamı)
    print(hepsiburadaUrunAdı)

    linkIci=requests.get(hepsiburadaLinkTamamı,headers=headers)
    soupH1=BeautifulSoup(linkIci.content,"lxml")

    PuanH=soupH1.find_all("span", attrs={"data-bind":"text: product().currentListing.merchantRatingSummary.lifeTimeRating.toFixed(1).toString().replace('.',','), css: product().currentListing.merchantRatingSummary.cssClass"})
    for span in PuanH:
      puan=(span.text)

    fiyatHepsiburada=soupH1.find_all("span", attrs={"data-bind":"markupText:'currentPriceBeforePoint'"})
    for span in fiyatHepsiburada:
      fiyat=(span.text)

    hepsiburadaResim=soupH1.img.get("src")
    print("ürün resmi:{}".format(hepsiburadaResim))
    print("ürün fiyatı:{}".format(fiyat))
    print("ürün puanı:{}".format(puan))


    #hepsiburadaOzellik=soupH1.find("table",attrs={"class ":"data-list tech-spec"})
    hepsi=soupH1.find("table",attrs={"class":"data-list tech-spec"})

    temp_list = ['İşlemci Hızı', 'İşlemci Numarası', 'İşlemci Çekirdek Sayısı', 'Ram Tipi', 'Full HD', 'HD', 'TN',
                 'Dokunmatik Ekran',
                 'IPS', 'Ekran Yenileme Hızı', 'Ekran Özellikleri', 'Çözünürlük (Piksel)']
    temp_dict = {}
    count = 0
    for ozellik in hepsi:
        a = ozellik.th.text
        b = ozellik.span.text
        if a not in temp_list:
            temp_dict[a] = b
            if len(temp_dict) > 1:
                count += 1
            print("{}:{}".format(list(temp_dict.keys())[count], list(temp_dict.values())[count]))
    print("--------------")






