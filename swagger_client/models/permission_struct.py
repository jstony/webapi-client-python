# coding: utf-8

"""
    Web-API

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/v5...  As a quick test try reaching the route http:/localhost:8080/api/v5/info (remember that you can only access \\\"localhost\\\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # List endpoints Lots of objects offer an endpoint to list all objects (e.g. `GET: /world` to get all worlds). These endpoints return only the properties marked 'required' by default, because the list might be quite large. If you want to return ALL data for a list endpoint add the query parameter `details`, (e.g. `GET: /world?details`).  > Remember that in this case the data returned by the endpoint might be quite large.  # Debugging endpoints Apart from the `?details` flag you can also pass some other flags for debugging purposes. Remember that you must include the first query parameter with `?`, and further ones with `&`:  `details`: Includes details for list endpoints  `accept=[json/xml]`: Manually set the accept content type. This is good for browser testing, **BUT DON'T USE THIS IN PRODUCTION, YOU CAN SUPPLY THE `Accepts` HEADER FOR THAT**  `pretty`: Pretty prints the data, also good for debugging in the browser.  An example request might look like this: `http://localhost:8080/api/v5/world?details&accpet=json&pretty&key=MY-API-KEY`  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md)  # noqa: E501

    OpenAPI spec version: @version@
    Contact: inithilian@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PermissionStruct(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key': 'str',
        'name': 'str',
        'permissions': 'object',
        'rate_limit': 'int'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'permissions': 'permissions',
        'rate_limit': 'rateLimit'
    }

    def __init__(self, key=None, name=None, permissions=None, rate_limit=None):  # noqa: E501
        """PermissionStruct - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._name = None
        self._permissions = None
        self._rate_limit = None
        self.discriminator = None

        self.key = key
        self.name = name
        self.permissions = permissions
        self.rate_limit = rate_limit

    @property
    def key(self):
        """Gets the key of this PermissionStruct.  # noqa: E501

        The key used authorize with the Web-API  # noqa: E501

        :return: The key of this PermissionStruct.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PermissionStruct.

        The key used authorize with the Web-API  # noqa: E501

        :param key: The key of this PermissionStruct.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this PermissionStruct.  # noqa: E501

        The human readable name of this permssions struct. Only useful for users.  # noqa: E501

        :return: The name of this PermissionStruct.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PermissionStruct.

        The human readable name of this permssions struct. Only useful for users.  # noqa: E501

        :param name: The name of this PermissionStruct.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this PermissionStruct.  # noqa: E501

        The permissions tree that this key grants access to  # noqa: E501

        :return: The permissions of this PermissionStruct.  # noqa: E501
        :rtype: object
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this PermissionStruct.

        The permissions tree that this key grants access to  # noqa: E501

        :param permissions: The permissions of this PermissionStruct.  # noqa: E501
        :type: object
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def rate_limit(self):
        """Gets the rate_limit of this PermissionStruct.  # noqa: E501

        The rate limit in requests per second that this key permits (0 = unlimited)  # noqa: E501

        :return: The rate_limit of this PermissionStruct.  # noqa: E501
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """Sets the rate_limit of this PermissionStruct.

        The rate limit in requests per second that this key permits (0 = unlimited)  # noqa: E501

        :param rate_limit: The rate_limit of this PermissionStruct.  # noqa: E501
        :type: int
        """
        if rate_limit is None:
            raise ValueError("Invalid value for `rate_limit`, must not be `None`")  # noqa: E501

        self._rate_limit = rate_limit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PermissionStruct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
