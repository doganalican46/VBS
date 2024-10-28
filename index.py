import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from interface import ogrenci_ara, veli_bilgilendir, rapor_olustur, tum_velileri_bilgilendir
from tkinter import ttk
ogrenciler = []

# Ana pencere oluşturma
root = tk.Tk()
root.title("VBS - Ahmet Doymuş")
root.geometry("800x550")

# Arka planı siyah yapma
root.configure(bg='black')

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = screen_width // 2 - size[0] // 2
    y = screen_height // 2 - size[1] // 2
    window.geometry(f"{size[0]}x{size[1]}+{x}+{y}")

# Tüm pencereleri ortalamak için global bir fonksiyon kullanıyoruz
def position_dialog(dialog):
    center_window(dialog)

# Başlık ekleme
title_label = tk.Label(root, text="VBS - Ahmet Doymuş", font=("Arial", 20), bg='black', fg='white')
title_label.pack(pady=20)

def load_students():
    global ogrenciler
    try:
        with open('ogrenciler.txt', 'r') as f:
            for line in f:
                values = line.strip().split(',')
                if len(values) >= 10:
                    ogrenci_no, ogrenci_ad, veli_ad, veli_tel, sinif, sinav1, sinav2, performans, proje, devamsizlik, ortalama = values[:11]
                    ogrenci = {
                        "Öğrenci No": ogrenci_no,
                        "Öğrenci Adı": ogrenci_ad,
                        "Veli Adı": veli_ad,
                        "Veli Telefon": veli_tel,
                        "Sınıf": sinif,
                        "1. Sınav": int(sinav1),
                        "2. Sınav": int(sinav2),
                        "Performans": int(performans),
                        "Proje": int(proje),
                        "Devamsızlık": int(devamsizlik),
                        "Ortalama": float(ortalama)
                    }
                    ogrenciler.append(ogrenci)
    except FileNotFoundError:
        open('ogrenciler.txt', 'w').close()

def ogrenci_ekle_gui():
    ogrenci_no = simpledialog.askstring("Öğrenci Ekle", "Öğrenci Numarası:", parent=root)
    position_dialog(root)
    ogrenci_ad = simpledialog.askstring("Öğrenci Ekle", "Öğrenci Adı:", parent=root)
    veli_ad = simpledialog.askstring("Öğrenci Ekle", "Veli Adı:", parent=root)
    veli_tel = simpledialog.askstring("Öğrenci Ekle", "Veli Telefon No:", parent=root)
    sinif = simpledialog.askstring("Öğrenci Ekle", "Sınıfı:", parent=root)
    sinav1 = simpledialog.askinteger("Öğrenci Ekle", "1. Sınav:", parent=root)
    sinav2 = simpledialog.askinteger("Öğrenci Ekle", "2. Sınav:", parent=root)
    performans = simpledialog.askinteger("Öğrenci Ekle", "Performans:", parent=root)
    proje = simpledialog.askinteger("Öğrenci Ekle", "Proje:", parent=root)
    devamsizlik = simpledialog.askinteger("Öğrenci Ekle", "Devamsızlık:", parent=root)

    ortalama = (sinav1 + sinav2 + performans + proje) / 4
    ogrenci = {
        "Öğrenci No": ogrenci_no,
        "Öğrenci Adı": ogrenci_ad,
        "Veli Adı": veli_ad,
        "Veli Telefon": veli_tel,
        "Sınıf": sinif,
        "1. Sınav": sinav1,
        "2. Sınav": sinav2,
        "Performans": performans,
        "Proje": proje,
        "Devamsızlık": devamsizlik,
        "Ortalama": ortalama
    }
    ogrenciler.append(ogrenci)
    with open('ogrenciler.txt', 'a') as f:
        f.write(f"{ogrenci_no},{ogrenci_ad},{veli_ad},{veli_tel},{sinif},{sinav1},{sinav2},{performans},{proje},{devamsizlik},{ortalama}\n")
    messagebox.showinfo("Başarılı", "Öğrenci başarıyla eklendi.")

