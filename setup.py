# This file wont work propery because django 1.3 is still in development, and
# is not in the Python package index. Install django 1.3 into your
# environment prior to using this file.

import os
import sys

from setuptools import setup, find_packages

project_directory = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(project_directory, 'README.md')).read()
CHANGES = open(os.path.join(project_directory, 'CHANGES.txt')).read()

dependancies = [
    'docutils',
    'markdown',
    'textile',
]

setup(name='monokro.me',
      version='0.0',
      description='The code used for http://monokro.me/',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
      ],
      author='Brandon R. Stoner',
      author_email='monokrome@limpidtech.com',
      url='http://monokro.me/',
      keywords='web django monokro.me',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=dependancies,
      tests_require=dependancies,
      tests_suite='monokro.me',
)

