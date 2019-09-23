import sys
import argparse
from request_user import User
from stats_helper import Stats
import time


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--users', action='store', type=int, required=True)
    arg_parser.add_argument('--conc', action='store', type=int, required=True)
    arg_parser.add_argument('--host', action='store', type=str, required=True)
    args = arg_parser.parse_args()

    number_of_users = args.users
    concurrency = args.conc
    host = args.host

    stats = Stats()

    users = []

    for i in range(int(number_of_users)):
        users.append(User(concurrency, host, stats))

    for user in users:
        user.send_requests()

    stats.set_finish(time.time())

    print(stats.calc_execution_time())
    print(stats.get_not_found())
    print(stats.get_server_error())

    

