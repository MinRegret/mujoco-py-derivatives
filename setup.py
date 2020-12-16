from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

import os.path as op

import numpy as np

def readlines(f):
    with open(f, encoding='utf-8') as fh:
        return fh.readlines()

extensions = [
    Extension("mujoco_py_deriv",
              ["mujoco_py_deriv.pyx",
               "mujoco_deriv_struct.c"],
              include_dirs=[
                  np.get_include(),
                  "{home}/.mujoco/mujoco200/include/".format(home=op.expanduser("~"))],
              library_dirs=["{home}/.mujoco/mujoco200/bin/".format(home=op.expanduser("~"))],
              extra_compile_args=['-fopenmp -g'],
              libraries=["mujoco200", "glew", "GL", "gomp", "m"]),
]

setup(
    name = 'mujoco-py-derivatives',
    version = '0.2.0',
    ext_modules = cythonize(extensions),
    package_data = {
        '': ['*.xml', '*.stl', '*.so', '*.pyd', '*.pyx'],
    },
    py_modules=['mujoco_py_deriv_dynamics', 'mujoco_py_deriv_cacheutils',
                'mujoco_py_deriv_mujoco_utils'],
    setup_requires=readlines('pip-requirements.txt'),
    install_requires=readlines('pip-requirements.txt'),


    # metadata to display on PyPI
    author="Daniel Suo",
    author_email="danielsuo@gmail.com",
    description=readlines("README.md"),
    license="MIT",
    keywords="mujoco mujoco_py derivative",
    url="https://github.com/MinRegret/mujoco-py-derivatives",   # project home page, if any
)

