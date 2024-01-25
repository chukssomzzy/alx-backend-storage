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
    def wrapper(url, *args, **kwargs) -> str:
        """Cache return in redis"""
        r.incr(f"count:{url}")
        res = r.get(f"result:{url}")
        if res:
            return res.decode('utf-8')
        res = f(url, *args, **kwargs)
        r.setex(f"result:{url}", timedelta(seconds=10), res)
        return res
    return wrapper


@track
def get_page(url: str) -> str:
    """Get a page and cache if neccessary.
    """
    r = requests.get(url)
    return (r.content.decode("utf-8"))
