__author__ = 'Daniel'

from distutils.core import setup
from setuptools import find_packages

setup(
      name='SolarSystem',
      version='1.0',
      description='SolarSystem Aufgabe',
      author='Daniel Bracher, Martin Suschny',
      package_dir={'':'SolarSystem'},
      packages=find_packages('SolarSystem'),
      package_data = {
            '': ['*.*'],
            'html': ['*.*']
      }
)