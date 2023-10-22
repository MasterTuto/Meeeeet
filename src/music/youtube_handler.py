from youtube import Search

from .video import Video

class Youtube:
    def search(query : str) -> Video:
        search_result = Search(query)
        
        return Video(search_result.first)
