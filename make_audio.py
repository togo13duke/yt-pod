import yt_dlp
import os
from datetime import datetime, timedelta
import json  # Import the json module

def clean_file_names(directory):
    """Rename files to replace problematic characters."""
    for filename in os.listdir(directory):
        new_name = filename.replace('&', '_').replace('#', '_').replace('%', '_')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

def delete_old_files(directory, days=30):
    """Delete files older than a specified number of days, excluding .jpg files."""
    cutoff_date = datetime.now() - timedelta(days=days)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.jpg'):
            continue
        if datetime.fromtimestamp(os.path.getmtime(file_path)) < cutoff_date:
            os.remove(file_path)

def download_audio_from_channels(channels, directory, archive='archive'):
    """Download audio files from a list of YouTube channels."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
        'match_filter': yt_dlp.utils.match_filter_func("!is_live"),
        'download_archive': archive,
        'outtmpl': os.path.join(directory, '%(channel)s_%(title).50B.%(ext)s'),
        #'cookiesfile': 'youtube.cookies.txt',
        'playlistend': 3,
        'min_filesize': 5*1024*1024,  # 5 MB
        'max_filesize': 60*1024*1024,  # 60 MB
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for channel in channels:
            ydl.download([channel])

def main(channels_file_path, directory):

    # Read channels from a JSON file
    with open(channels_file_path, 'r') as file:
        channels_data = json.load(file)
    channels = channels_data['channels']

    download_audio_from_channels(channels, directory)
    clean_file_names(directory)
    delete_old_files(directory)

if __name__ == '__main__':
    # Assume the channels JSON file path is passed as a command-line argument or hardcode the path
    channels_file_path = 'channels.json'  # Adjust this path as necessary
    main(channels_file_path)