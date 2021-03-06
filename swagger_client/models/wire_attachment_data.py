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

from swagger_client.models.catalog_type import CatalogType  # noqa: F401,E501


class WireAttachmentData(object):
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
        'east': 'CatalogType',
        'north': 'CatalogType',
        'south': 'CatalogType',
        'west': 'CatalogType'
    }

    attribute_map = {
        'east': 'east',
        'north': 'north',
        'south': 'south',
        'west': 'west'
    }

    def __init__(self, east=None, north=None, south=None, west=None):  # noqa: E501
        """WireAttachmentData - a model defined in Swagger"""  # noqa: E501

        self._east = None
        self._north = None
        self._south = None
        self._west = None
        self.discriminator = None

        self.east = east
        self.north = north
        self.south = south
        self.west = west

    @property
    def east(self):
        """Gets the east of this WireAttachmentData.  # noqa: E501

        The type of wire attachment to the east of this entity  # noqa: E501

        :return: The east of this WireAttachmentData.  # noqa: E501
        :rtype: CatalogType
        """
        return self._east

    @east.setter
    def east(self, east):
        """Sets the east of this WireAttachmentData.

        The type of wire attachment to the east of this entity  # noqa: E501

        :param east: The east of this WireAttachmentData.  # noqa: E501
        :type: CatalogType
        """
        if east is None:
            raise ValueError("Invalid value for `east`, must not be `None`")  # noqa: E501

        self._east = east

    @property
    def north(self):
        """Gets the north of this WireAttachmentData.  # noqa: E501

        The type of wire attachment to the north of this entity  # noqa: E501

        :return: The north of this WireAttachmentData.  # noqa: E501
        :rtype: CatalogType
        """
        return self._north

    @north.setter
    def north(self, north):
        """Sets the north of this WireAttachmentData.

        The type of wire attachment to the north of this entity  # noqa: E501

        :param north: The north of this WireAttachmentData.  # noqa: E501
        :type: CatalogType
        """
        if north is None:
            raise ValueError("Invalid value for `north`, must not be `None`")  # noqa: E501

        self._north = north

    @property
    def south(self):
        """Gets the south of this WireAttachmentData.  # noqa: E501

        The type of wire attachment to the south of this entity  # noqa: E501

        :return: The south of this WireAttachmentData.  # noqa: E501
        :rtype: CatalogType
        """
        return self._south

    @south.setter
    def south(self, south):
        """Sets the south of this WireAttachmentData.

        The type of wire attachment to the south of this entity  # noqa: E501

        :param south: The south of this WireAttachmentData.  # noqa: E501
        :type: CatalogType
        """
        if south is None:
            raise ValueError("Invalid value for `south`, must not be `None`")  # noqa: E501

        self._south = south

    @property
    def west(self):
        """Gets the west of this WireAttachmentData.  # noqa: E501

        The type of wire attachment to the west of this entity  # noqa: E501

        :return: The west of this WireAttachmentData.  # noqa: E501
        :rtype: CatalogType
        """
        return self._west

    @west.setter
    def west(self, west):
        """Sets the west of this WireAttachmentData.

        The type of wire attachment to the west of this entity  # noqa: E501

        :param west: The west of this WireAttachmentData.  # noqa: E501
        :type: CatalogType
        """
        if west is None:
            raise ValueError("Invalid value for `west`, must not be `None`")  # noqa: E501

        self._west = west

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
        if not isinstance(other, WireAttachmentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
