#!/usr/bin/env python3
"""
regular function that returns a asyncio task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    returns a asyncio.task.
    """

    return asyncio.Task(coro)