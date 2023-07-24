import os
from pytube import YouTube
from validator import YouTubeValidator
from stream_downloader import YouTubeStreamDownloader
import requests

class YouTubeDownloaderApp:

    # No output path by default
    def __init__(self):
        self.output_path = None

    def download(self, video_url, output_path=None):
        print("Fetching...")
        try:
            # Ensure the URL is the correct format.
            if not YouTubeValidator.validate_video_url(video_url):
                print("Invalid YouTube video URL. Please try again.")
                return

            # Create pytube Youtube object.
            yt = YouTube(video_url)
            
            # Get the highest reolution stream.
            video_stream = yt.streams.get_highest_resolution()

            print(f"Downloading {yt.title} by {yt.author} in {video_stream.resolution}...\n")

            # Set file name as the video title.
            output_filename = f"{yt.title}.mp4"

            # Save the video to downloads by default.
            output_path = output_path or os.path.join(os.path.expanduser('~'), 'Downloads', output_filename)

            # Make sure output path is valid.
            if not os.path.isdir(os.path.dirname(output_path)):
                raise ValueError("Invalid output path. The directory does not exist.")

            # Download the video stream.
            YouTubeStreamDownloader.download_video(video_stream, output_path)

            print("Video downloaded successfully!")
        
        # Catch request errors.
        except requests.exceptions.RequestException as e:
            print("Error: Failed to establish a connection.")
        # Catch value and OS errors.
        except (ValueError, OSError) as e:
            print("Error:", str(e))
        # Catch any other errors.
        except Exception as e:
            print("Error: An unexpected error occurred.")