# -*- coding: utf-8 -*-

"""
    securitytextorgapi.models.attributes_uuid_model

    This file was automatically generated for SecurityTextOrg by APIMATIC v2.0 ( https://apimatic.io )
"""


class AttributesUuidModel(object):

    """Implementation of the 'Attributes\Uuid' model.

    UUID attributes

    Attributes:
        value (string): Value of UUID

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value" : "value"
    }

    def __init__(self,
                 value=None,
                 additional_properties = {}):
        """Constructor for the AttributesUuidModel class"""

        # Initialize members of the class
        self.value = value

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
        value = dictionary.get("value")

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(value,
                   dictionary)


