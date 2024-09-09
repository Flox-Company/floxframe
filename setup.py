# setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='floxframe',
    version='1.0',
    packages=find_packages(),
    description='A python package that helps with GUIs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Florian Ratgers',
    author_email='flox@ratgers.nl',
    url='https://sites.google.com/ratgers.nl/flox-company/packages/floxframe',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
