#!/usr/bin/env python3
"""
measure_time
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure time of execution
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time() - start_time
    
    return end_time / n
