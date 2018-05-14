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

from swagger_client.models.location import Location  # noqa: F401,E501
from swagger_client.models.player import Player  # noqa: F401,E501
from swagger_client.models.vector3d import Vector3d  # noqa: F401,E501
from swagger_client.models.world import World  # noqa: F401,E501


class RedProtectRegion(object):
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
        'id': 'str',
        'link': 'str',
        'max': 'Vector3d',
        'min': 'Vector3d',
        'name': 'str',
        'world': 'World',
        'admins': 'list[Player]',
        'can_delete': 'bool',
        'date': 'str',
        'flags': 'dict(str, object)',
        'leaders': 'list[Player]',
        'members': 'list[Player]',
        'priority': 'int',
        'tp_point': 'Location',
        'welcome_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'link': 'link',
        'max': 'max',
        'min': 'min',
        'name': 'name',
        'world': 'world',
        'admins': 'admins',
        'can_delete': 'canDelete',
        'date': 'date',
        'flags': 'flags',
        'leaders': 'leaders',
        'members': 'members',
        'priority': 'priority',
        'tp_point': 'tpPoint',
        'welcome_message': 'welcomeMessage'
    }

    def __init__(self, id=None, link=None, max=None, min=None, name=None, world=None, admins=None, can_delete=None, date=None, flags=None, leaders=None, members=None, priority=None, tp_point=None, welcome_message=None):  # noqa: E501
        """RedProtectRegion - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._link = None
        self._max = None
        self._min = None
        self._name = None
        self._world = None
        self._admins = None
        self._can_delete = None
        self._date = None
        self._flags = None
        self._leaders = None
        self._members = None
        self._priority = None
        self._tp_point = None
        self._welcome_message = None
        self.discriminator = None

        self.id = id
        self.link = link
        self.max = max
        self.min = min
        self.name = name
        self.world = world
        if admins is not None:
            self.admins = admins
        if can_delete is not None:
            self.can_delete = can_delete
        if date is not None:
            self.date = date
        if flags is not None:
            self.flags = flags
        if leaders is not None:
            self.leaders = leaders
        if members is not None:
            self.members = members
        if priority is not None:
            self.priority = priority
        if tp_point is not None:
            self.tp_point = tp_point
        if welcome_message is not None:
            self.welcome_message = welcome_message

    @property
    def id(self):
        """Gets the id of this RedProtectRegion.  # noqa: E501

        The unique id of this region  # noqa: E501

        :return: The id of this RedProtectRegion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RedProtectRegion.

        The unique id of this region  # noqa: E501

        :param id: The id of this RedProtectRegion.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def link(self):
        """Gets the link of this RedProtectRegion.  # noqa: E501

        The API link that can be used to obtain more information about this object  # noqa: E501

        :return: The link of this RedProtectRegion.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this RedProtectRegion.

        The API link that can be used to obtain more information about this object  # noqa: E501

        :param link: The link of this RedProtectRegion.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def max(self):
        """Gets the max of this RedProtectRegion.  # noqa: E501

        The maximum coordinates that define the region  # noqa: E501

        :return: The max of this RedProtectRegion.  # noqa: E501
        :rtype: Vector3d
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this RedProtectRegion.

        The maximum coordinates that define the region  # noqa: E501

        :param max: The max of this RedProtectRegion.  # noqa: E501
        :type: Vector3d
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def min(self):
        """Gets the min of this RedProtectRegion.  # noqa: E501

        The minimum coordinates that define the region  # noqa: E501

        :return: The min of this RedProtectRegion.  # noqa: E501
        :rtype: Vector3d
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this RedProtectRegion.

        The minimum coordinates that define the region  # noqa: E501

        :param min: The min of this RedProtectRegion.  # noqa: E501
        :type: Vector3d
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def name(self):
        """Gets the name of this RedProtectRegion.  # noqa: E501

        The name of this region  # noqa: E501

        :return: The name of this RedProtectRegion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RedProtectRegion.

        The name of this region  # noqa: E501

        :param name: The name of this RedProtectRegion.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def world(self):
        """Gets the world of this RedProtectRegion.  # noqa: E501

        The world this region is located in  # noqa: E501

        :return: The world of this RedProtectRegion.  # noqa: E501
        :rtype: World
        """
        return self._world

    @world.setter
    def world(self, world):
        """Sets the world of this RedProtectRegion.

        The world this region is located in  # noqa: E501

        :param world: The world of this RedProtectRegion.  # noqa: E501
        :type: World
        """
        if world is None:
            raise ValueError("Invalid value for `world`, must not be `None`")  # noqa: E501

        self._world = world

    @property
    def admins(self):
        """Gets the admins of this RedProtectRegion.  # noqa: E501

        A list of players that are admins of this region  # noqa: E501

        :return: The admins of this RedProtectRegion.  # noqa: E501
        :rtype: list[Player]
        """
        return self._admins

    @admins.setter
    def admins(self, admins):
        """Sets the admins of this RedProtectRegion.

        A list of players that are admins of this region  # noqa: E501

        :param admins: The admins of this RedProtectRegion.  # noqa: E501
        :type: list[Player]
        """

        self._admins = admins

    @property
    def can_delete(self):
        """Gets the can_delete of this RedProtectRegion.  # noqa: E501

        True if this region can be deleted, false otherwise  # noqa: E501

        :return: The can_delete of this RedProtectRegion.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this RedProtectRegion.

        True if this region can be deleted, false otherwise  # noqa: E501

        :param can_delete: The can_delete of this RedProtectRegion.  # noqa: E501
        :type: bool
        """

        self._can_delete = can_delete

    @property
    def date(self):
        """Gets the date of this RedProtectRegion.  # noqa: E501

        The date this region was created?  # noqa: E501

        :return: The date of this RedProtectRegion.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this RedProtectRegion.

        The date this region was created?  # noqa: E501

        :param date: The date of this RedProtectRegion.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def flags(self):
        """Gets the flags of this RedProtectRegion.  # noqa: E501

        A map of flags applicable to this region  # noqa: E501

        :return: The flags of this RedProtectRegion.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this RedProtectRegion.

        A map of flags applicable to this region  # noqa: E501

        :param flags: The flags of this RedProtectRegion.  # noqa: E501
        :type: dict(str, object)
        """

        self._flags = flags

    @property
    def leaders(self):
        """Gets the leaders of this RedProtectRegion.  # noqa: E501

        A list of players that are leaders of this region  # noqa: E501

        :return: The leaders of this RedProtectRegion.  # noqa: E501
        :rtype: list[Player]
        """
        return self._leaders

    @leaders.setter
    def leaders(self, leaders):
        """Sets the leaders of this RedProtectRegion.

        A list of players that are leaders of this region  # noqa: E501

        :param leaders: The leaders of this RedProtectRegion.  # noqa: E501
        :type: list[Player]
        """

        self._leaders = leaders

    @property
    def members(self):
        """Gets the members of this RedProtectRegion.  # noqa: E501

        A list of players that are members of this region  # noqa: E501

        :return: The members of this RedProtectRegion.  # noqa: E501
        :rtype: list[Player]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this RedProtectRegion.

        A list of players that are members of this region  # noqa: E501

        :param members: The members of this RedProtectRegion.  # noqa: E501
        :type: list[Player]
        """

        self._members = members

    @property
    def priority(self):
        """Gets the priority of this RedProtectRegion.  # noqa: E501

        The priority of this region compared to other regions  # noqa: E501

        :return: The priority of this RedProtectRegion.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this RedProtectRegion.

        The priority of this region compared to other regions  # noqa: E501

        :param priority: The priority of this RedProtectRegion.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def tp_point(self):
        """Gets the tp_point of this RedProtectRegion.  # noqa: E501

        The teleport point for this region  # noqa: E501

        :return: The tp_point of this RedProtectRegion.  # noqa: E501
        :rtype: Location
        """
        return self._tp_point

    @tp_point.setter
    def tp_point(self, tp_point):
        """Sets the tp_point of this RedProtectRegion.

        The teleport point for this region  # noqa: E501

        :param tp_point: The tp_point of this RedProtectRegion.  # noqa: E501
        :type: Location
        """

        self._tp_point = tp_point

    @property
    def welcome_message(self):
        """Gets the welcome_message of this RedProtectRegion.  # noqa: E501

        The welcome message displayed to a player when they enter this region  # noqa: E501

        :return: The welcome_message of this RedProtectRegion.  # noqa: E501
        :rtype: str
        """
        return self._welcome_message

    @welcome_message.setter
    def welcome_message(self, welcome_message):
        """Sets the welcome_message of this RedProtectRegion.

        The welcome message displayed to a player when they enter this region  # noqa: E501

        :param welcome_message: The welcome_message of this RedProtectRegion.  # noqa: E501
        :type: str
        """

        self._welcome_message = welcome_message

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
        if not isinstance(other, RedProtectRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
