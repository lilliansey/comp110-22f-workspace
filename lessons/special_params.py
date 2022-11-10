"""Examples of optional parameters and Union types."""

from typing import Union


def hello(name: Union[str, int] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    else: 
        greeting += "COMP" + str(name)
    return greeting

# Single-argument
print(hello("Sally"))

# No arguements!
print(hello())

print(hello(110))