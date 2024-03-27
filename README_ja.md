# yt-pod

YouTube の動画をダウンロードして音声ファイルに変換し、Podcast 用のフィードファイルを作成することで、自分用のオリジナル Podcast を作成できます。

## 機能

- Youtube の動画をダウンロード
- 動画を音声データに変換
- Podcast 用のFeedファイルを作成

## 始め方

### 必要条件

以下の環境とモジュールを用意してください。

- Python 3
- ffmpeg
- yt_dlp

```bash
sudo apt -y install ffmpeg
pip install -U yt-dlp
```

### インストール方法

プロジェクトのセットアップ手順を記述します。

```bash
git clone https://github.com/togo13duke/yt-pod.git
cd yt-pod
pip install -r requirements.txt
```

## 使用方法

取得したいYoutubeチャンネルリストのファイルを作成します。

例）

```json
{
    "channels": [
        "https://www.youtube.com/@satomai811/videos",
        "https://www.youtube.com/@sonsera_ch/videos"
    ]
}
```

以下のように Python で main.py に引数を渡して実行します。

| Argument         | ‌‌Short | ‌‌‌Description                                              |
| ---------------- | ------ | --------------------------------------------------------- |
| \--directory     | \-d    | Directory to download audio files and store the RSS feed. |
| \--title         | \-t    | Title of the podcast.                                     |
| \--url           | \-u    | URL of the podcast host.                                  |
| \--channels-file | \-c    | Path to the JSON file containing channel URLs.            |

```bash
python main.py -d "/path/" -t "my youtube podcast" -u "https://podcast.com" -c "/path/channels.json"
```

## ライセンス

このプロジェクトは [MIT ライセン](https://opensource.org/license/mit) のもとで公開されています。
