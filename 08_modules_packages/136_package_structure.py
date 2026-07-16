print("""
A Python package is a directory containing Python files and an __init__.py file.

Example structure:
    mypackage/
        __init__.py
        utils.py
        models.py

To use it:
    import mypackage
    from mypackage import utils
    from mypackage.models import User

The __init__.py file can be empty or define what gets exported:
    from .utils import helper_function
    from .models import User

Sub-packages are nested packages:
    mypackage/
        __init__.py
        api/
            __init__.py
            views.py
        db/
            __init__.py
            models.py
""")
