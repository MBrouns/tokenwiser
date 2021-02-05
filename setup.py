from tokenwiser import __version__
from setuptools import setup, find_packages

base_packages = [
    "jellyfish>=0.8.2",
    "Pyphen>=0.10.0",
    "scikit-learn>=0.24.0",
    "PyYAML>=5.3.1",
    "spacy>=3.0",
    "yake-github>=0.4.0",
    "rich>=9.2.0",
    "mktestdocs>=0.1.0",
]

dev_packages = [
    "flake8>=3.6.0",
    "pytest>=4.0.2",
    "jupyter>=1.0.0",
    "jupyterlab>=0.35.4",
]


setup(
    name="tokenwiser",
    version=__version__,
    packages=find_packages(exclude=["notebooks"]),
    install_requires=base_packages,
    dependency_links=["https://github.com/LIAAD/yake/archive/v0.4.3.tar.gz"],
    extras_require={"dev": dev_packages},
)
