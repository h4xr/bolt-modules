'''
File: setup.py
Description: Make the bolt-modules package installable
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 27/10/2017
'''
import setuptools

setup=(
    name='bolt-modules',
    version='0.0.1',
    packages=find_packages(exclude=['docs', 'test', 'temp'])
)
