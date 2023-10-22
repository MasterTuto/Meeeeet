from typing import List
import vlc

from music.video import Video


class Radio:
    def __init__(self):
        self.queue : List[Video] = []

        self.vlc_instance = vlc.Instance()
        self.current_song : Video = None

        self.player = vlc.MediaPlayer(self.vlc_instance)

        self.will_play_first = True
    
    def add_to_queue(self, video : Video) -> None:
        self.queue.append(video)
    
    def play(self) -> None:
        if len(self.queue) == 0: return

        if self.will_play_first:
            video = self.queue.pop(0)
            self.current_song = video

            self.player.set_mrl(video.url)
        
        try:
            self.player.play()
            self.will_play_first = False
        except:
            if self.player.set_pause(False):
                self.will_play_first = False
    
    def stop(self) -> None:
        self.player.stop()
    
    def pause(self) -> None:
        self.player.set_pause(True)
    
    def set_output_device_to_ab(self) -> None:
        ab_device : bytes = None
        mods = self.player.audio_output_device_enum()

        if mods:
            mod = mods
            while mod:
                mod = mod.contents

                if mod.description == b'CABLE Input (VB-Audio Virtual Cable)':
                    ab_device = mod.device
                mod = mod.next

        vlc.libvlc_audio_output_device_list_release(mods)

        self.player.audio_output_device_set(None, ab_device)
    
    def play_next(self) -> None:
        self.current_song = self.queue.pop(0)
        if self.current_song:
            self.player.stop()
            self.player.set_mrl(self.current_song.url)
            self.player.play()
        else:
            self.player.stop()
            self.will_play_first = True
    
    def get_current(self) -> str:
        if self.current_song:
            return f"🎵 Tocando: {self.current_song.title}"
        else:
            return "Nenhuma musica esta tocando"
    
    def jump_to(self, index : int) -> None:
        # index starts from 0
        if index > len(self.queue) or index < 0: return

        self.player.stop()
        self.current_song = self.queue[index-1]

        self.player.set_mrl(self.current_song.url)
        self.queue = self.queue[index-1:]
        print(self.queue[0].title)
    
    def set_volume(self, volume : int) -> None:
        self.player.audio_set_volume(100)
        self.player.audio_set_volume(volume)

    def clear_queue(self) -> None:
        self.player.stop()
        self.queue = []
    
    def is_playing(self) -> bool:
        return self.player.is_playing()
