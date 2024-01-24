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

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """takes a data and return a key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key