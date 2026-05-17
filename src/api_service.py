from __future__ import annotations

from typing import Any

import requests
from requests import RequestException

API_URL = "http://worldtimeapi.org/api/timezone/America/Sao_Paulo"


def get_current_time() -> str:
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data: dict[str, Any] = response.json()
    except RequestException as error:
        raise RuntimeError('Falha ao obter horário atual da API.') from error

    if 'datetime' not in data:
        raise RuntimeError('Resposta inválida da API de horário.')

    return data['datetime']
