"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a positive integer quantity parsed from *value*.

    Raises:
        ValueError: if *value* cannot be parsed or is not a positive integer.
    """
    result = int(value.strip())
    if result <= 0:
        raise ValueError(f"quantity must be positive, got {result}")
    return result
