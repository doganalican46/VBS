import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

# Ana uygulama penceresini oluştur
root = tk.Tk()
root.title("AHMET DOYMUŞ - Veli Bilgilendirme Sistemi")
root.geometry("800x400")
root.configure(bg='#000000')

# Pencereyi ekranın ortasına yerleştirme
def center_window(root, width=800, height=400):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

center_window(root)

# Renkler ve stiller
bg_color = "#000000"
fg_color = "#ffffff"
entry_bg = "#ffffff"
entry_fg = "#000000"  # Entry widget'ları için yazı rengi
button_bg = "#4CAF50"
button_fg = "#ffffff"
font_style = ("Helvetica", 12)

def login():
    username = username_entry.get()
    password = password_entry.get()
    # Demonstrasyon için, kullanıcı adı ve şifre bu değerlere eşitse giriş başarılı sayılır
    if username == "admin" and password == "password":
        messagebox.showinfo("Giriş Başarılı", "Yav ben ne bilim!")
        root.destroy()  # Giriş penceresini kapat
        subprocess.Popen(['python', 'index.py'])  # index.py dosyasını çalıştır
    else:
        messagebox.showerror("Giriş Başarısız", "Şifrenizi mi unuttunuz? Bi dal b12 iyi gelebilir.")

# Resmi yükle ve yerleştir
image_path = "C:/Users/dogan/OneDrive/Masaüstü/VBS/images/vector.png"
img = Image.open(image_path)
img = img.resize((400, 400), Image.LANCZOS)  # Resmi pencereye sığacak şekilde yeniden boyutlandır
photo = ImageTk.PhotoImage(img)
img_label = tk.Label(root, image=photo, bg=bg_color)
img_label.pack(side="left")

# Giriş formu için bir çerçeve oluştur
form_frame = tk.Frame(root, bg=bg_color)
form_frame.pack(side="right", padx=50, pady=50)

# Başlık etiketini oluştur ve yerleştir
title_label = tk.Label(form_frame, text="GİRİŞ EKRANI", font=("Helvetica", 18), bg=bg_color, fg=fg_color)
title_label.pack(pady=20)

# Kullanıcı adı etiketi ve giriş kutusunu oluştur ve yerleştir
username_label = tk.Label(form_frame, text="Kullanıcı Adı", font=font_style, bg=bg_color, fg=fg_color)
username_label.pack(pady=5)
username_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg, fg=entry_fg, width=30)
username_entry.pack(pady=5)

# Şifre etiketi ve giriş kutusunu oluştur ve yerleştir
password_label = tk.Label(form_frame, text="Şifre", font=font_style, bg=bg_color, fg=fg_color)
password_label.pack(pady=5)
password_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg, fg=entry_fg, width=30, show="*")
password_entry.pack(pady=5)

# Giriş butonunu oluştur ve yerleştir
login_button = tk.Button(form_frame, text="GİRİŞ YAP", font=font_style, bg=button_bg, fg=button_fg, command=login)
login_button.pack(pady=20)

# Tkinter etkinlik döngüsünü çalıştır
root.mainloop()
