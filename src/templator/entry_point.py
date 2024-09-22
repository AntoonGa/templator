"""File: entry_point.py | Author: agarcon | date: Sat Sep 21 2024

Description: This script is an entry point for the entire package
TODO @agarcon:
"""

import logging

from templator.module.foo import foo

logger = logging.getLogger("EntryPoint")


def main() -> None:
    """User entry point for the package"""
    arr = list(range(10))
    arr_out = foo(arr)
    logger.info(arr_out)


if __name__ == "__main__":
    main()
