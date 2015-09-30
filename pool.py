# could switch this to a generator design...if we care about memory
# Should probably change the delimiter to not be a comma...
def line_parser(line, append_token=None):
    endpoint_tokens = line.split(',')
    if len(endpoint_tokens) == 1:
        return [append_token + endpoint_tokens[0].strip()]
    elif len(endpoint_tokens) > 1:
        endpoint, freq = endpoint_tokens[0].strip(), int(endpoint_tokens[1])
        return freq*[append_token + endpoint]

def load_uris(endpoint_file, append_token=None):
    loaded_uris = list()
    with open(endpoint_file, 'r') as f:
        # The first line is just a description and should be tossed
        f.readline()
        for line in f:
            endpoint = line_parser(line, append_token)
            loaded_uris.extend(endpoint)
    return loaded_uris

basic = load_uris('basic-endpoints')
cookies = load_uris('cookies-endpoints')
status = load_uris('status-endpoints', 'status/')
#post = load_uris('post-endpoints', 'post/')
#custom = load_uris('custom-endpoints')
#response_headers = load_uris('response-headers-endpoints', 'response-headers?')

uris = list()
uris.extend(basic)
uris.extend(status)
uris.extend(cookies)
#uris.extend(post)
#uris.extend(custom)
#uris.extend(response_headers)


UAs = ["curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)",
       "Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1",
       "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:1.8.0.7) Gecko/20110321 MultiZilla/4.33.2.6a SeaMonkey/8.6.55",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A ",
       "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
]
