#!/usr/bin/env python


from distutils.core import setup

package_dir = {'': 'src'}
py_modules = ['main']
requires = []
scripts = ['main.py']

setup(name = 'objRec',
      version = '1.0', 
      author = 'Divyanshu Kakwani',
      package_dir = package_dir,
      py_modules = py_modules,
      requires = requires)
