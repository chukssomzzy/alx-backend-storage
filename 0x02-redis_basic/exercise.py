#!/usr/bin/env python3
"""redis Cache class"""

from typing import Any, Callable, Union
import redis
import uuid

from redis.commands.core import ResponseT


class Cache:
    """Redis cache implementation"""
    data_types = [str.__name__, float.__name__, int.__name__, bytes.__name__]

    def __init__(self) -> None:
        """setup cache"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> Union[str, None]:
        """takes a data and return a key
        args:
            data (str|float|int|bytes): value to store in redis database
        """

        if data and type(data).__name__ in self.data_types:
            key = str(uuid.uuid4())
            self._redis.set(key, data)
            return key

