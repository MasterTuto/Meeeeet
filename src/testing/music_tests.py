import time

from music.youtube_handler import Youtube
from music.radio import Radio

from .logger import Logger

def test_search_video():
    Logger.annotation("Iniciando teste de pesquisa...")
    
    video = Youtube.search("psy gangnam style")
    
    assert video.video_watch_url == "https://www.youtube.com/watch?v=9bZkp7q19f0", Logger.get_err("Teste de pesquisa")

    Logger.success("Pesquisa no Youtube")


def test_change_output_device():
    Logger.annotation("Iniciando teste de troca dispositivo de entrada..")

    radio = Radio()
    radio.set_output_device_to_ab()

    video1 = Youtube.search("psy gangnam style")
    
    radio.add_to_queue(video1)

    radio.play()

    time.sleep(20)

    radio.stop()

    Logger.success("Ao mudar dispositivo de saida")

def test_play_song():
    radio = Radio()

    video1 = Youtube.search("psy gangnam style")

    radio.add_to_queue(video1)

    radio.play()

    time.sleep(20)

    radio.stop()

    Logger.success("Ao tocar musica")

def test_queue():
    radio = Radio()

    video1 = Youtube.search("psy gangnam style")
    video2 = Youtube.search("alan walker faded")

    radio.add_to_queue(video1)
    radio.add_to_queue(video2)

    radio.play()

    time.sleep(20)

    radio.play_next()

    time.sleep(20)

    radio.stop()

    Logger.success("Teste de fila")

def test_change_volume():
    radio = Radio()

    video = Youtube.search("psy gangnam style")

    radio.add_to_queue(video)

    radio.play()

    radio.set_volume(30)

    time.sleep(20)

    radio.stop()
    
    Logger.success("Volume alterado com sucesso!")

def test_get_current():
    radio = Radio()

    video = Youtube.search("psy gangnam style")

    radio.add_to_queue(video)

    radio.play()

    assert video.title in radio.get_current(), Logger.get_err("Nao foi possivel obter o atual")

    Logger.success("Foi possivel obter o atual")

def test_jump_to():

    searchs = [
        'psy gangnam style',
        'alan walker fade',
        'rammstein deutschland',
        'jupiter maça um lugar do caralho'
    ]

    radio = Radio()

    for search in searchs:
        video = Youtube.search(search)

        radio.add_to_queue(video)

    radio.jump_to(3)

    radio.play()

    t = Youtube.search(searchs[2]).title
    rc = radio.get_current()

    print(t, rc)

    assert t in rc, Logger.get_err("Nao foi possivel pular para video")

    Logger.success("Pular para musica")

def test_clear_queue():    
    searchs = [
        'psy gangnam style',
        'alan walker fade',
        'rammstein deutschland',
        'jupiter maça um lugar do caralho'
    ]

    radio = Radio()

    for search in searchs:
        video = Youtube.search(search)

        radio.add_to_queue(video)
    
    radio.clear_queue()

    assert len(radio.queue) == 0, Logger.get_err("Ao limpar musica")

    Logger.success("Ao limpar musica")
    

def begin():
    test_search_video()
    test_play_song()
    test_change_output_device()
    test_queue()
    test_change_volume()
    test_get_current()
    test_jump_to()
    test_clear_queue()