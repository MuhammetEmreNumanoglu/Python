import math as m
import os as operating_system
import datetime as dt
from collections import defaultdict as dd, Counter as C

print(m.pi)
print(m.sqrt(49))
print(operating_system.getcwd())
print(dt.date.today())

counts = C(["a", "b", "a", "c", "a"])
print(counts)

groups = dd(list)
groups["fruits"].append("apple")
print(dict(groups))
