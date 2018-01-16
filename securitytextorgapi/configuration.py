# -*- coding: utf-8 -*-

"""
   securitytextorgapi.configuration

   This file was automatically generated for SecurityTextOrg by APIMATIC v2.0 ( https://apimatic.io )
"""
import sys
import logging

from .api_helper import APIHelper

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # The base Uri for API calls
    base_uri = 'https://api.securitytext.org/v1'

