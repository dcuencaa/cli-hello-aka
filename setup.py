from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name='akamaicliexample', 
    version='0.1.0', 
    description='Example command for Akamai CLI in Python'
    author='Kirsten Hunter',
    author_email='khunter@akamai.com',
    url='https://github.com/akamai/cli-example-python',
    packages=find_packages(),
    license='MIT'
)
