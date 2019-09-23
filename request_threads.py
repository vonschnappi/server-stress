import threading

class Threader:
    def __init__(self, concurrency, target, host):
        self.concurrency = concurrency
        self.target = target
        self.threads = []
        self.host = host
    
    def create_threads(self):
        for i in range(int(self.concurrency)):
            self.threads.append(threading.Thread(target=self.target, args=[self.host]))
        return self.threads

    def get_threads(self):
        return self.create_threads()


