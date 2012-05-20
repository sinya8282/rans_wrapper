#!/usr/bin/env python

"""
setup.py file for wrapper of RANS
"""

from distutils.core import setup, Extension

rans_module = Extension('_rans',
                           sources=['rans_wrap.cxx', 'rans.cxx'],
                        libraries=['gmp', 'gmpxx']
                           )

setup (name = 'rans',
       version = '0.1',
       author      = "Ryoma Sin'ya",
       description = """RANS""",
       ext_modules = [rans_module],
       py_modules = ["rans"],
       )
