#!/usr/bin/env python3
""" Module: Redis Server, use redis for basic operations,
    to use redis as a simple cache"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Method: count calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Method: Wrapper """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and
    outputs for a particular function.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Method: Wrapper"""
        inputs = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", inputs)
        outputs = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", outputs)
        return outputs
    return wrapper


def replay(fn: Callable):
    """Function: show the history of calls of a particular function."""
    redis = fn.__self__._redis
    value = fn.__qualname__
    count = redis.get(value).decode("utf-8")
    print(f"{value} was called {count} times:")
    inputs = redis.lrange(value + ":inputs", 0, -1)
    outputs = redis.lrange(value + ":outputs", 0, -1)
    merge_list = list(zip(inputs, outputs))
    for inp, out in merge_list:
        argument, data = inp.decode("utf-8"), out.decode("utf-8")
        print(f"{value}(*{argument}) -> {data}")


