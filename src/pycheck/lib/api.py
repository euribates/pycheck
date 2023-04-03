import json
import urllib.request

from pycheck import settings

URL_ALL_BADGES = f'{settings.URL_API}/badges/all/'
URL_LOGIN = f'{settings.URL_API}/login/'
URL_OWNED_BADGES = f'{settings.URL_API}/badges/owned/'
URL_SCORE = f'{settings.URL_API}/score/'
URL_STATUS = f'{settings.URL_API}/status/'
URL_SUBMIT = f'{settings.URL_API}/submit/'


STATUS_OK = 'ok'


def api_get(url):
    with urllib.request.urlopen(url) as response:
        body = response.read()
        return json.loads(body)


def api_post(url, **kwargs):
    params = json.dumps(kwargs).encode('utf8')
    req = urllib.request.Request(
        url,
        data=params,
        headers={'content-type': 'application/json'},
    )
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode('utf8'))
    return result
