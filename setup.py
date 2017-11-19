#!/usr/bin/env python3

from setuptools import setup


requires = [
]


setup(
    name='fuocli',
    version='0.0.1a0',
    description='feeluown cli',
    author='Cosven',
    author_email='cosven.yin@gmail.com',
    packages=[
        'fuocli',
        ],
    package_data={
        '': []
        },
    url='https://github.com/cosven/feeluown-cli',
    keywords=['toy'],
    classifiers=(
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        ),
    install_requires=requires,
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'mock',
        'flake8'
    ],
    entry_points={
        'console_scripts': [
            'fuocli=fuocli.__main__:main',
        ]
    },
)
