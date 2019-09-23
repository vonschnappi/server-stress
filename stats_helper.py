import time

class Stats:

    def __init__(self):
        self.start = time.time()
        self.finish = 0
        self.execution_time = 0
        self.server_error = 0
        self.not_found = 0
        self.timeout = 0
        self.server_error_perc = 0
        self.not_found_perc = 0
        self.timeout_perc = 0

    def set_finish(self, timestamp):
        self.finish = timestamp

    def log_server_error(self):
        self.server_error = self.server_error + 1

    def get_server_error(self):
        return self.server_error
    
    def log_not_found(self):
        self.not_found = self.not_found + 1

    def get_not_found(self):
        return self.not_found

    def log_timeout(self):
        self.timeout = self.timeout + 1

    def calc_execution_time(self):
        return self.finish - self.start
