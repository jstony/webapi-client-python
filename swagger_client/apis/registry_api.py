# coding: utf-8

"""
    WebAPI

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/...  As a quick test try reaching the route http:/localhost:8080/api/info (remember that you can only access \"localhost\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md) 

    OpenAPI spec version: <version>
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class RegistryApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_catalog_values(self, class_name, **kwargs):
        """
        List catalog values
        Lists all the catalog values of a specified CatalogType.  > Required permission: registry.one 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_catalog_values(class_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str class_name: The fully qualified class name of the CatalogType to get. (required)
        :return: CatalogTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_catalog_values_with_http_info(class_name, **kwargs)
        else:
            (data) = self.get_catalog_values_with_http_info(class_name, **kwargs)
            return data

    def get_catalog_values_with_http_info(self, class_name, **kwargs):
        """
        List catalog values
        Lists all the catalog values of a specified CatalogType.  > Required permission: registry.one 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_catalog_values_with_http_info(class_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str class_name: The fully qualified class name of the CatalogType to get. (required)
        :return: CatalogTypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['class_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_catalog_values" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'class_name' is set
        if ('class_name' not in params) or (params['class_name'] is None):
            raise ValueError("Missing the required parameter `class_name` when calling `get_catalog_values`")


        collection_formats = {}

        path_params = {}
        if 'class_name' in params:
            path_params['className'] = params['class_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['headerKey', 'queryKey']

        return self.api_client.call_api('/registry/{className}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogTypesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)