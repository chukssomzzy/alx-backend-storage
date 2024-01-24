#!/usr/bin/env python3
"""redis Cache class
"""

from typing import Callable, Optional, Union
import redis
import uuid

from redis.commands.core import ResponseT


class Cache:
    """Redis cache implementation
    """

    def __init__(self) -> None:
        """setup cache instance
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data and return a key
        args:
            data (str|float|int|bytes): value to store in redis database
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Get an value for the provided key
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value
