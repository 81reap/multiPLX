import os, random

class queue():
    def __init__(self):
        self.queue = []

    def add_dir(self, path):
        files = os.listdir( path )
        for file in files:
            self.queue.append(os.path.join(path, file))

    def dequeue(self) -> object:
        tmp = self.queue[0]
        del self.queue[0]
        return tmp
    
    def randomize(self):
        random.shuffle(self.queue)