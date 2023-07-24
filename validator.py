import re

class YouTubeValidator:

    @staticmethod
    def validate_video_url(video_url):
        # Validate YouTube video url format.
        return re.match(r'^https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+', video_url)
