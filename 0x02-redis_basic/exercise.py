#!/usr/bin/env python3
"""redis Cache class"""

from typing import Any, Callable, Union
import redis
import uuid

from redis.commands.core import ResponseT


class Cache:
    """Redis cache implementation"""
    data_types = [str, float, int, bytes]

    def __init__(self) -> None:
        """setup cache"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """takes a data and return a key
        args:
            data (str|float|int|bytes): value to store in redis database
        """
        key = ""
        if type(data) in self.data_types:
            key = str(uuid.uuid4())
            self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> Any:
        """get an item from redis cache"""
        value: ResponseT = self._redis.get(key)
        if value:
            value = fn(value)
        return value

    def get_int(self, key: str) -> int:
        """Paramitarize Cache.get with the correct function"""
        return self.get(key, int)

    def get_str(self, key: str) -> str:
        """Paramitarize Cache.get with the correct convertion function """
        return self.get(key, str)
