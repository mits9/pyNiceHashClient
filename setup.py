# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyNiceHashClient',
    version='0.1.0',
    description='Library in Python to access NiceHash.com API',
    long_description=readme,
    author='MikeInTimeSaves9',
    author_email='mikeintimesaves9@gmail.com',
    url='https://github.com/mits9/pyNiceHashClient',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
