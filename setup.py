from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

import os

import numpy as np

with open(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8",
) as f:
    long_description = f.read()

extensions = [
    Extension(
        "mujoco_py_derivatives",
        [
            "mujoco_py_derivatives/mujoco_py_derivatives.pyx",
            # "mujoco_py_derivatives/mujoco_py_derivatives.c",
        ],
        include_dirs=[
            np.get_include(),
            "{home}/.mujoco/mujoco200/include/".format(home=os.path.expanduser("~")),
        ],
        library_dirs=["{home}/.mujoco/mujoco200/bin/".format(home=os.path.expanduser("~"))],
        extra_compile_args=["-fopenmp"],
        libraries=["mujoco200", "glew", "GL", "gomp", "m"],
    ),
]

setup(
    name="mujoco-py-derivatives",
    version="0.1.1",
    ext_modules=cythonize(extensions),
    # ext_modules=extensions,
    install_requires=["mujoco-py", "keyword2cmdline==1.3.0", "kwplus>=0.3.0", "numpy", "Cython"],
    package_data={"": ["*.xml", "*.stl", "*.so", "*.pyd", "*.pyx"],},
    author="Daniel Suo",
    author_email="danielsuo@gmail.com",
    description=long_description,
    license="MIT",
    keywords="mujoco mujoco_py derivativesative",
    url="https://github.com/MinRegret/mujoco_py_derivatives",  # project home page, if any
)

