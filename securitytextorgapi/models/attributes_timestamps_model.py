# -*- coding: utf-8 -*-

"""
    securitytextorgapi.models.attributes_timestamps_model

    This file was automatically generated for SecurityTextOrg by APIMATIC v2.0 ( https://apimatic.io )
"""
from securitytextorgapi.api_helper import APIHelper

class AttributesTimestampsModel(object):

    """Implementation of the 'Attributes\Timestamps' model.

    Timestamp attributes

    Attributes:
        created_at (datetime): Creation date
        updated_at (datetime): Last updated

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_at" : "created_at",
        "updated_at" : "updated_at"
    }

    def __init__(self,
                 created_at=None,
                 updated_at=None,
                 additional_properties = {}):
        """Constructor for the AttributesTimestampsModel class"""

        # Initialize members of the class
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None

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
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(created_at,
                   updated_at,
                   dictionary)


