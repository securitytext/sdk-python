# -*- coding: utf-8 -*-

"""
    securitytextorgapi.controllers.whois_controller

    This file was automatically generated for SecurityTextOrg by APIMATIC v2.0 ( https://apimatic.io ).
"""

import logging
from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.responses_query_model import ResponsesQueryModel
from ..exceptions.responses_error_exception import ResponsesErrorException

class WhoisController(BaseController):

    """A Controller to access Endpoints in the securitytextorgapi API."""

    def __init__(self, client=None, call_back=None):
        super(WhoisController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create_api_whois_query(self,
                               body):
        """Does a POST request to /query.

        Query the server for a Domain object

        Args:
            body (RequestsQueryModel): Body of API request

        Returns:
            ResponsesQueryModel: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_api_whois_query called.')
    
            # Validate required parameters
            self.logger.info('Validating required parameters for create_api_whois_query.')
            self.validate_parameters(body=body)
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_api_whois_query.')
            _query_builder = Configuration.base_uri
            _query_builder += '/query'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_api_whois_query.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_api_whois_query.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            _context = self.execute_request(_request, name = 'create_api_whois_query')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_api_whois_query.')
            if _context.response.status_code == 404:
                self.logger.info('Status code 404 received for create_api_whois_query. Returning nil.')
                return None
            elif _context.response.status_code == 400:
                raise ResponsesErrorException('Bad Request', _context)
            elif _context.response.status_code == 406:
                raise ResponsesErrorException('Not Acceptable', _context)
            elif _context.response.status_code == 500:
                raise ResponsesErrorException('Internal Server Error', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, ResponsesQueryModel.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
