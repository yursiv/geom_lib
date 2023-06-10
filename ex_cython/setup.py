from distutils.core import setup, Extension
from Cython.Build import cythonize

import Cython.Compiler.Options

Cython.Compiler.Options.annotate = True

import numpy

"""
python setup.py build_ext --inplace
"""

if __name__ == '__main__':
    exts = [
        Extension('optimize',
                  sources=['optimize.pyx'],
                  include_dirs=[numpy.get_include()]),

    ]

    setup(name='optimize', version='1.0', author='yursiv', ext_modules=cythonize(exts, annotate=True))

"""
T:\Programs\VisualStudio\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD 
-IC:\Users\yursiv\AppData\Roaming\Python\Python310\site-packages\numpy\core\include 
-IC:\Python\Python310\include 
-IC:\Python\Python310\Include 
-IT:\Programs\VisualStudio\VC\Tools\MSVC\14.29.30133\ATLMFC\include 
-IT:\Programs\VisualStudio\VC\Tools\MSVC\14.29.30133\include 
-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\ucrt 
-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\shared 
-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\um 
-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\winrt 
-IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\cppwinrt /Tcoptimize.c /Fobuild\temp.win-amd64-3.10\Release\optimize.obj
optimize.c
"""
