import time

from music.youtube_handler import Youtube
from music.radio import Radio

from tests.logger import Logger

def test_search_video():
    video = Youtube.search("psy gangnam style")
    
    assert video.video_watch_url == "https://www.youtube.com/watch?v=9bZkp7q19f0", Logger.err("Erro - Teste de pesquisa")

    Logger.success("Sucesso - Pesquisa no Youtube")

def test_play_song():
    radio = Radio()

    video1 = Youtube.search("psy gangnam style")

    radio.add_to_queue(video1)

    radio.play()

    time.sleep(30)

    radio.stop()

def test_queue():
    radio = Radio()

    video1 = Youtube.search("psy gangnam style")
    video2 = Youtube.search("alan walker faded")

    radio.add_to_queue(video1)
    radio.add_to_queue(video2)

    radio.play()

    time.sleep(30)

    radio.play_next()

    time.sleep(30)

    radio.stop()

def begin():
    pass