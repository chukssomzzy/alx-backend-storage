#!/usr/bin/env python3

"""Web.py cache webpage.
"""
from datetime import timedelta
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
        k_cache = "cache:{}".format(url)
        r.incr(k)
        if r.exists(k_cache):
            return r.get(k_cache).decode('utf-8')
        ret = f(url, *args, **kwargs)
        r.setex(k_cache, timedelta(seconds=10), ret)
        return ret
    return wrapper


@track
def get_page(url: str) -> str:
    """Get a page and cache if neccessary.
    """
    r = requests.get(url)
    return (r.content.decode("utf-8"))
