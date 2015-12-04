# .... TODO: support for "post" request
import requests
import grequests
import random
import time
import logging
import pool
import sys
from exceptions import IndexError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('/tmp/demo.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s;%(message)s", "%s")
handler.setFormatter(formatter)

logger.addHandler(handler)

protocol= "http://"
host = "httpbin-servers.gencore.io"
port = "80"

mode = ""
try:
    host = str(sys.argv[1])
    port = str(sys.argv[2])
    mode = str(sys.argv[3])
except IndexError, e:
    print "No arguments given"
except Exception, e:
    print "Error"

period = 200
count=0
uris=pool.uris

# ht = high throughput mode
if mode == "ht":
    uris=pool.ht_uris
elif mode == "hilat":
    uris=pool.hilat_uris
elif mode == "dl":
    uris=pool.dl_uris
elif mode == "mix":
    uris=pool.uris

uri_window_size=len(uris)/10
print uri_window_size
# This goes through the uris and makes asynchronous requests with batch size "uri_window_size"
while True:
    count = (count + 1) % period

    ua_header = random.choice(pool.UA_headers)
    headers = {ua_header[0]:ua_header[1]}

    try:
        random.shuffle(uris)
        uri_ptr=0
        while uri_ptr < len(uris):
            uri_cap = uri_ptr + uri_window_size
            uris_window = uris[uri_ptr:uri_cap]
            rs = (grequests.get(protocol + host + ":" + port + "/" + u, headers=headers) for u in uris_window)
            m = grequests.map(rs)
            print "start: ", uri_ptr, " end: ", uri_cap
            uri_ptr += uri_window_size
    except Exception, e:
        print e

    if count == 0:
        try:
            for uri in pool.periodic_uris:
                url = protocol + host + ":" + port + "/" + uri
                r = requests.get(url, headers=headers)
        except Exception, e:
            print e
