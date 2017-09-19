#!/usr/bin/env python

from setuptools import setup

version = '1.0.3'

required = open('requirements.txt').read().split('\n')

setup(
    name='abi2fastq',
    version=version,
    description='abi2fastq is a small utility to convert Sanger sequencing '
                'reads in .abi (applied biosystems) format to FASTQ Edit',
    author='olgabot',
    author_email='olga.botvinnik@gmail.com',
    url='https://github.com/olgabot/abi2fastq',
    packages=['abi2fastq'],
    install_requires=required,
    long_description='See ' + 'https://github.com/olgabot/abi2fastq',
    license='MIT',
    entry_points={'console_scripts': [
        'abi2fastq = abi2fastq.cli:cli'
    ]},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
