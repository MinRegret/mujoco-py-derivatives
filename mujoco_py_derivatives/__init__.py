import os
import sys
from importlib.machinery import ExtensionFileLoader

DIR = os.path.abspath(os.path.dirname(__file__))
python_version = str(sys.version_info.major) + str(sys.version_info.minor)
cymjd = ExtensionFileLoader(
    "cymjd", os.path.join(DIR, "cymjd.cpython-{}-x86_64-linux-gnu.so".format(python_version))
).load_module()

checkderiv = cymjd.checkderiv
MjDerivative = cymjd.MjDerivative
