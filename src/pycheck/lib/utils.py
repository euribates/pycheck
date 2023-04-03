import hashlib
import datetime
import subprocess
import sys

import pkg_resources
from rich import print
from typing import Dict, List

from .exceptions import NotAuthorizedError
from pycheck import settings
from . import api
from . import auth


# Parsers


def to_datetime(string_in_iso_8601: str) -> datetime.datetime:
    """Convierte una cadena de texto en formato ISO 8601 en un datetime.
    """
    return datetime.datetime.fromisoformat(string_in_iso_8601)


# Filters


def as_human_date(dt: datetime.date|datetime.datetime) -> str:
    """Representación textual de un objeto date o datetime.
    """
    return dt.strftime('%d/%b/%Y')


def update_pycheck():
    url = f'git+{settings.GITHUB_REPO}'
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', url])


def get_pycheck_version():
    return pkg_resources.get_distribution('pycheck').version


def admin_required():
    key_hash = gen_hash(settings.KEY_ADMIN_PRIVATE)
    if key_hash != settings.KEY_ADMIN_PUBLIC:
        raise NotAuthorizedError()


def gen_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()


def succ_msg(text: str):
    print(f'[green]{settings.SUCCESS_MSG_EMOJI}[/] {text}')


def err_msg(text: str):
    print(f'[red]{settings.ERROR_MSG_EMOJI}[/] {text}')


def warn_msg(text: str):
    print(f'[yellow]{settings.WARNING_MSG_EMOJI}[/] {text}')


def _process_response(response):
    status = response['status']
    if status == 'error':
        err_msg(response['message'])
        raise ValueError(response['message'])
    return response['result']


def get_all_badges() -> List[Dict]:
    '''Todos los badgets posibles.
    '''
    response = api.api_get(api.URL_ALL_BADGES)
    return _process_response(response)


def get_owned_badges() -> List[Dict]:
    token = auth.get_token()
    if token:
        response = api.api_post(api.URL_OWNED_BADGES, token=token)
        result = _process_response(response)
        for item in result:
            item['granted_at'] = to_datetime(item['granted_at'])
        return result
    warn_msg(
        'No puedo localizar el token de autenticación. Seguramente'
        ' necesitas identificarte con el comando `login`.'
        )
    return []
