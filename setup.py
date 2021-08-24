#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: bright
# Mail: brightmail@vip.qq.com
# Created Time:  2023-08-24 16:25:34
#############################################


from setuptools import setup, find_packages

setup(
    name="bright",
    version="0.0.12",
    keywords=["tool", "bright"],
    description="bright tool",
    long_description="bright tool etc",
    license="MIT Licence",

    url="https://github.com/brightlike/Christmastree/",
    author="bright",
    author_email="brightmail@vip.qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['chardet', 'requests']
)
