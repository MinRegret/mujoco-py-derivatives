from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

import os

import numpy as np

DIR = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(DIR, "README.md"), encoding="utf-8",) as f:
    long_description = f.read()

extensions = [
    Extension(
        "mujoco_py_derivatives",
        [
            os.path.join(DIR, "src/mujoco_py_derivatives.pyx"),
            os.path.join(DIR, "src/mujoco_derivatives_struct.c"),
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
    version="0.1.2",
    ext_modules=cythonize(extensions),
    install_requires=["mujoco-py", "keyword2cmdline==1.3.0", "kwplus>=0.3.0", "numpy", "Cython"],
    package_data={"": ["*.xml", "*.stl", "*.so", "*.pyd", "*.pyx"],},
    author="Daniel Suo",
    author_email="danielsuo@gmail.com",
    description="Derivatives for MuJoCo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="mujoco mujoco_py derivatives",
    url="https://github.com/MinRegret/mujoco-py-derivatives",
)

