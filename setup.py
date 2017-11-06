#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.1.2'


def read(fname):
    return codecs.open(
        os.path.join(os.path.dirname(__file__), fname), 'r', 'utf-8').read()


readme = read('README.rst')
history = read('HISTORY.rst').replace('.. :changelog:', '')

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    os.system("git tag -a %s -m 'version %s'" % (__version__, __version__))
    os.system("git push --tags")
    sys.exit()

setup(
    name='instance-config',
    version=__version__,
    description='A simple library using consul locks to do one-time configuration tasks on AWS instances.',
    long_description=readme + '\n\n' + history,
    author='Mark Lipscombe',
    author_email='mark@lipscombe.com',
    url='https://github.com/mlipscombe/instance-config',
    packages=['instance_config'],
    include_package_data=True,
    license="BSD",
    zip_safe=True,
    keywords='instance-config',
    install_requires=['boto3', 'credstash', 'python-consul', 'cached_property', 'consul_lock'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
