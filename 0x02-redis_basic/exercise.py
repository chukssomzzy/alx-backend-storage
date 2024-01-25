#!/usr/bin/env python3
'''redis Cache class
'''

import functools
import uuid
from typing import Any, Callable, Optional, Union

import redis


def count_calls(method: Callable) -> Callable:
    '''decorator to track how many times Cache has been initialized.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        '''Wraps function passed to count_calls'''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''Cache calls history.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        '''Wrapper that function returns and execute the function.
        '''
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush("{}:inputs".format(method.__qualname__),
                              str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush("{}:outputs".format(method.__qualname__), output)
        return output
    return wrapper


class Cache:
    '''Redis cache implementation.
    '''
    def __init__(self) -> None:
        '''setup cache instance
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''takes a data and return a key  value to store in redis database.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        ''' Get an value for the provided key.
        '''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_int(self, key: str) -> int:
        '''return get with function as int.
        '''
        return self.get(key, lambda val: int(val))

    def get_str(self, key: str) -> int:
        '''return get with function as int.
        '''
        return self.get(key, lambda val: val.decode("utf-8"))
