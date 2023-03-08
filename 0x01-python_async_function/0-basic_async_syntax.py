#!/usr/bin/env python3
"""
Basic Async Syntax
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:

    """
    synchronous coroutine that takes
    an integer argument
    """
    delay = random.uniform(0, max_delay)
    

    return

