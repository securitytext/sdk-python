# -*- coding: utf-8 -*-

"""
    securitytextorgapi.models.responses_query_model

    This file was automatically generated for SecurityTextOrg by APIMATIC v2.0 ( https://apimatic.io )
"""


class ResponsesQueryModel(object):

    """Implementation of the 'Responses\Query' model.

    Query response

    Attributes:
        found (bool): Query matched exactly one Domain object
        status (int): Status of matched Domain object (if any)
        output (string): Text output of Query

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "found" : "found",
        "status" : "status",
        "output" : "output"
    }

    def __init__(self,
                 found=None,
                 status=None,
                 output=None,
                 additional_properties = {}):
        """Constructor for the ResponsesQueryModel class"""

        # Initialize members of the class
        self.found = found
        self.status = status
        self.output = output

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
        found = dictionary.get("found")
        status = dictionary.get("status")
        output = dictionary.get("output")

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(found,
                   status,
                   output,
                   dictionary)


