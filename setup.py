# -*- coding: utf-8 -*-
"""Convert Python objects to jcamp"""

from setuptools import find_packages, setup

import versioneer

with open("requirements.txt", "r") as fh:
    REQUIREMENTS = [line.strip() for line in fh]

setup(
    name="pytocjcamp",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    url="",
    license="MIT",
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    extras_require={
        "testing": ["pytest", "pytest-cov<2.11"],
        "docs": ["guzzle_sphinx_theme"],
        "pre-commit": [
            "pre-commit",
            "black",
            "prospector",
            "pylint",
            "versioneer",
            "isort",
            "gitchangelog",
        ],
    },
    author="Kevin M. Jablonka",
    author_email="kevin.jablonka@epfl.ch",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 1 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
