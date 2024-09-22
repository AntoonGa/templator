"""File: time_profiling.py | Author: agarcon | date: Sun Sep 22 2024

.. include:: readme.md
Description: A set of time profiling utilities
TODO @agarcon:
"""

import logging
import logging.config
import time
from collections.abc import Generator
from contextlib import contextmanager

from pyinstrument import Profiler

logger = logging.getLogger("TimeProfiler")
logging.basicConfig(level=logging.DEBUG)

@contextmanager
def time_profiler(path: str | None = None) -> Generator:
    """A context manager for profiling a section of code.

    Takes an optional `path` parameter, defaulting to "profile.html", to specify the output file.
    Yields a `Profiler` object for the section, and upon exit, stops the profiler, writes the
    results to the specified file, and prints the results.

    Args:
        path (str | None, optional): The path to the output file.
    """
    # make sure the path ends with .html
    profiler = Profiler(interval=0.001)
    try:
        profiler.start()
        yield profiler
    finally:
        profiler.stop()
        profiler.print()
        if path:
            if path[-4:] != "html":
                path = path + ".html"
            profiler.write_html(path)


@contextmanager
def time_print() -> Generator:
    """Weak profiler that prints the elapsed time to the console.

    Use as a context manager:
    >>> with time_print():
    >>>     do_something()
    """
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        msg = f"Elapsed time: {elapsed_time:.4f} seconds"
        logger.info(msg)


def stats(func: callable) -> callable:
    """Time a method or function runtime and push exec time to logger

    Use as a decorator:
    >>> @stats
    >>> def my_method():
    >>>     do_something()
    """
    def wrapper(*args, **kwargs):  # noqa: ANN202
        try:
            class_name = args[0].__class__.__name__  # Get the class name from the first argument (self)
        except IndexError:
            class_name = ""

        method_name = func.__name__  # Get the method name
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        msg = f"{class_name}.{method_name} executed in {execution_time:.4f} seconds"
        logger.info(msg)
        return result

    return wrapper

if __name__ == "__main__":
    def _long_running_func() -> list[int]:
        arr = []
        for i in range(100000):
            arr.append(i)
            arr.pop(0)
        return arr

    # profile with context manager, no output
    with time_profiler() as p:
        _long_running_func()

    # profile with context manager, output to profile.html
    with time_profiler("profile.html") as p:
        _long_running_func()

    # weak profiling with time prints
    with time_print() as p:
        _long_running_func()

    # In loops
    for _ in range(10):
        with time_print() as p:
            _long_running_func()

    # profiling with decorator
    @stats
    def _long_running_func_decorated() -> list[int]:
        arr = []
        for i in range(100000):
            arr.append(i)
            arr.pop(0)
        return arr

    _long_running_func_decorated()
