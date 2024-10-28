import pandas as pd
import pywhatkit as kit
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def ogrenci_ekle():
    ogrenci_no = input("Öğrenci Numarası: ")
    ogrenci_ad = input("Öğrenci Adı: ")
    veli_ad = input("Veli Adı: ")
    veli_tel = input("Veli Telefon No: ")
    sinav1 = int(input("1. Sınav: "))
    sinav2 = int(input("2. Sınav: "))
    performans = int(input("Performans: "))
    proje = int(input("Proje: "))
    sinav3 = (performans + proje) / 2
    ortalama = (sinav1 + sinav2 + sinav3) / 3
    devamsizlik = int(input("Devamsızlık: "))
    
    ogrenci = {
        "Öğrenci No": ogrenci_no,
        "Öğrenci Adı": ogrenci_ad,
        "Veli Adı": veli_ad,
        "Veli Telefon": veli_tel,
        "1. Sınav": sinav1,
        "2. Sınav": sinav2,
        "3. Sınav": sinav3,
        "Ortalama": ortalama,
        "Devamsızlık": devamsizlik
    }
    return ogrenci

def ogrenci_ara(ogrenci_no, ogrenciler):
    for ogrenci in ogrenciler:
        if ogrenci["Öğrenci No"] == ogrenci_no:
            return ogrenci
    return None

def ogrenci_duzenle(ogrenci_no, ogrenciler):
    ogrenci = ogrenci_ara(ogrenci_no, ogrenciler)  # Öğrenci arama fonksiyonunu çağırıyoruz
    if ogrenci:
        # Her bir bilgi için kullanıcıya güncelleme fırsatı veriyoruz.
        ogrenci["Öğrenci Adı"] = input(f"Yeni Öğrenci Adı ({ogrenci['Öğrenci Adı']}): ") or ogrenci["Öğrenci Adı"]
        ogrenci["Veli Adı"] = input(f"Yeni Veli Adı ({ogrenci['Veli Adı']}): ") or ogrenci["Veli Adı"]
        ogrenci["Veli Telefon"] = input(f"Yeni Veli Telefon No ({ogrenci['Veli Telefon']}): ") or ogrenci["Veli Telefon"]
        ogrenci["1. Sınav"] = input(f"Yeni 1. Sınav Notu ({ogrenci['1. Sınav']}): ") or ogrenci["1. Sınav"]
        ogrenci["2. Sınav"] = input(f"Yeni 2. Sınav Notu ({ogrenci['2. Sınav']}): ") or ogrenci["2. Sınav"]
        ogrenci["Performans"] = input(f"Yeni Performans Notu ({ogrenci['Performans']}): ") or ogrenci["Performans"]
        ogrenci["Proje"] = input(f"Yeni Proje Notu ({ogrenci['Proje']}): ") or ogrenci["Proje"]

        print("Öğrenci bilgileri başarıyla güncellendi.")
    else:
        print("Öğrenci bulunamadı.")

def ogrenci_sil(ogrenci_no, ogrenciler):
    ogrenci = ogrenci_ara(ogrenci_no, ogrenciler)
    if ogrenci:
        ogrenciler.remove(ogrenci)
        print(f"{ogrenci_no} numaralı öğrenci silindi.")
    else:
        print("Öğrenci bulunamadı.")

def rapor_olustur(sinif, ogrenciler):
    # Seçilen sınıfa ait öğrencileri filtreleyelim
    secilen_sinif_ogrencileri = [ogrenci for ogrenci in ogrenciler if ogrenci['Sınıf'] == sinif]

    # Eğer o sınıfta öğrenci yoksa bilgi mesajı verelim
    if not secilen_sinif_ogrencileri:
        print(f"{sinif} sınıfında öğrenci bulunamadı.")
        return

    # Rapor dizini ve PDF dosyasını oluşturalım
    rapor_dizini = f"Raporlarim/{sinif}/"
    if not os.path.exists(rapor_dizini):
        os.makedirs(rapor_dizini)

    pdf_dosyasi = os.path.join(rapor_dizini, f"{sinif}_Not_Raporu.pdf")
    c = canvas.Canvas(pdf_dosyasi)

    # Başlık
    c.setFont("Helvetica", 16)
    c.drawString(100, 800, f"{sinif} Sınıfı Not Raporu")

    y = 780
    c.setFont("Helvetica", 12)  # Varsayılan fonta devam ediliyor
    for ogrenci in secilen_sinif_ogrencileri:
        c.drawString(100, y, f"Öğrenci No: {ogrenci['Öğrenci No']}")
        y -= 20
        c.drawString(100, y, f"Adı: {ogrenci['Öğrenci Adı']}")
        y -= 20
        c.drawString(100, y, f"Ortalama: {ogrenci['Ortalama']}")
        y -= 20
        c.drawString(100, y, "-" * 30)  # Ayracı çiziyoruz
        y -= 20

    c.save()
    print(f"PDF raporu başarıyla oluşturuldu: {pdf_dosyasi}")

