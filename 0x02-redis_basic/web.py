#!/usr/bin/env python3

"""Web.py cache webpage.
"""
from datetime import timedelta
import functools
from typing import Callable

import redis
import requests

r = redis.Redis()
""" One time connection"""


def track(method: Callable) -> Callable:
    """Cache return and url"""

    @functools.wraps(method)
    def wrapper(url) -> str:
        """Cache return in redis"""
        r.incr("count:{}".format(url))
        res = r.get("result:{}".format(url))
        if res:
            return res.decode('utf-8')
        res = method(url)
        r.set("count:{}".format(url), 1)
        r.setex("result:{}".format(url), timedelta(seconds=10), res)
        return res
    return wrapper


@track
def get_page(url: str) -> str:
    """Get a page and cache if neccessary.
    """
    return requests.get(url).text
