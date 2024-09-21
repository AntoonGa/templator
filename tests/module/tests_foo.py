"""File: test_foo.py | Author: username | date: Sat Sep 21 2024

.. include:: readme.md
Description:
TODO @username:
"""
import pytest
from templator.module.foo import foo

@pytest.fixture(scope="module")
def test_data() -> list:
    test_data = list(range(10))
    return test_data

def test_foo_types(test_data: list) -> None:
    returned = foo(test_data)
    assert isinstance(returned, list)

def test_foo_shape(test_data: list) -> None:
    returned = foo(test_data)
    assert len(returned) == len(test_data)

def test_foo_values(test_data: list) -> None:
    returned = foo(test_data)
    for i in range(len(returned)):
        assert returned[i] == test_data[i]
    
    

if __name__ == "__main__":
    pytest.main()
