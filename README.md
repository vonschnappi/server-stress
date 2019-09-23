# server-stress
This a small python script that sends multiple requests to test server stress and overload

## What it does
This script creates a bunch of threads that send simoultanous requests to a specified host. It essentially simulates server stress in that it creates a bunch of users who send a bunch of requests. You get the idea...

## Requirements
This server stress script makes use of the requests python package. Install it before you run the script.
https://2.python-requests.org/en/master/
Code was written in python3

## How to run
The main file is server-stress.py. Run this file with the following flags
- --host (required) the host that points to the server that you want to test.
- --users (required) the number of users that you want to simulate.
- --conc (required) concurrency, basically how many concurrent requests you want each "user to make".

## Example
```python server-stress.py --host http://localhost:9000/index.html --users 30 --conc 100```
