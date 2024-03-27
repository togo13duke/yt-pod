import xml.etree.ElementTree as ET
from datetime import datetime
import os
import time  # Import the time module for accessing file modification times

def format_datetime(timestamp):
    """Format a timestamp to RFC 822 format."""
    return datetime.fromtimestamp(timestamp).strftime('%a, %d %b %Y %H:%M:%S +0000')

def generate_rss(title, url, directory, image_url):
    """Generate an RSS feed for a podcast with iTunes-specific tags."""
    # Define namespaces for iTunes
    ET.register_namespace('itunes', "http://www.itunes.com/dtds/podcast-1.0.dtd")

    # Create the root element with namespaces
    rss = ET.Element('rss', attrib={'version': '2.0', 'xmlns:itunes': "http://www.itunes.com/dtds/podcast-1.0.dtd"})
    channel = ET.SubElement(rss, 'channel')

    # Basic podcast information
    ET.SubElement(channel, 'title').text = title
    #ET.SubElement(channel, 'link').text = url
    ET.SubElement(channel, 'itunes:image', href=image_url)

    # Iterate over audio files in the directory to add each as an item in the feed
    for audio_file in os.listdir(directory):
        if audio_file.endswith('.mp3'):
            item = ET.SubElement(channel, 'item')
            audio_file_path = os.path.join(directory, audio_file)
            audio_file_url = os.path.join(url, audio_file)

            # Use file's modification time as publication date
            mtime = os.path.getmtime(audio_file_path)
            pub_date = format_datetime(mtime)

            ET.SubElement(item, 'title').text = os.path.splitext(audio_file)[0]
            ET.SubElement(item, 'enclosure', url=audio_file_url, length=str(os.path.getsize(audio_file_path)), type="audio/mp3")
            ET.SubElement(item, 'guid', isPermaLink="true").text = audio_file_url
            ET.SubElement(item, 'pubDate').text = pub_date

    # Generate the tree and write the RSS XML to a file
    tree = ET.ElementTree(rss)
    with open(os.path.join(directory, 'podcast_rss.xml'), 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)

    print(f'RSS Feed generated successfully at {os.path.join(directory, "podcast_rss.xml")}')


