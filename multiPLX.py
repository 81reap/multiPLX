import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

import vlc, queue
import tkinter as tk
from tkinter import ttk
from video_player import video_player as vp

N = 3
files = queue.queue()

class BaseTkContainer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("lqud")
        self.root.protocol("WM_DELETE_WINDOW", self.delete_window)
        self.root.geometry("1920x1080") # default to 1080p
        self.root.configure(background='black')
        self.root.size = self.root.winfo_width() - self.root.winfo_height()
        #self.root.resizable(0, 0)
        
        self.theme = ttk.Style()
        self.theme.theme_use("alt")
        
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.players = []

    def delete_window(self):
        tk_instance = self.root
        tk_instance.quit()
        tk_instance.destroy()
        os._exit(1)

    def update_window(self):
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        for player in self.players:
            # resize player to fit current window
            if self.root.size != width-height:
                player.player.configure(width=width//N, height=height//N)

            if player.isDone() :
                print("update :: new media")
                player.playMedia(files.dequeue())
        
        self.root.after(1000, self.update_window)

    def add_player(self, row, col, file):
        player = vp(self.frame, row, col)
        player.playMedia(file)
        self.players.append(player)
    
    def __repr__(self):
        return "Base tk Container"

if __name__ == "__main__":
    # 1. get the files
    path = "D:\\.plex\\.sus\\"
    files.add_dir(path)
    files.randomize()

    # 2. set up GUI
    root = BaseTkContainer()

    # 3. set up video streams
    for col in range(0, N):
        for row in range(0, N):
            root.add_player(col, row, files.dequeue())

    # 4. create perodic update function to refresh finished streams
    root.update_window()
    root.root.mainloop()
    