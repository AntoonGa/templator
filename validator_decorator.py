"""File: validator_decorator.py | Author: username | date: Sun Sep 22 2024

.. include:: readme.md
Description:
A decorator to validate arguments passed to a function or method.
This is a slight modification of the validate_call() pydantic decorator.
However you may now pass a model to use for custom validation.
"""

import functools
import inspect
import logging
from collections.abc import Callable

import numpy as np
from pydantic import BaseModel, ConfigDict, PositiveInt
from pydantic._internal import _typing_extra, _validate_call

logger = logging.getLogger("Pydantic validators")


def validate_args(
    func: Callable | None = None,
    /,
    *,
    validate_return: bool = False,
    model: type[BaseModel] | None = None,
) -> Callable[[Callable], Callable]:
    """Used as a decorator to validate argument passed to a function or method.

    This function is a slight modification of the validate_call() pydantic decorator:
    https://docs.pydantic.dev/2.8/concepts/validation_decorator/

    This version enables you to pass a custom pydantic model (inheriting from BaseModel) and use
    your own validation methods.

    Returns a decorated wrapper around the function that validates the arguments and, optionally,
    the return value.


    Args:
        func: The function to be decorated.
        validate_return: Whether to validate the return value.
        model: The Pydantic model to use for custom validation.

    Returns:
        The decorated function.
    """
    local_ns = _typing_extra.parent_frame_namespace()

    def validate(function: Callable) -> Callable:
        if isinstance(function, (classmethod | staticmethod)):
            name = type(function).__name__
            msg = (
                f"The `@{name}` decorator should be applied "
                f"after `@validate_args` (put `@{name}` on top)"
            )
            logger.error(msg)
            raise TypeError(msg)

        @functools.wraps(function)
        def wrapper_function(*args, **kwargs):  # noqa: ANN202
            try:
                # If a model is passed, combine args and kwargs into a single dictionary and
                # instantiate model
                if model:
                    # Get the function's signature
                    sig = inspect.signature(function)
                    # Combine args and kwargs into a single dictionary, including default values
                    bound_args = sig.bind_partial(*args, **kwargs)
                    bound_args.apply_defaults()
                    combined_args = bound_args.arguments
                    # Validate using the Pydantic model
                    _ = model(**combined_args)
                    # function call
                    return function(**combined_args)
                # If no model is passed, use the validate_call of pydantic
                else:  # noqa: RET505
                    config = ConfigDict(strict=True, arbitrary_types_allowed=True)
                    validate_call_wrapper = _validate_call.ValidateCallWrapper(
                        function, config, validate_return, local_ns
                    )
                return validate_call_wrapper(*args, **kwargs)
            except Exception:
                _msg = "Argument validation failed: "
                logger.exception(_msg)
                raise

        wrapper_function.raw_function = function

        return wrapper_function

    if func:
        return validate(func)
    return validate


if __name__ == "__main__":

    class ParamModel(BaseModel):
        """Argument validation model"""
        class Config:  # noqa: D106
            arbitrary_types_allowed = True  # enable arbitrary types in pydantic
            validate_assignment = True  # force validation at each new assignment

        a: int
        b: str
        c: float
        d: list[int]
        e: np.ndarray
        z: PositiveInt

    @validate_args(model=ParamModel)
    def my_func(a: int, b: str, c: float, d: list[int], e: np.ndarray, z: int) -> None:  # noqa: PLR0913
        """This function's arguments are all described in the ParamModel"""
        print(a, b, c, d, e, z)  # noqa: T201

    # This will work fine !
    my_func(1, "2", 3.0, [4, 5, 6], np.array([7, 8, 9]), 10)
    # This won't work !
    try:
        my_func(1, "2", 3.0, [4, 5, 6], np.array([7, 8, 9]), -10)
    except Exception as e:
        print(e)

    try:
        my_func(1, "2", 3.0, [4, 5, 6], "hi", 10)
    except Exception as e:
        print(e)

    try:
        my_func(1, "2", 3.0, np.ndarray([4, 5, 6]), np.array([7, 8, 9]), 10)
    except Exception as e:
        print(e)

    try:
        my_func(1, "2", [1,2,3], [4, 5, 6], np.array([7, 8, 9]), 10)
    except Exception as e:
        print(e)

    try:
        my_func(1, 2, 3.0, [4, 5, 6], np.array([7, 8, 9]), 10)
    except Exception as e:
        print(e)

    try:
        my_func("hello", "2", 3.0, [4, 5, 6], np.array([7, 8, 9]), 10)
    except Exception as e:
        print(e)

