import time
from music.radio import Radio
from music.youtube_handler import Youtube

def main():
    radio = Radio()

    video = Youtube.search("Tudo pura - la furia")

    radio.add_to_queue(video)

    radio.set_output_device_to_ab()

    radio.play()

    while (radio.is_playing()):
        time.sleep(1)

    radio.stop()


if __name__ == '__main__':
    main()