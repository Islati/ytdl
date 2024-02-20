import sys
import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video_file = video.download()
        return video_file
    except Exception as e:
        print("Error:", e)
        return None

def convert_to_mp3(video_file):
    try:
        video = VideoFileClip(video_file)
        audio_file = os.path.splitext(video_file)[0] + ".mp3"
        video.audio.write_audiofile(audio_file)
        video.close()  # Close the video file
        return audio_file
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dl.py [url]")
        sys.exit(1)

    url = sys.argv[1]

    print("Downloading video...")
    video_file = download_video(url)
    if video_file:
        print("Converting to MP3...")
        audio_file = convert_to_mp3(video_file)
        if audio_file:
            print("MP3 file saved as:", audio_file)