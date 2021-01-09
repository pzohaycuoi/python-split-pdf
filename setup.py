from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'pythonsplitpdf',
    version = '1.0',
    description = 'split python module',
    author = 'Nguyen Hoang Nam',
    author_email = 'namnguyen270297@outlook.com',
    packages = ['code'],
    install_requires = requirements,
)