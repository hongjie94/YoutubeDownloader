import yt_dlp

URLS = [input("Enter Youtube Link: ")]
while URLS != 'exit':
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)
    URLS = [input("Enter Youtube Link: ")]    
