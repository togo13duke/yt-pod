# yt-pod

[日本語](README_ja.md)

You can create your own original Podcast by downloading videos from YouTube, converting them into audio files, and creating a feed file for Podcasts.

## Features

- Download videos from YouTube
- Convert videos to audio data
- Create a feed file for Podcasts

## Getting Started

### Prerequisites

Prepare the following environment and modules.

- Python 3
- ffmpeg
- yt_dlp

```bash
sudo apt -y install ffmpeg
pip install -U yt-dlp
```

## Installation

Describe the setup steps for the project.

```
git clone https://github.com/togo13duke/yt-pod.git
cd yt-pod
pip install -r requirements.txt
```

## Usage
Create a file with the list of YouTube channels you want to obtain.

Example:

```json
{
    "channels": [
        "https://www.youtube.com/@satomai811/videos",
        "https://www.youtube.com/@sonsera_ch/videos"
    ]
}
```

Execute main.py with arguments in Python as follows:

| Argument         | ‌‌Short | ‌‌‌Description                                              |
| ---------------- | ------ | --------------------------------------------------------- |
| \--directory     | \-d    | Directory to download audio files and store the RSS feed. |
| \--title         | \-t    | Title of the podcast.                                     |
| \--url           | \-u    | URL of the podcast host.                                  |
| \--channels-file | \-c    | Path to the JSON file containing channel URLs.            |

```bash
python main.py -d "/path/" -t "my youtube podcast" -u "https://podcast.com" -c "/path/channels.json"
```

## License

This project is released under the MIT License.
