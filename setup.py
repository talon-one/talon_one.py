# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='talon_one',
    version='1.0.0',
    description='Talon.One Python SDK',
    long_description=readme,
    author='Martin Wiso',
    author_email='wiso@talon.one',
    url='https://github.com/talon_one/talon_one.py',
    license=license,
    packages=find_packages(exclude=('tests'))
)
