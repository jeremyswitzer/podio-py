from setuptools import setup, find_packages
'''The setup and build script for the pypodio library.'''

__author__ = 'jeremy.switzer@gmail.com'
__version__ = '0.1dev'

setup(
  name = "pypodio2",
  version = __version__,
  author='Jeremy Switzer',
  author_email='jeremy.switzer@gmail.com',
  description='A Python wrapper around the Podio API',
  license='MIT',
  url='https://github.com/jeremyswitzer/podio-py.git',
  keywords='podio',
  packages= find_packages(),
  install_requires = ['httplib2'],
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Communications',
    'Topic :: Internet',
  ],
)