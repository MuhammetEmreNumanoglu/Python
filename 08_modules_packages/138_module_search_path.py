import sys

print("Module search path:")
for path in sys.path:
    print(" ", path)

import math
print("\nmath module file:", math.__file__)

import os
print("os module file:", os.__file__)

import json
print("json module file:", json.__file__)
