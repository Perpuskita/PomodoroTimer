import tkinter as tk
import customtkinter as ctk
from datetime import datetime, timedelta

# Ukuran panel berdasarkan pixel
size = "500x400"

# Waktu dan kata2 penyemangat Pomodoro (menit)
pomodoro = [25, 5, 25, 5, 25, 5, 25, 30]
sesion_name = ["belajar dengan semangat", "istirahat kecil", 
               "belajar giat mencapai cita", "istirahat kecil", 
               "belajar adalah investasi", "istirahat kecil",
               "belajar untuk masa depan", "istirahat besar"]

# Kelas yang menampung panel utama aplikasi
class App(ctk.CTk):
    def __init__(self, pomodoro_time, fg_color=None, **kwargs):
        super().__init__(fg_color=fg_color, **kwargs)

        self.geometry(size)
        self.title("Pomodoro App")

        # Simpan konfigurasi waktu
        self.pomodoro = pomodoro_time
        self.counter = 0

        # Label tampilan sesi
        self.session = ctk.CTkLabel(self, text="Klik tombol mulai untuk menjalankan aplikasi", text_color="white", font=("Consolas", 14))
        self.session.pack(pady=20, padx=20, fill="x")

        # Label tampilan waktu
        self.clock_now = ctk.CTkLabel(self, text="Pomodoro Time", text_color="white", font=("Consolas", 28))
        self.clock_now.pack(pady=20, padx=20, fill="x")

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self, orientation="horizontal")
        self.progress_bar.pack(pady=20, padx=20, fill="x")
        self.progress_bar.set(0)

        # Tombol Mulai
        self.start_button = ctk.CTkButton(self, text="Mulai", command=self.start_pomodoro)
        self.start_button.pack(pady=20, padx=20, fill="x")

    def start_pomodoro(self):
        # Cek kondisi counter jika lebih dari panjang array pomodoro maka hentikan countdown
        if self.counter >= len(self.pomodoro):
            self.clock_now.configure(text="Pomodoro Time!")
            self.start_button.configure(state="normal", text="Mulai Lagi", command=self.start_pomodoro)
            self.session.configure(text="Klik tombol mulai untuk menjalankan aplikasi")
            self.counter = 0
            self.progress_bar.set(0)
            return
        
        # Kondisi ketika counter kurang dari panjang array pomodoro
        # Lanjutkan untuk update clock
        session_text = f"{self.counter+1} : {sesion_name[self.counter]}"
        self.session.configure(text=f"Sesi {session_text}")
        self.start_button.configure(state="disabled", text = "...")
        self.countdown = self.pomodoro[self.counter] * 60
        self.progress_time = self.countdown
        self.update_clock()

    def update_clock(self):
        # Update tampilan clock selama sekian menit
        minutes, seconds = divmod(self.countdown, 60)
        self.clock_now.configure(text=f"{minutes:02d}:{seconds:02d}")

        # Update progress bar
        progress = 1 - (self.countdown / self.progress_time)
        self.progress_bar.set(progress)

        # Kondisi pengecekan countdown
        # Lanjutkan countdown jika detik belum 0
        if self.countdown < 0:
            self.counter += 1
            self.start_pomodoro()
        else:
            self.countdown -= 1
            self.after(1000, self.update_clock)

# Entry Point Program
if __name__ == "__main__":
    app = App(pomodoro_time=pomodoro)
    app.mainloop()
