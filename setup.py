import os
from setuptools import find_packages, setup
# import glob
# with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
# original_dir = os.getcwd()
# os.chdir('julip')
# plugins = glob.glob('plugins/*/*.py')
# plugins.extend(glob.glob('plugins/*/*.yapsy-plugin'))
# plugins.extend(glob.glob('api_utils/*.py'))
# os.chdir(original_dir)
setup(
    name='lablr',
    version='0.1',
#    packages=find_packages(),
    packages=['lablr'],
#    include_package_data=True,
    install_requires=['pillow', 'qrcode'],
    license='BSD License',  # example license
    description='An extensible Yapsy based workflow runner engine',
    # long_description=README,
    url='https://www.example.com/',
    author='Your Name',
    author_email='yourname@example.com',
#     package_data={
#         'julip': ['plugins/google/*', 'plugins/hipchat/*']
#     },
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