def veli_bilgilendir(ogrenci_no, ogrenciler):
    ogrenci = ogrenci_ara(ogrenci_no, ogrenciler)
    if ogrenci:
        telefon = ogrenci['Veli Telefon']
        
        # Telefon numarasının +90 ile başlayıp başlamadığını kontrol et
        if not telefon.startswith("+90"):
            telefon = "+90" + telefon
        
        # Öğrenci bilgileriyle birlikte detaylı mesaj oluştur
        mesaj = (f"Merhaba {ogrenci['Veli Adı']}, {ogrenci['Öğrenci Adı']}'nın güncel bilgileri aşağıdadır:\n"
                 f"Sınıf: {ogrenci.get('Sınıf', 'Bilgi yok')}\n"
                 f"Öğrenci No: {ogrenci['Öğrenci No']}\n"
                 f"1. Sınav: {ogrenci.get('1. Sınav', 'Henüz girilmedi')}\n"
                 f"2. Sınav: {ogrenci.get('2. Sınav', 'Henüz girilmedi')}\n"
                 f"3. Sınav (Performans+Proje): {ogrenci.get('3. Sınav', 'Henüz hesaplanmadı')}\n"
                 f"Ortalama: {ogrenci.get('Ortalama', 'Henüz hesaplanmadı')}\n"
                 f"Devamsızlık: {ogrenci['Devamsızlık']}\n")

        try:
            kit.sendwhatmsg_instantly(telefon, mesaj)
            print("Mesaj gönderildi.")
        except Exception as e:
            print(f"Mesaj gönderilemedi: {e}")
    else:
        print("Öğrenci bulunamadı.")

def tum_velileri_bilgilendir(ogrenciler):
    # Her öğrenci için mesaj oluştur ve gönder
    for ogrenci in ogrenciler:
        telefon = ogrenci['Veli Telefon']
        
        # Telefon numarasının +90 ile başlayıp başlamadığını kontrol et
        if not telefon.startswith("+90"):
            telefon = "+90" + telefon
        
        # Öğrenci bilgileriyle birlikte detaylı mesaj oluştur
        mesaj = (f"Merhaba {ogrenci['Veli Adı']}, {ogrenci['Öğrenci Adı']}'nın güncel bilgileri aşağıdadır:\n"
                 f"Sınıf: {ogrenci.get('Sınıf', 'Bilgi yok')}\n"
                 f"Öğrenci No: {ogrenci['Öğrenci No']}\n"
                 f"1. Sınav: {ogrenci.get('1. Sınav', 'Henüz girilmedi')}\n"
                 f"2. Sınav: {ogrenci.get('2. Sınav', 'Henüz girilmedi')}\n"
                 f"3. Sınav (Performans+Proje): {ogrenci.get('3. Sınav', 'Henüz hesaplanmadı')}\n"
                 f"Ortalama: {ogrenci.get('Ortalama', 'Henüz hesaplanmadı')}\n"
                 f"Devamsızlık: {ogrenci['Devamsızlık']}\n")

        try:
            # WhatsApp mesajını gönder
            kit.sendwhatmsg_instantly(telefon, mesaj)
            print(f"{ogrenci['Veli Adı']} için mesaj gönderildi.")
        except Exception as e:
            print(f"{ogrenci['Veli Adı']} için mesaj gönderilemedi: {e}")