def ogrenci_ara_gui():
    ogrenci_no = simpledialog.askstring("Öğrenci Ara", "Öğrenci Numarası:", parent=root)
    position_dialog(root)
    ogrenci_bulundu = ogrenci_ara(ogrenci_no, ogrenciler)
    if ogrenci_bulundu:
        result = (f"Öğrenci Bulundu:\n"
                  f"Numara: {ogrenci_bulundu['Öğrenci No']}\n"
                  f"Ad: {ogrenci_bulundu['Öğrenci Adı']}\n"
                  f"Veli Adı: {ogrenci_bulundu['Veli Adı']}\n"
                  f"Veli Telefon No: {ogrenci_bulundu['Veli Telefon']}\n"
                  f"Sınıf: {ogrenci_bulundu['Sınıf']}\n"
                  f"1. Sınav: {ogrenci_bulundu['1. Sınav']}\n"
                  f"2. Sınav: {ogrenci_bulundu['2. Sınav']}\n"
                  f"Performans: {ogrenci_bulundu['Performans']}\n"
                  f"Proje: {ogrenci_bulundu['Proje']}\n"
                  f"Ortalama: {ogrenci_bulundu.get('Ortalama', 'Hesaplanmadı')}\n"
                  f"Devamsızlık: {ogrenci_bulundu['Devamsızlık']}") 
        messagebox.showinfo("Arama Sonucu", result)
    else:
        messagebox.showerror("Hata", "Öğrenci bulunamadı.")

def ogrenci_guncelle_gui():
    ogrenci_no = simpledialog.askstring("Öğrenci Güncelle", "Güncellemek istediğiniz Öğrenci Numarası:", parent=root)
    position_dialog(root)
    ogrenci = ogrenci_ara(ogrenci_no, ogrenciler)

    if ogrenci:
        ogrenci_ad = simpledialog.askstring("Öğrenci Güncelle", "Öğrenci Adı:", initialvalue=ogrenci['Öğrenci Adı'], parent=root)
        veli_ad = simpledialog.askstring("Öğrenci Güncelle", "Veli Adı:", initialvalue=ogrenci['Veli Adı'], parent=root)
        veli_tel = simpledialog.askstring("Öğrenci Güncelle", "Veli Telefon No:", initialvalue=ogrenci['Veli Telefon'], parent=root)
        sinif = simpledialog.askstring("Öğrenci Güncelle", "Sınıfı:", initialvalue=ogrenci['Sınıf'], parent=root)
        sinav1 = simpledialog.askinteger("Öğrenci Güncelle", "1. Sınav:", initialvalue=ogrenci['1. Sınav'], parent=root)
        sinav2 = simpledialog.askinteger("Öğrenci Güncelle", "2. Sınav:", initialvalue=ogrenci['2. Sınav'], parent=root)
        performans = simpledialog.askinteger("Öğrenci Güncelle", "Performans:", initialvalue=ogrenci['Performans'], parent=root)
        proje = simpledialog.askinteger("Öğrenci Güncelle", "Proje:", initialvalue=ogrenci['Proje'], parent=root)
        devamsizlik = simpledialog.askinteger("Öğrenci Güncelle", "Devamsızlık:", initialvalue=ogrenci['Devamsızlık'], parent=root)

        ortalama = (sinav1 + sinav2 + performans + proje) / 4

        ogrenci.update({
            "Öğrenci Adı": ogrenci_ad,
            "Veli Adı": veli_ad,
            "Veli Telefon": veli_tel,
            "Sınıf": sinif,
            "1. Sınav": sinav1,
            "2. Sınav": sinav2,
            "Performans": performans,
            "Proje": proje,
            "Devamsızlık": devamsizlik,
            "Ortalama": ortalama
        })
        
        messagebox.showinfo("Başarılı", "Öğrenci başarıyla güncellendi.")
    else:
        messagebox.showerror("Hata", "Öğrenci bulunamadı.")

