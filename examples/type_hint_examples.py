"""Type hints document intent; they do not enforce runtime types by themselves."""
from typing import Callable, Protocol, Sequence, TypeVar

T = TypeVar('T')


def first_element(items: Sequence[T]) -> T:
    if not items:
        raise ValueError('Sequence must not be empty')
    return items[0]


def apply(function: Callable[[int, int], int], x: int, y: int) -> int:
    return function(x, y)


class Drawable(Protocol):
    def draw(self) -> str: ...


class Circle:
    def draw(self) -> str:
        return 'Drawing a demo circle'


def render(item: Drawable) -> str:
    return item.draw()


if __name__ == '__main__':
    print(first_element(['Demo A', 'Demo B']))
    print(apply(lambda a, b: a+b, 2, 3))
    print(render(Circle()))
