import requests
from requests.adapters import HTTPAdapter
from request_threads import Threader

class User:
    def __init__(self, concurrency, host, stats):
        self.concurrency = concurrency
        self.host = host
        self.stats = stats
        self.threader = Threader(self.concurrency, self.send_request, self.host)
        self.threads = self.threader.get_threads()
        print(self)

    def send_request(self, host):
        try:
            req = requests.Request('GET', host)
            r = req.prepare()
            s = requests.Session()
            s.mount(host, HTTPAdapter(pool_maxsize=9000))
            res = s.send(r, timeout=3)
            if res.status_code == 404:
                self.stats.log_not_found()
            if res.status_code == 500:
                self.stats.log_server_error()
        except requests.exceptions.Timeout as e:
            self.stats.log_timeout()
            print('timeout')
        except requests.exceptions.ConnectionError as e:
            print('con error')
        except requests.exceptions.HTTPError as e:
            print('http error')

    def send_requests(self):
        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()

    