def ogrenci_sil_gui():
    ogrenci_no = simpledialog.askstring("Öğrenci Sil", "Silmek istediğiniz Öğrenci Numarası:", parent=root)
    position_dialog(root)
    ogrenci = ogrenci_ara(ogrenci_no, ogrenciler)

    if ogrenci:
        ogrenciler.remove(ogrenci)
        messagebox.showinfo("Başarılı", "Öğrenci başarıyla silindi.")
    else:
        messagebox.showerror("Hata", "Öğrenci bulunamadı.")

def veli_bilgilendir_gui():
    ogrenci_no = simpledialog.askstring("Veli Bilgilendir", "Bilgilendirmek istediğiniz Öğrenci Numarası:", parent=root)
    position_dialog(root)
    ogrenci = ogrenci_ara(ogrenci_no, ogrenciler)

    if ogrenci:
        veli_bilgilendir(ogrenci)
        messagebox.showinfo("Başarılı", "Veli başarıyla bilgilendirildi.")
    else:
        messagebox.showerror("Hata", "Öğrenci bulunamadı.")

def tum_velileri_bilgilendir_gui():
    tum_velileri_bilgilendir(ogrenciler)
    messagebox.showinfo("Başarılı", "Tüm veliler başarıyla bilgilendirildi.")

def rapor_olustur_gui():
    rapor_olustur(ogrenciler)
    messagebox.showinfo("Başarılı", "Rapor başarıyla oluşturuldu.")



style = ttk.Style()
# Buttonlar ekleme
# Buton stillerini belirleme
style.configure("TButton",
                font=("Helvetica", 12),
                padding=10,
                background="#4CAF50",
                foreground="black",
                focuscolor=style.configure(".")["background"])

# Butonları oluşturma ve yerleştirme
button_width = 20

button_ogrenci_ekle = ttk.Button(root, text="Öğrenci Ekle", command=ogrenci_ekle_gui, width=button_width, style="TButton")
button_ogrenci_ekle.pack(pady=5)

button_ogrenci_ara = ttk.Button(root, text="Öğrenci Ara", command=ogrenci_ara_gui, width=button_width, style="TButton")
button_ogrenci_ara.pack(pady=5)

button_ogrenci_guncelle = ttk.Button(root, text="Öğrenci Güncelle", command=ogrenci_guncelle_gui, width=button_width, style="TButton")
button_ogrenci_guncelle.pack(pady=5)

button_ogrenci_sil = ttk.Button(root, text="Öğrenci Sil", command=ogrenci_sil_gui, width=button_width, style="TButton")
button_ogrenci_sil.pack(pady=5)

button_veli_bilgilendir = ttk.Button(root, text="Veli Bilgilendir", command=veli_bilgilendir_gui, width=button_width, style="TButton")
button_veli_bilgilendir.pack(pady=5)

button_tum_velileri_bilgilendir = ttk.Button(root, text="Tüm Velileri Bilgilendir", command=tum_velileri_bilgilendir_gui, width=button_width, style="TButton")
button_tum_velileri_bilgilendir.pack(pady=5)

button_rapor_olustur = ttk.Button(root, text="Rapor Oluştur", command=rapor_olustur_gui, width=button_width, style="TButton")
button_rapor_olustur.pack(pady=5)

def cikis_yap():
    root.destroy()
    os.system("python login.py")

# ÇIKIŞ YAP butonunu ekleme
cikis_butonu = ttk.Button(root, text="ÇIKIŞ YAP", command=cikis_yap, style="TButton")
cikis_butonu.pack(side=tk.BOTTOM, pady=10)

# Öğrenci bilgilerini yükleme
load_students()

# Ana döngü
root.mainloop()
