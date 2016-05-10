import os
from setuptools import find_packages, setup
setup(
    name='lablr',
    version='0.1',
    packages=['lablr'],
    install_requires=['pillow', 'qrcode'],
    license='BSD License',  # example license
    description='An extensible Yapsy based workflow runner engine',
    url='https://github.com/lablr',
    author='Kyle Crawshaw',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
