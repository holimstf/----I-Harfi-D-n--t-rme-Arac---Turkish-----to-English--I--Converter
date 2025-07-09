import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("dark")  # "dark", "light" veya "system"
ctk.set_default_color_theme("blue")  # "blue", "dark-blue", "green"

class ConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("İ → I Harfi Dönüştürücü")
        self.geometry("650x600")
        self.resizable(False, False)

        self.file_path = None
        self.original_content = ""

        # Başlık
        self.label_title = ctk.CTkLabel(self, text="İ → I Harfi Dönüştürme Aracı", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=(20, 10))

        # Açıklama
        self.label_desc = ctk.CTkLabel(self, 
            text="Bir metin dosyası seçip içindeki Türkçe 'İ' harflerini\nİngilizce 'I' ile değiştir ve kaydet.", 
            font=ctk.CTkFont(size=14), justify="center")
        self.label_desc.pack(pady=(0, 20))

        # Dosya seçme butonu
        self.btn_select = ctk.CTkButton(self, text="Dosya Seç", command=self.select_file, width=150)
        self.btn_select.pack(pady=5)

        # Önizleme alanı (metin kutusu)
        self.text_preview = ctk.CTkTextbox(self, width=600, height=250, font=("Courier New", 12))
        self.text_preview.pack(pady=15)
        self.text_preview.configure(state="disabled")

        # Dönüştür ve Kaydet butonu (pasif)
        self.btn_convert = ctk.CTkButton(self, text="Dönüştür ve Kaydet", command=self.convert_and_save, width=180, state="disabled")
        self.btn_convert.pack(pady=10)

        # Durum etiketi
        self.label_status = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=12))
        self.label_status.pack(pady=5)

    def select_file(self):
        filetypes = [("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")]
        path = filedialog.askopenfilename(title="Dosya Seç", filetypes=filetypes)
        if path:
            self.file_path = path
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    self.original_content = f.read()
                self.text_preview.configure(state="normal")
                self.text_preview.delete("0.0", "end")
                self.text_preview.insert("0.0", self.original_content)
                self.text_preview.configure(state="disabled")
                self.label_status.configure(text=f"Seçilen dosya yüklendi:\n{self.file_path}")
                self.btn_convert.configure(state="normal")
            except Exception as e:
                messagebox.showerror("Hata", f"Dosya okunamadı:\n{e}")
                self.label_status.configure(text="Dosya okunamadı.")
                self.btn_convert.configure(state="disabled")
        else:
            self.label_status.configure(text="Dosya seçilmedi.")
            self.btn_convert.configure(state="disabled")
            self.text_preview.configure(state="normal")
            self.text_preview.delete("0.0", "end")
            self.text_preview.configure(state="disabled")

    def convert_and_save(self):
        if not self.original_content:
            messagebox.showwarning("Uyarı", "Lütfen önce bir dosya seçin.")
            return
        try:
            converted = self.original_content.replace("İ", "I")
            save_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Metin Dosyaları", "*.txt")],
                                                     title="Dönüştürülmüş dosyayı kaydet")
            if save_path:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(converted)
                messagebox.showinfo("Başarılı", f"Dosya başarıyla kaydedildi:\n{save_path}")
                self.label_status.configure(text=f"Dosya başarıyla kaydedildi:\n{save_path}")
            else:
                self.label_status.configure(text="Kaydetme işlemi iptal edildi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu:\n{e}")

if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()

