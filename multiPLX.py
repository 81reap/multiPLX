import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

import vlc, queue
import tkinter as tk
from tkinter import ttk
from video_player import video_player as vp

files = queue.queue()

class BaseTkContainer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("lqud")
        self.root.protocol("WM_DELETE_WINDOW", self.delete_window)
        self.root.geometry("1920x1080") # default to 1080p
        self.root.configure(background='black')
        self.root.resizable(0, 0)
        
        self.theme = ttk.Style()
        self.theme.theme_use("alt")
        
        self.frame = ttk.Frame(self.root)
        self.vlc = vlc.Instance()
        self.players = []

    def delete_window(self):
        tk_instance = self.root
        tk_instance.quit()
        tk_instance.destroy()
        os._exit(1)

    def update_window(self):
        for player in self.players:
            if player.isDone() :
                print("update :: new media")
                player.playMedia(files.dequeue())
        self.root.after(1000, self.update_window)

    def add_player(self, row, col, file):
        player = vp(self.frame, self.vlc, row, col)
        player.playMedia(file)
        self.players.append(player)
    
    def __repr__(self):
        return "Base tk Container"

if __name__ == "__main__":
    N = 2

    # 1. get the files
    path = "D:\\.plex\\.sus\\"
    files.add_dir(path)
    files.randomize()

    # 2. set up GUI
    root = BaseTkContainer()

    # 3. set up video streams
    root.frame.columnconfigure(0, weight=1)
    root.frame.columnconfigure(1, weight=1)

    root.add_player(0,0,files.dequeue())
    root.add_player(0,1,files.dequeue())
    root.add_player(1,0,files.dequeue())
    root.add_player(1,1,files.dequeue())

    # 4. create perodic update function to refresh finished streams
    root.update_window()
    root.root.mainloop()
    