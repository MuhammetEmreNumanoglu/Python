import warnings

def old_function():
    warnings.warn("old_function is deprecated, use new_function instead", DeprecationWarning, stacklevel=2)
    return 42

result = old_function()
print(result)

def risky_divide(a, b):
    if b == 0:
        warnings.warn("Dividing by zero will cause issues", RuntimeWarning)
        return None
    return a / b

risky_divide(10, 0)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    old_function()

warnings.filterwarnings("error", category=DeprecationWarning)
try:
    old_function()
except DeprecationWarning as e:
    print("Caught as error:", e)
