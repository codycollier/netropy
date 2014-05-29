
from distutils.core import setup

setup (
    name = 'netropy',
    version = '1.0',
    packages = ['netropy', ],
    description = 'Netropy is a python interface to the NIST Randomness Beacon',
    long_description = open('README.md').read(),

    license = 'The MIT License (MIT)',
    author = 'Cody Collier',
    author_email = 'cody@telnet.org',
    url = 'https://github.com/codycollier/netropy',
)

