import os, time
import tkinter as tk
from tkinter import ttk

class video_player:
    def __init__ (self, parent, vlc, row, col):
        self.parent = parent
        self.debug = "[" + str(row) + "," + str(col) + "]"

        # Create a vlc instance; 
        # https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.MediaPlayer-class.html
        self.vlc_instance = vlc
        self.vlc_media_player_instance = self.vlc_instance.media_player_new()

        self.player = tk.Canvas(self.parent, background='black')
        self.player.pack(fill=tk.BOTH, expand=1)

        print(self.debug, "init")
        self.parent.grid(column=col, row=row)
        self.parent.update()

    def play(self):
        print(self.debug,"play")
        """Play a file."""
        if not self.vlc_media_player_instance.get_media():
            self.open()
        else:
            if self.vlc_media_player_instance.play() == -1:
                pass
    
    def playMedia(self, file):
        print(self.debug, "new file ::", file)
        """Invokes the `play` method on the vlc instance for the current file."""
        directory_name = os.path.dirname(file)
        file_name = os.path.basename(file)
        self.Media = self.vlc_instance.media_new(
            str(os.path.join(directory_name, file_name))
        )
        #self.Media.get_meta()
        self.vlc_media_player_instance.set_media(self.Media)
        self.vlc_media_player_instance.set_hwnd(self.player.winfo_id())
        self.play()

    def isDone(self) -> bool:
        wontPlay = not self.vlc_media_player_instance.will_play()
        finished = not self.vlc_media_player_instance.is_playing()

        if wontPlay :
            print(self.debug, "file error", self.Media)

        return wontPlay or finished
