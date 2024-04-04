def factorial(n: int) -> int:
    """Compute factorial (mathematical shortcut !) of a non negative integer number

    All Napoleon sections have been added to this docstring to see how they get rendered.
    Some wierd behavior depending on a `:` being present in the text string...
    To be investigated.

    Args:
        n: number to factor, must be an non negative integer value.

    Raises:
        ValueError: is not a positive integer

    Returns:
        factorial of supplied integer argument.

    Warning:
        Value can become quite large quickly.

    Examples:
        ```python
        >>> factorial(4)
        24
        >>> factorial(0)
        1
        >>> factorial(-2)
        not non negative integer
        ValueError
        >>> factorial(3.4)
        not non negative integer
        ValueError
        ```

    See Also:
        I love [airports](../../airport/#class-hierarchy).

    """

    if not isinstance(n, int) or n < 0:
        print("not non negative integer")
        raise ValueError

    return 1 if n == 0 else n * factorial(n - 1)
