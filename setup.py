import os
from setuptools import find_packages, setup
setup(
    name='lablr',
    version='0.1',
    packages=['lablr'],
    install_requires=['pillow', 'qrcode'],
    license='MIT License',  # example license
    description='Used to generate images and labels easily.',
    url='https://github.com/lablr',
    author='Kyle Crawshaw',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
