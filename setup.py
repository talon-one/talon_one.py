# coding: utf-8

from setuptools import setup, find_packages
import pathlib

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

NAME = "talon-one-python-sdk"
VERSION = "8.0.0"

# Get the long description from the README.md file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Talon.One Python SDK",
    author="Talon.One GmbH",
    author_email="devs@talon.one",
    url="https://github.com/talon-one/talon_one.py/",
    keywords=["talon","one","sdk"],
    install_requires=REQUIRES,
    license="MIT",
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
