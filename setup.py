#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

classifiers = [line.strip() for line in """
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: DFSG approved
License :: OSI Approved
License :: OSI Approved :: MIT License
Topic :: Internet :: Name Service (DNS)
Topic :: Software Development :: Libraries :: Python Modules
Environment :: Console
Natural Language :: English
Operating System :: MacOS :: MacOS X
Operating System :: POSIX :: Linux
Operating System :: POSIX :: BSD :: FreeBSD
Programming Language :: Python
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
""".splitlines() if len(line) > 0]

install_requires = ["IPy>=0.56"]
if sys.version_info >= (3, 0):
    install_requires.append("netifaces-py3==0.8")
else:
    install_requires.append("netifaces>=0.4")

setup(name="dyndnsc",
      packages=["dyndnsc"],
      version="0.3",
      author="Paul Kremer",
      author_email="@".join(("paul", "spurious.biz")),  # avoid spam,
      license="MIT License",
      description="dynamic dns update client module that tries to be extensible, re-usable and efficient on network resources",
      long_description="https://github.com/infothrill/python-dyndnsc",
      url="https://github.com/infothrill/python-dyndnsc",
      install_requires=install_requires,
      entry_points=("""
                      [console_scripts]
                      dyndnsc=dyndnsc.cli:main
                      """),
      classifiers=classifiers,
      test_suite='dyndnsc.tests',
      tests_require=['bottle==0.11.6'],
      )
