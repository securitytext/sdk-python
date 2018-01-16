# -*- coding: utf-8 -*-

"""
    securitytextorgapi.models.requests_query_model

    This file was automatically generated for SecurityTextOrg by APIMATIC v2.0 ( https://apimatic.io )
"""


class RequestsQueryModel(object):

    """Implementation of the 'Requests\Query' model.

    Query request

    Attributes:
        domain (string): Name of Domain to query

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "domain" : "domain"
    }

    def __init__(self,
                 domain=None,
                 additional_properties = {}):
        """Constructor for the RequestsQueryModel class"""

        # Initialize members of the class
        self.domain = domain

        # Add additional model properties to the instance
        self.additional_properties = additional_properties


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        domain = dictionary.get("domain")

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(domain,
                   dictionary)


