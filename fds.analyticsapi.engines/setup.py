# coding: utf-8

"""
    Engines API

    Allow clients to fetch Engines Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: 2
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "fds.analyticsapi.engines"
VERSION = "3.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Engines API",
    author="Analytics API Support",
    author_email="analytics.api.support@factset.com",
    url="https://github.com/factset/analyticsapi-engines-python-sdk",
    keywords=["OpenAPI", "OpenAPI-Generator", "Engines API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="The Apache Software License, Version 2.0",
    long_description="""\
    Allow clients to fetch Engines Analytics through APIs.  # noqa: E501
    """
)
