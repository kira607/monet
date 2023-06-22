"""The Result class represents the outcome of an operation."""


from typing import Any, Callable, Iterable


class Result:
    """
    Represents the outcome of an operation.

    Attributes
    ----------
    success : bool
        A flag that is set to True if the operation was successful, False if
        the operation failed.
    value : object
        The result of the operation if successful, value is None if operation
        failed or if the operation has no return value.
    error : str
        Error message detailing why the operation failed, value is None if
        operation was successful.
    """

    def __init__(
        self, success: bool, value: Any, error: str | None
    ) -> None:  # noqa: ANN401
        """Represent the outcome of an operation."""
        self.success = success
        self.error = error
        self.value = value

    def __str__(self) -> str:
        """Informal string representation of a result."""
        if self.success:
            return "[Success]"
        return f"[Failure] {self.error}"

    def __repr__(self) -> str:
        """Official string representation of a result."""
        if self.success:
            return f"<Result success={self.success}>"
        return f'<Result success={self.success}, message="{self.error}">'

    @property
    def failure(self) -> bool:
        """Flag that indicates if the operation failed."""
        return not self.success

    def on_success(
        self, func: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> Any:  # noqa: ANN401
        """Pass result of successful operation (if any) to subsequent function."""
        if self.failure:
            return self
        if self.value:
            return func(self.value, *args, **kwargs)
        return func(*args, **kwargs)

    def on_failure(
        self, func: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> Any:  # noqa: ANN401
        """Pass error message from failed operation to subsequent function."""
        if self.success:
            return self.value if self.value else None
        if self.error:
            return func(self.error, *args, **kwargs)
        return func(*args, **kwargs)

    def on_both(
        self, func: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> Any:  # noqa: ANN401
        """Pass result (either succeeded/failed) to subsequent function."""
        if self.value:
            return func(self.value, *args, **kwargs)
        return func(*args, **kwargs)

    @staticmethod
    def fail(error_message: str) -> "Result":
        """Create a Result object for a failed operation."""
        return Result(False, value=None, error=error_message)

    @staticmethod
    def ok(value: Any = None) -> "Result":  # noqa: ANN401
        """Create a Result object for a successful operation."""
        return Result(True, value=value, error=None)

    @staticmethod
    def combine(results: Iterable["Result"]) -> "Result":
        """Return a Result object based on the outcome of a list of Results."""
        if all(result.success for result in results):
            return Result.ok()
        errors = [str(result.error) for result in results if result.failure]
        return Result.fail("\n".join(errors))
