import pygame
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

pygame.mixer.init()

class MusicPlayer(tk.Tk):    
    def __init__(self):
        super().__init__()

        self.title("Music Player")
        self.geometry("800x600")  
        self.config(bg="#1e1e1e")
        
        self.current_song = None

        self.song_label = tk.Label(self, text="No song playing", bg="#1e1e1e", fg="white", font=("Arial", 14))
        self.song_label.pack(pady=10)

        self.image_label = tk.Label(self, bg="#1e1e1e")
        self.image_label.pack(pady=10)

        button_frame = tk.Frame(self, bg="#1e1e1e")
        button_frame.pack(pady=10)

        button_style = {"width": 12, "bg": "#333", "fg": "white", "font": ("Arial", 10)}

        self.play_button = tk.Button(button_frame, text="Play", command=self.play_music, **button_style)
        self.play_button.grid(row=0, column=0, padx=5, pady=5)

        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_music, **button_style)
        self.pause_button.grid(row=0, column=1, padx=5, pady=5)

        self.resume_button = tk.Button(button_frame, text="Resume", command=self.resume_music, **button_style)
        self.resume_button.grid(row=0, column=2, padx=5, pady=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_music, **button_style)
        self.stop_button.grid(row=1, column=0, padx=5, pady=5)

        self.load_button = tk.Button(button_frame, text="Load Music", command=self.load_music, **button_style)
        self.load_button.grid(row=1, column=1, padx=5, pady=5)

        self.quit_button = tk.Button(button_frame, text="Quit", command=self.quit, **button_style)
        self.quit_button.grid(row=1, column=2, padx=5, pady=5)

        self.prev_button = tk.Button(button_frame, text="Previous", command=self.previous_song, **button_style)
        self.prev_button.grid(row=2, column=0, padx=5, pady=5)

        self.next_button = tk.Button(button_frame, text="Next", command=self.next_song, **button_style)
        self.next_button.grid(row=2, column=2, padx=5, pady=5)

        self.song_list = []  
        self.current_song_index = -1
        
      # Playlist
        self.song_list = ["Happy Na Birthday Mo Pa.mp3", "Cry.mp3"]
        self.current_song_index = 0

    def play_music(self):
        if self.current_song:
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            self.song_label.config(text=f"Playing: {os.path.basename(self.current_song)}")
            self.display_image()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.song_label.config(text="No song playing")
        self.image_label.config(image="")

    def load_music(self):
        file_path = filedialog.askopenfilename(title="Select Music File", filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")])
        if file_path:
            self.current_song = file_path
            self.song_label.config(text=f"Loaded: {os.path.basename(file_path)}")
            self.play_music()

    def display_image(self):
        image_path = os.path.splitext(self.current_song)[0] + ".jpg"
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((450, 350), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img

    def next_song(self):
        if self.song_list:
            self.current_song_index = (self.current_song_index + 1) % len(self.song_list)
            self.current_song = self.song_list[self.current_song_index]
            self.song_label.config(text=f"Loaded: {os.path.basename(self.current_song)}")
            self.play_music()

    def previous_song(self):
        if self.song_list:
            self.current_song_index = (self.current_song_index - 1) % len(self.song_list)
            self.current_song = self.song_list[self.current_song_index]
            self.song_label.config(text=f"Loaded: {os.path.basename(self.current_song)}")
            self.play_music()

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()

