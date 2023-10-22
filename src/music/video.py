import pafy
from youtube import Video as YoutubeVideo

class Video(object):
    def __init__(self, video : YoutubeVideo) -> None:
        pafy_video = pafy.new( video.video_watch_url )

        self.video_id : str = video.video_id
        self.video_watch_url : str = video.video_watch_url
        self.title : str = video.title

        self.url : str = pafy_video.getbestaudio().url
