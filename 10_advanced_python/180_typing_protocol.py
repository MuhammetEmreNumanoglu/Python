from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None:
        ...

@runtime_checkable
class Resizable(Protocol):
    def resize(self, factor: float) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

    def resize(self, factor: float) -> None:
        print(f"Resizing circle by {factor}")

class Square:
    def draw(self) -> None:
        print("Drawing square")

    def resize(self, factor: float) -> None:
        print(f"Resizing square by {factor}")

def render(shape: Drawable) -> None:
    shape.draw()

shapes = [Circle(), Square()]
for shape in shapes:
    render(shape)
    print(isinstance(shape, Drawable))
    print(isinstance(shape, Resizable))
