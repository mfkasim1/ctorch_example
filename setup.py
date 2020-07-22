from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import setuptools

__version__ = '0.0.1'

ext_name = "example.csrc"
cpp_sources = [
    "src/add.cpp"
]

def get_pybind_include():
    import pybind11
    return pybind11.get_include()

def get_torch_cpp_extension():
    from torch.utils.cpp_extension import CppExtension
    return CppExtension(
        name=ext_name,
        sources=cpp_sources,
        include_dirs=[get_pybind_include()],
    )

def get_build_extension():
    from torch.utils.cpp_extension import BuildExtension
    return BuildExtension

setup(
    name='example',
    version=__version__,
    author='Muhammad Kasim',
    author_email='firman.kasim@gmail.com',
    url='https://github.com/mfkasim91/ctorch_example',
    description='A test project using pybind11 and torch C++ extension',
    long_description='',
    ext_modules=[get_torch_cpp_extension()],
    setup_requires=["pybind11>=2.5.0", "torch>=1.2.0"],
    cmdclass={'build_ext': get_build_extension()},
    zip_safe=False,
)
