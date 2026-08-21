print("""
pdb (Python Debugger) lets you step through code interactively.

To use:
    import pdb; pdb.set_trace()
    or
    breakpoint()   (Python 3.7+)

Common pdb commands:
    n (next)       - Execute next line
    s (step)       - Step into function
    c (continue)   - Continue execution
    p var          - Print variable value
    l (list)       - Show surrounding code
    q (quit)       - Quit debugger
    h (help)       - Show help

Example usage in code:
""")

def buggy_function(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

data = [1, 2, 3, 4, 5]
result = buggy_function(data)
print(f"Result: {result}")
print("Run: python -m pdb 237_pdb_debugger.py to start debugging")
