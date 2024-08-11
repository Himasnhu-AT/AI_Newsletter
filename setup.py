from setuptools import setup
from Cython.Build import cythonize
from setuptools.command.build_ext import build_ext as build_ext_orig
import os
import shutil
import glob

class build_ext(build_ext_orig):
    def build_extensions(self):
        # Call the original build_ext method
        super().build_extensions()

        # Move .so files to the same directory as the .py files
        for ext in self.extensions:
            for ext_file in ext.sources:
                base, _ = os.path.splitext(os.path.basename(ext_file))
                pattern = os.path.join(self.build_lib, f"{base}.cpython-*.so")
                for so_file in glob.glob(pattern):
                    target_dir = os.path.dirname(ext_file)
                    shutil.move(so_file, target_dir)

setup(
    ext_modules = cythonize(
        ["Bot/**/*.py"],
        exclude=["**/cython.py"]  # Exclude any file named cython.py
    ),
    cmdclass={'build_ext': build_ext},
)
