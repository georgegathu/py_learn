import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yt_dlp
from threading import Thread

class MediaDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Downloader")
        self.root.geometry("600x400")
        self.setup_ui()
        
    def setup_ui(self):
        # URL Input
        url_frame = ttk.LabelFrame(self.root, text="URL", padding="10")
        url_frame.pack(fill="x", padx=10, pady=5)
        
        self.url_entry = ttk.Entry(url_frame)
        self.url_entry.pack(fill="x", expand=True)
        
        # Download Options
        options_frame = ttk.LabelFrame(self.root, text="Download Options", padding="10")
        options_frame.pack(fill="x", padx=10, pady=5)
        
        self.download_type = tk.StringVar(value="video")
        ttk.Radiobutton(options_frame, text="Video", value="video", 
                       variable=self.download_type).pack(side="left", padx=5)
        ttk.Radiobutton(options_frame, text="Audio Only", value="audio", 
                       variable=self.download_type).pack(side="left", padx=5)
        
        # Quality Selection
        quality_frame = ttk.LabelFrame(self.root, text="Quality", padding="10")
        quality_frame.pack(fill="x", padx=10, pady=5)
        
        self.quality_var = tk.StringVar(value="highest")
        ttk.Radiobutton(quality_frame, text="Highest", value="highest", 
                       variable=self.quality_var).pack(side="left", padx=5)
        ttk.Radiobutton(quality_frame, text="Lowest", value="lowest", 
                       variable=self.quality_var).pack(side="left", padx=5)
        
        # Progress Frame
        progress_frame = ttk.LabelFrame(self.root, text="Download Progress", padding="10")
        progress_frame.pack(fill="x", padx=10, pady=5)
        
        self.progress_bar = ttk.Progressbar(progress_frame, length=400, mode='determinate')
        self.progress_bar.pack(fill="x", pady=5)
        
        self.status_label = ttk.Label(progress_frame, text="Ready")
        self.status_label.pack()
        
        # Download Button
        self.download_button = ttk.Button(self.root, text="Download", command=self.start_download)
        self.download_button.pack(pady=10)

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            if 'total_bytes' in d:
                percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
                self.progress_bar["value"] = percent
                self.status_label["text"] = f"Downloading... {percent:.1f}%"
            else:
                self.status_label["text"] = "Downloading... (Size unknown)"
        elif d['status'] == 'finished':
            self.status_label["text"] = "Download Complete!"
            self.download_button["state"] = "normal"
            messagebox.showinfo("Success", "Download completed successfully!")
            
    def start_download(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            return
            
        self.download_button["state"] = "disabled"
        self.status_label["text"] = "Starting download..."
        Thread(target=self.download_media, args=(url,)).start()
        
    def download_media(self, url):
        try:
            # Get download path from user
            download_path = filedialog.askdirectory()
            if not download_path:
                self.download_button["state"] = "normal"
                self.status_label["text"] = "Download cancelled"
                return

            ydl_opts = {
                'format': 'best' if self.download_type.get() == 'video' else 'bestaudio/best',
                'progress_hooks': [self.progress_hook],
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            }

            if self.download_type.get() == 'audio':
                ydl_opts.update({
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                })

            if self.quality_var.get() == 'lowest':
                ydl_opts['format'] = 'worst' if self.download_type.get() == 'video' else 'worstaudio/worst'

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
        except Exception as e:
            self.status_label["text"] = "Error occurred"
            self.download_button["state"] = "normal"
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MediaDownloader(root)
    root.mainloop()