# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import clients._generated.petstore
from clients._generated.petstore.model.tag import Tag
from clients._generated.petstore import configuration


class TestTag(unittest.TestCase):
    """Tag unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
