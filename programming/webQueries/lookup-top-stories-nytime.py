import requests
import os
from pprint import pprint

apikey = os.getenv('NYTIME_APIKEY', '....')

# Top Stories
# https://developer.nytiems.com/docs/top-stories-product/1/overview
section = "science"
query_url = f"https://api.nytime.com/svc/topstories/v2/{section}.json?api-key={apikey}"

r = requests.get(query_url)
pprint(r.json())

