import requests
from tqdm import tqdm

class YouTubeStreamDownloader:

    # Constant chunk size (4kb)
    CHUNK_SIZE = 4096

    @staticmethod
    def download_video(stream, output_path):
        # URL for the video stream
        stream_url = stream.url
        # Make a GET request for the stream
        response = requests.get(stream_url, stream=True)
        # Total video size
        total_size = int(response.headers.get('content-length', 0))
        # Initialize progress bar
        progress_bar = tqdm(total=total_size, unit="B", unit_scale=True, unit_divisor=1024, ncols=80)

        # Open output path in 'write binary' mode
        with open(output_path, 'wb') as f:
            # Iterate over response, writing chunk_size to file on each iteration
            for chunk in response.iter_content(chunk_size=YouTubeStreamDownloader.CHUNK_SIZE):
                f.write(chunk)
                progress_bar.update(len(chunk))
        progress_bar.close()
