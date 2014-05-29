
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup (
    name = 'netropy',
    version = '1.0',
    packages = 'netropy',
    license = open('LICENSE').read(),
    long_description = open('README.md').read(),
)

