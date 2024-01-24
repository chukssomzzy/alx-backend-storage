#!/usr/bin/env python3
"""redis setup"""

from typing import Union
import redis
import uuid


class Cache:
    """Redis cache"""
    data_types = [str, float, int, bytes]

    def __init__(self) -> None:
        """setup cache"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> Union[str, None]:
        """takes a data and return a key"""
        if type(data) in self.data_types:
            key = str(uuid.uuid4())
            self._redis.set(key, data)
            return key
