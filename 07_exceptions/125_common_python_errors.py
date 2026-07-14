errors = [
    (lambda: 1 / 0, ZeroDivisionError),
    (lambda: int("abc"), ValueError),
    (lambda: [][0], IndexError),
    (lambda: {}["missing"], KeyError),
    (lambda: open("/no/such/file"), FileNotFoundError),
    (lambda: None + 1, TypeError),
    (lambda: None.strip(), AttributeError),
]

for func, expected in errors:
    try:
        func()
    except expected as e:
        print(f"{expected.__name__}: {e}")
