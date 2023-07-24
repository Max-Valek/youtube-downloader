from youtube_downloader import YouTubeDownloaderApp

# example url: https://www.youtube.com/watch?v=4v8ek9TEeOU

if __name__ == "__main__":
    
    youtube_downloader = YouTubeDownloaderApp()
    video_url = input("Enter video URL: ")
    youtube_downloader.download(video_url)

    # If you want to save the video to a specific location.
    
    # output_path = input("Enter the path to save the video: ")
    # youtube_downloader.download(video_url, output_path)
