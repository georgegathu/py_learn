from pytube import YouTube
import youtube_dl

def download_video(url, output_path):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    print(f"Downloading video: {yt.title}")
    ys.download(output_path)
    print("Video downloaded successfully!")

def download_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Audio downloaded successfully!")

if __name__ == "__main__":
    url = input("Enter the URL of the video: ")
    output_path = input("Enter the output path (directory) for the downloads: ")
    
    download_choice = input("Download (v)ideo or (a)udio? ").lower()
    if download_choice == 'v':
        download_video(url, output_path)
    elif download_choice == 'a':
        download_audio(url, output_path)
    else:
        print("Invalid choice! Please enter 'v' for video or 'a' for audio.")
