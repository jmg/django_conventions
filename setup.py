#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="django_conventions",
    version="0.1",
    description="Django Convention Over Configuration",
    author="Juan Manuel García",
    author_email = "jmg.utn@gmail.com",
    license = "GPL v3",
    keywords = "Scraping Crawling Framework Python",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "django",
    ],
    url='https://github.com/jmg',
)
