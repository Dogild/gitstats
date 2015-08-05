#!/usr/bin/env python

from distutils.core import setup
from os.path import join

setup(name='gitstats',
      version='0.0.2',
      description='Python library to retrieve public contributions from github',
      author='Alexandre Wilhelm',
      author_email='contact.dogild@gmail.com',
      url='https://github.com/Dogild/gitstats',
      packages=['gitstats', 'gitstats.lib', 'gitstats.models'],
      license='MIT',
      install_requires=map(str.strip, open(join('requirements.txt')))
     )