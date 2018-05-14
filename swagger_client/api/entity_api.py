# coding: utf-8

"""
    Web-API

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/v5...  As a quick test try reaching the route http:/localhost:8080/api/v5/info (remember that you can only access \\\"localhost\\\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # List endpoints Lots of objects offer an endpoint to list all objects (e.g. `GET: /world` to get all worlds). These endpoints return only the properties marked 'required' by default, because the list might be quite large. If you want to return ALL data for a list endpoint add the query parameter `details`, (e.g. `GET: /world?details`).  > Remember that in this case the data returned by the endpoint might be quite large.  # Debugging endpoints Apart from the `?details` flag you can also pass some other flags for debugging purposes. Remember that you must include the first query parameter with `?`, and further ones with `&`:  `details`: Includes details for list endpoints  `accept=[json/xml]`: Manually set the accept content type. This is good for browser testing, **BUT DON'T USE THIS IN PRODUCTION, YOU CAN SUPPLY THE `Accepts` HEADER FOR THAT**  `pretty`: Pretty prints the data, also good for debugging in the browser.  An example request might look like this: `http://localhost:8080/api/v5/world?details&accpet=json&pretty&key=MY-API-KEY`  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md)  # noqa: E501

    OpenAPI spec version: @version@
    Contact: inithilian@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EntityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_entity(self, **kwargs):  # noqa: E501
        """Spawn an entity  # noqa: E501

        Creates & Spawns a new entity with the specified properties.     **Required permissions:**    - **entity.create**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_entity(async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateEntityRequest body:
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_entity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_entity_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_entity_with_http_info(self, **kwargs):  # noqa: E501
        """Spawn an entity  # noqa: E501

        Creates & Spawns a new entity with the specified properties.     **Required permissions:**    - **entity.create**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_entity_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateEntityRequest body:
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_entity" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'details' in params:
            query_params.append(('details', params['details']))  # noqa: E501
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/entity', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Entity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def execute_method(self, entity, **kwargs):  # noqa: E501
        """Execute a method  # noqa: E501

        Provides direct access to the underlaying entity object and can execute any method on it.     **Required permissions:**    - **entity.method**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.execute_method(entity, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity: The uuid of the entity (required)
        :param ExecuteMethodRequest body:
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: ExecuteMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.execute_method_with_http_info(entity, **kwargs)  # noqa: E501
        else:
            (data) = self.execute_method_with_http_info(entity, **kwargs)  # noqa: E501
            return data

    def execute_method_with_http_info(self, entity, **kwargs):  # noqa: E501
        """Execute a method  # noqa: E501

        Provides direct access to the underlaying entity object and can execute any method on it.     **Required permissions:**    - **entity.method**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.execute_method_with_http_info(entity, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity: The uuid of the entity (required)
        :param ExecuteMethodRequest body:
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: ExecuteMethodResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity', 'body', 'details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method execute_method" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity' is set
        if ('entity' not in params or
                params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `execute_method`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity' in params:
            path_params['entity'] = params['entity']  # noqa: E501

        query_params = []
        if 'details' in params:
            query_params.append(('details', params['details']))  # noqa: E501
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/entity/{entity}/method', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExecuteMethodResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_entity(self, entity, **kwargs):  # noqa: E501
        """Get entity  # noqa: E501

        Get detailed information about an entity.     **Required permissions:**    - **entity.one**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_entity(entity, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity: The uuid of the entity (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_entity_with_http_info(entity, **kwargs)  # noqa: E501
        else:
            (data) = self.get_entity_with_http_info(entity, **kwargs)  # noqa: E501
            return data

    def get_entity_with_http_info(self, entity, **kwargs):  # noqa: E501
        """Get entity  # noqa: E501

        Get detailed information about an entity.     **Required permissions:**    - **entity.one**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_entity_with_http_info(entity, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity: The uuid of the entity (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity', 'details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_entity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity' is set
        if ('entity' not in params or
                params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `get_entity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity' in params:
            path_params['entity'] = params['entity']  # noqa: E501

        query_params = []
        if 'details' in params:
            query_params.append(('details', params['details']))  # noqa: E501
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/entity/{entity}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Entity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_entities(self, **kwargs):  # noqa: E501
        """List entities  # noqa: E501

        Get a list of all entities on the server (in all worlds).     **Required permissions:**    - **entity.list**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_entities(async=True)
        >>> result = thread.get()

        :param async bool
        :param str world: The world to filter the entities by
        :param str type: The type id of the entities to filter by
        :param str min: The minimum coordinates at which the entity must be, min=x|y|z
        :param str max: The maximum coordinates at which the entity must be, max=x|y|z
        :param int limit: The maximum amount of entities returned
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: list[Entity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_entities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_entities_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_entities_with_http_info(self, **kwargs):  # noqa: E501
        """List entities  # noqa: E501

        Get a list of all entities on the server (in all worlds).     **Required permissions:**    - **entity.list**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_entities_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str world: The world to filter the entities by
        :param str type: The type id of the entities to filter by
        :param str min: The minimum coordinates at which the entity must be, min=x|y|z
        :param str max: The maximum coordinates at which the entity must be, max=x|y|z
        :param int limit: The maximum amount of entities returned
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: list[Entity]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['world', 'type', 'min', 'max', 'limit', 'details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_entities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'world' in params:
            query_params.append(('world', params['world']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'min' in params:
            query_params.append(('min', params['min']))  # noqa: E501
        if 'max' in params:
            query_params.append(('max', params['max']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'details' in params:
            query_params.append(('details', params['details']))  # noqa: E501
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/entity', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Entity]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_entity(self, entity, **kwargs):  # noqa: E501
        """Modify an entity  # noqa: E501

        Modify the properties of an existing entity.     **Required permissions:**    - **entity.modify**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.modify_entity(entity, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity: The uuid of the entity (required)
        :param UpdateEntityRequest body:
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.modify_entity_with_http_info(entity, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_entity_with_http_info(entity, **kwargs)  # noqa: E501
            return data

    def modify_entity_with_http_info(self, entity, **kwargs):  # noqa: E501
        """Modify an entity  # noqa: E501

        Modify the properties of an existing entity.     **Required permissions:**    - **entity.modify**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.modify_entity_with_http_info(entity, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity: The uuid of the entity (required)
        :param UpdateEntityRequest body:
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity', 'body', 'details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_entity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity' is set
        if ('entity' not in params or
                params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `modify_entity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity' in params:
            path_params['entity'] = params['entity']  # noqa: E501

        query_params = []
        if 'details' in params:
            query_params.append(('details', params['details']))  # noqa: E501
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/entity/{entity}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Entity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_entity(self, entity, **kwargs):  # noqa: E501
        """Destroy an entity  # noqa: E501

        Destroys an entity.     **Required permissions:**    - **entity.delete**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_entity(entity, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity: The uuid of the entity (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_entity_with_http_info(entity, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_entity_with_http_info(entity, **kwargs)  # noqa: E501
            return data

    def remove_entity_with_http_info(self, entity, **kwargs):  # noqa: E501
        """Destroy an entity  # noqa: E501

        Destroys an entity.     **Required permissions:**    - **entity.delete**     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_entity_with_http_info(entity, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity: The uuid of the entity (required)
        :param bool details: Add to include additional details, omit or false otherwise
        :param str accept: Override the 'Accept' request header (useful for debugging your requests)
        :param bool pretty: Add to make the Web-API pretty print the response (useful for debugging your requests)
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity', 'details', 'accept', 'pretty']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_entity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity' is set
        if ('entity' not in params or
                params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `remove_entity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity' in params:
            path_params['entity'] = params['entity']  # noqa: E501

        query_params = []
        if 'details' in params:
            query_params.append(('details', params['details']))  # noqa: E501
        if 'accept' in params:
            query_params.append(('accept', params['accept']))  # noqa: E501
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeader', 'ApiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/entity/{entity}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Entity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
