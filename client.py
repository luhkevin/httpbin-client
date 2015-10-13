import requests
import random
import time
import logging
import pool

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('/tmp/demo.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s;%(message)s", "%s")
handler.setFormatter(formatter)

logger.addHandler(handler)

protocol= "http://"
host = "httpbin-servers.gencore.io:"
port = str(80)

period = 200
count=0
while True:
    count = (count + 1) % period
    dosleep=random.randint(0,1500)

    ua_header = random.choice(pool.UA_headers)
    headers = {ua_header[0]:ua_header[1]}

    if dosleep == 1500:
        time.sleep(0.5)
    else:
        # .... TODO: remember to switch this to "post" if our url is /post
        try:
            uri = random.choice(pool.uris)
            url = protocol + host + port + "/" + uri
            if uri.startswith("/post"):
                r = requests.post(url, headers=headers)
            else:
                r = requests.get(url, headers=headers)
        except Exception, e:
            print e

    if count == 0:
        try:
            for uri in pool.periodic_uris:
                url = protocol + host + port + "/" + uri
                print "url is: ", url
                r = requests.get(url, headers=headers)
        except Exception, e:
            print e
