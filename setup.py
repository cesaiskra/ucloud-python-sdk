#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from setuptools import setup, find_packages

setup(
    name = 'ucloudclient',
    version = '1.0.1.dev1',
    #packages = ['ucloudclient'],
    # packages = find_packages(),
    package_dir = {'':'ucloudclient'},
    keywords = ('ucloud', 'client'),
    description = 'ucloud python client and command line tools',
    license = 'Apache License Version 2.0',

    url = 'https://github.com/yanheven/ucloud-python-sdk',
    author = 'yanhaifeng(颜海峰)',
    author_email = 'yanheven@gmail.com',

    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)
