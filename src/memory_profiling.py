"""File: memory_profiling.py | Author: agarcon | date: Sun Sep 22 2024

.. include:: readme.md
Description: A usefull memory profiling script.
To fetch the package:
>>> pip install -U memory_profiler
Then profile a @profile decorated function:
>>> mprof run script.py
To display the results:
>>> mprof plot

TODO @agarcon:
"""

from memory_profiler import profile


@profile
def _growing_memory_func() -> list[list[int]]:
    """This method allocates memory in a growing fashion.

    Each iteration generates a new list prior to appending it to the array.
    """
    arr = []
    for _ in range(1000):
        arr.append(list(range(10000)))  # noqa: PERF401
    return arr


@profile
def _stable_memory_func() -> list[list[int]]:
    """This method allocates memory in a stable fashion.

    Each iteration appends the same pre-allocated list to the array.
    """
    arr = []
    sublist = list(range(10000))
    for _ in range(1000):
        arr.append(sublist)  # noqa: PERF401
    return arr

if __name__ == "__main__":
    arr = _growing_memory_func()
    # arr = _stable_memory_func()
