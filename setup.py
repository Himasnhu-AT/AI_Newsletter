from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(
        ["Bot/**/*.py"],
        exclude=["**/cython.py"]  # Exclude any file named cython.py
    )
)
