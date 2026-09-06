import tkinter
from tkinter import messagebox

# 1. ANA PENCERE OLUŞTURMA
pencere = tkinter.Tk()
pencere.title("Not Hesaplama")
pencere.geometry("250x220")
pencere.resizable(False, False)

# 2. ARAYÜZ ELEMANLARI
tkinter.Label(
    pencere, text="Puanınızı giriniz:", font=("Arial", 10, "bold")
).place(x=15, y=25)

puan_entry = tkinter.Entry(pencere)
puan_entry.place(x=40, y=55, width=170)

yazi_label = tkinter.Label(pencere, font=("Arial", 11, "bold"))
yazi_label.place(x=40, y=140, width=170)


# 3. HESAPLAMA FONKSİYONU
def hesaplama():
    try:
        puanim = int(puan_entry.get())

        if puanim < 0 or puanim > 100:
            yazi_label.configure(
                text="0-100 arası giriniz!", fg="orange"
            )
        elif puanim < 50:
            yazi_label.configure(text="Kaldı", fg="red")
        elif 50 <= puanim <= 69:
            yazi_label.configure(text="Geçti", fg="blue")
        else:  # 70 ve üzeri
            yazi_label.configure(text="Başarılı", fg="green")

        puan_entry.delete(0, tkinter.END)

    except ValueError:
        messagebox.showwarning(
            "Hatalı Giriş", "Lütfen sadece sayısal bir değer giriniz!"
        )
        puan_entry.delete(0, tkinter.END)


# 4. BUTON (Fonksiyon tanımlandıktan sonra command ile bağlandı)
hesapla_butonu = tkinter.Button(
    pencere, text="Hesapla", font=("Arial", 10, "bold"), command=hesaplama
)
hesapla_butonu.place(x=85, y=90, width=80)

# 5. DÖNGÜYÜ BAŞLATMA / Ekrana Getirme 
pencere.mainloop()
