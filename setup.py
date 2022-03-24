from setuptools import find_packages, setup

setup(
    name='bustem-plagiarism',
    packages=find_packages(include=['bustem']),
    version='0.1.0',
    author='Vadim Saprykin',
    install_requires=['nltk~=3.7']
)