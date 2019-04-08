from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    cythonize("Algorithms/ConstraintSatisfactionProblem.py"),
    cythonize("Algorithms/ForwardChecking.py"),
#   ... all your modules that need be compiled ...
]
setup(
    name = 'My Program Name',
    ext_modules = ext_modules
)