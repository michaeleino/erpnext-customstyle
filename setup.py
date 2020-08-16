# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in customstyle/__init__.py
from customstyle import __version__ as version

setup(
	name='customstyle',
	version=version,
	description='for erpnext custom styles',
	author='Michael F',
	author_email='michaeleino@hotmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
