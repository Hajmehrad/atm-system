#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="atm-system",
    version="1.0.0",
    author="Hajmehrad",
    author_email="mehrad.mehrad.mehrad1487@gmail.com",
    description="A simple ATM (Automated Teller Machine) system module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hajmehrad/atm-system",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'atm-system=atm_system.atm:atm_system',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
