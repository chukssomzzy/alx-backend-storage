#!/usr/bin/env python3
"""redis Cache class"""

from typing import Union
import redis
import uuid


class Cache:
    """Redis cache implementation"""

    def __init__(self) -> None:
        """setup cache"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data and return a key
        args:
            data (str|float|int|bytes): value to store in redis database
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
