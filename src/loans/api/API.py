import urllib.request
import json

from django.conf import settings


def get_autorization_api(legal_number, gender, email):
    url_api = settings.HOST_API
    url_api += '?document_number={0}&gender={1}&email={2}'.format(
        legal_number,
        gender,
        email
    )
    request = urllib.request.Request(url_api)
    try:
        connection = urllib.request.urlopen(request) 
    except urllib.HTTPError as e:
        connection = e
    if connection.code == 200:
        data = connection.read()
        return json.loads(data)
    else:
        return {'error': 'true'}
