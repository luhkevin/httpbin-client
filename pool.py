# could switch this to a generator design...if we care about memory

def line_parser(line):
    endpoint_tokens = line.split(',') 
    if len(endpoint_tokens) == 1:
        return [endpoint_tokens[0].strip()]
    elif len(endpoint_tokens) > 1:
        endpoint, freq = endpoint_tokens[0].strip(), int(endpoint_tokens[1])
        return freq*[endpoint]

def load_urls(endpoint_file):
    loaded_urls = list()
    with open(endpoint_file, 'r') as f:
        # The first line is just a description and should be tossed
        f.readline()
        for line in f:
            endpoint = line_parser(line)
            loaded_urls.extend(endpoint)
    return loaded_urls

basic = load_urls('basic-endpoints')
#cookies = load_urls('cookies-endpoints')
#custom = load_urls('custom-endpoints')
#post = load_urls('post-endpoints')
#response_headers = load_urls('response-headers-endpoints')
status = load_urls('status-endpoints')

urls = list()
urls.extend(basic)
urls.extend(status)
#urls.extend(cookies)
#urls.extend(custom)
#urls.extend(post)
#urls.extend(response_headers)

print len(urls)
