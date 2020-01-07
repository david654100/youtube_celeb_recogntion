from pytube import YouTube
from pytube import Playlist
import os


def create_url(video_id: str) -> str:
    return "https://www.youtube.com/watch?v=" + video_id


def downloadYouTube(video_url:str, path:str):
    yt = YouTube(video_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

def downloadPlaylist(playlist_url:str,path:str):
    playlist = Playlist(playlist_url)
    if not os.path.exists(path):
        os.makedirs(path)
    playlist.download_all(path)

