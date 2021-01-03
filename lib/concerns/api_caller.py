import json
import urllib.request

def get_api_response(question, url, headers):
    data = {
        'type': 'text',
        'text': question
    }
    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    res = urllib.request.urlopen(req)
    return res
