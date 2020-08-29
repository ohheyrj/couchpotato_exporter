from prometheus_client import Gauge, start_http_server
import urllib3
from urllib.parse import urljoin
import json
import os

COUCHPOTATO_URL = os.environ.get('COUCHPOTATO_URL')
COUCHPOTATO_API_KEY = os.environ.get('COUCHPOTATO_API_KEY')
COUCHPOTATO_BASE_API = f"{COUCHPOTATO_URL}/api/{COUCHPOTATO_API_KEY}"

TOTAL_MOVIES = Gauge('couchpotato_total_movies', 'Total Number of Movies in CouchPotato')
TOTAL_ACTIVE = Gauge('couchpotato_total_wanted', 'Total number of movies wanted in couchpotato')
TOTAL_DONE = Gauge('couchpotato_total_done', 'Total number of movies done')

def couchpotato_client(api_method, params=None):
    api_call = urllib3.PoolManager()
    if params:
        url = f"{COUCHPOTATO_BASE_API}/{api_method}/?{params}"
    else:
        url = f"{COUCHPOTATO_BASE_API}/{api_method}"

    try:
        r = api_call.request('GET', url)
        return json.loads(r.data)
    except urllib3.exceptions.HTTPError:
        print("Cannot complete request")

def total_movies():
    data = couchpotato_client("movie.list")
    TOTAL_MOVIES.set(data.get('total'))

def total_active():
    data = couchpotato_client("movie.list", "status=active")
    TOTAL_ACTIVE.set(data.get('total'))

def total_done():
    data = couchpotato_client("movie.list", "status=done")
    TOTAL_DONE.set(data.get('total'))

if __name__ == '__main__':
    start_http_server(9316, addr='0.0.0.0')
    while True:
        total_movies()
        total_active()
        total_done()