import argparse
from make_audio import main as download_and_clean_audio
from generate_rss import generate_rss

def parse_arguments():
    parser = argparse.ArgumentParser(description='Download YouTube videos as audio and generate an RSS feed.')
    parser.add_argument('--directory', '-d', type=str, required=True, help='Directory to download audio files and store the RSS feed.')
    parser.add_argument('--title', '-t', type=str, required=True, help='Title of the podcast.')
    parser.add_argument('--url', '-u', type=str, required=True, help='URL of the podcast host.')
    parser.add_argument('--channels-file', '-c', type=str, required=True, help='Path to the JSON file containing channel URLs.')
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Download audio from YouTube channels and clean file names
    # Now passing the channels JSON file path as an argument
    download_and_clean_audio(args.channels_file, args.directory)

    # Generate RSS feed from the downloaded audio files
    generate_rss(args.title, args.url, args.directory,args.url+"/index.jpg")

    print(f'Process completed. The RSS feed is available in {args.directory}')

if __name__ == '__main__':
    main()