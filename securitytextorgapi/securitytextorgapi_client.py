# -*- coding: utf-8 -*-

"""
    securitytextorgapi.securitytext_org_api_client

    This file was automatically generated for SecurityTextOrg by APIMATIC v2.0 ( https://apimatic.io ).
"""
from .decorators import lazy_property
from .configuration import Configuration
from .controllers.whois_controller import WhoisController

class SecuritytextorgapiClient(object):

    config = Configuration

    @lazy_property
    def whois(self):
        return WhoisController()



