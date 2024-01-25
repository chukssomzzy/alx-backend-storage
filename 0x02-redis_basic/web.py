#!/usr/bin/env python3

"""Web.py cache webpage.
"""
import functools
from typing import Callable

import redis
import requests


def track(f: Callable) -> Callable:
    """Cache return and url"""
    r = redis.Redis()

    @functools.wraps(f)
    def wrapper(url, *args, **kwargs):
        """Cache return in redis"""
        k = "count:{}".format(url)
        r.incr(k)
        return f(url, *args, **kwargs)
    return wrapper


@track
def get_page(url: str) -> str:
    """Get a page and cache if neccessary.
    """
    r = requests.get(url)
    return (r.content.decode("utf-8"))
