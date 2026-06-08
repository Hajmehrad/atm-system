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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
)