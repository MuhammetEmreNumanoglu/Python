import tempfile, sys, os

module_code = '''
PI = 3.14159

def area_of_circle(radius):
    return PI * radius ** 2

def perimeter_of_circle(radius):
    return 2 * PI * radius
'''

tmp_dir = tempfile.mkdtemp()
module_path = os.path.join(tmp_dir, "geometry.py")

with open(module_path, "w") as f:
    f.write(module_code)

sys.path.insert(0, tmp_dir)
import geometry

print(geometry.PI)
print(geometry.area_of_circle(5))
print(geometry.perimeter_of_circle(5))

sys.path.pop(0)
import shutil
shutil.rmtree(tmp_dir)
