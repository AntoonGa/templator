"""File: foo.py | Author: user | date: Sat Sep 21 2024

Description: A simple module that serves as an example.
"""

import logging

from templator import setup_logging

logger = logging.getLogger("foo")
setup_logging()


def foo(arr: list) -> list:
    """This is a docstring that follows the nice Google standard

    Args:
        arr (list): a collection of things.

    Returns:
        list: the exact same collection of things.
    """
    if not isinstance(arr, list):
        msg = f"Expected a list, got {type(arr)}"
        logger.error(msg)
        raise TypeError
    msg = f"Received {arr}"
    logger.info(msg)
    return arr


if __name__ == "__main__":
    # Always nice to add an entry point to the module
    array = list(range(100))
    foo(array)
