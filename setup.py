from __future__ import print_function

import os.path as osp
from setuptools import find_packages
from setuptools import setup


version = "0.0.1"


def listup_package_data():
    data_files = []
    for root, _, files in os.walk('shapent_utils/data'):
        for filename in files:
            data_files.append(
                osp.join(
                    root[len('shapent_utils/'):],
                    filename))
    return data_files


setup_requires = []
install_requires = ['trimesh']

setup(
    name="shapenet_utils",
    version=version,
    description="shapenet_utils",
    author="kosuke55",
    author_email="kosuke.tnp@gmail.com",
    url="https://github.com/kosuke55/shapenet_utils",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    packages=find_packages(),
    install_requires=install_requires,
)
