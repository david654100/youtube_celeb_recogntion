import pytube


def create_url(videoId: str) -> str:
    return "https://www.youtube.com/watch?v=" + videoId

def youtube_download(path:str,url:str):
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download(path)