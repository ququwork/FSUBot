from distutils.core import setup, find_packages
from setuptools.command.test import test as TestCommand

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('VERSION.rst', 'r', 'utf-8') as f:
    version = f.read().strip()


setup(
    name='fsubot',
    version=version,
    description='Base bot for developing FSU bots.',
    long_description=readme,
    author='Sean Pianka',
    author_email='pianka@eml.cc',
    url = 'https://github.com/seanpianka/fsubot',
    download_url = 'https://github.com/seanpianka/FSUBot/tarball/{}'.format(version),
    packages=find_packages(exclude=['tests']),
    install_requires=[
        "selenium==3.0.2",
        "lxml==3.7.2",
        "argparse"
    ],
    license='MIT',
    keywords = ['florida', 'state', 'university', 'fsu', 'bot'],
    zip_safe=False,
    include_package_data=True,
    copyright = 'Copyright (c) 2017 Sean Pianka',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Education',
        'Topic :: Utilities'
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ),
)

