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
host = "127.0.0.1:"
port = str(5000)

while True:
    dosleep=random.randint(0,1500)

    if dosleep == 750:
        time.sleep(1)
    else:
        url = random.choice(pool.urls)

        # .... TODO: remember to switch this to "post" if our url is /post
        try:
            r = requests.get(protocol + host + port + '/' + url)
        except Exception, e:
            print e

