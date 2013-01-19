#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="django_conventions",
    version="0.1.1",
    description="Django Convention Over Configuration",
    author="Juan Manuel García",
    author_email = "jmg.utn@gmail.com",
    license = "GPL v3",
    keywords = "Django Routing Convetion Over Configuration",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "django",
    ],
    url='https://github.com/jmg/django_conventions',
)
