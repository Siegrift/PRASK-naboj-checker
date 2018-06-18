import os
import subprocess
import shutil
import hashToJs


def file(*path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), *path)


if not os.path.exists(file("..", "vstupy")):
    os.mkdir(file("..", "vstupy"))

with open(file("order.txt")) as order:
    for index, directory in enumerate(order, 1):
        print(directory[:-1])
        d = lambda *path: file(directory[:-1], *path)
        with open(d("data.in"), "wb") as data_in:
            subprocess.run(["python3", d("gen.py")], stdout=data_in)
        with open(d("data.in"), "rb") as data_in, open(d("data.out"),
                                                       "wb") as data_out:
            subprocess.run(
                ["python3", d("sol.py")], stdin=data_in, stdout=data_out)
        shutil.copy(d("data.in"), file("..", "vstupy", "%02d.in" % index))

hashToJs.main()
