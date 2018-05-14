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

from swagger_client.models.block_state import BlockState  # noqa: F401,E501


class FallingBlockData(object):
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
        'state': 'BlockState',
        'can_drop_as_item': 'bool',
        'can_hurt_entities': 'bool',
        'can_place_as_block': 'bool',
        'fall_damage_per_block': 'float',
        'fall_time': 'int',
        'max_fall_damage': 'float'
    }

    attribute_map = {
        'state': 'state',
        'can_drop_as_item': 'canDropAsItem',
        'can_hurt_entities': 'canHurtEntities',
        'can_place_as_block': 'canPlaceAsBlock',
        'fall_damage_per_block': 'fallDamagePerBlock',
        'fall_time': 'fallTime',
        'max_fall_damage': 'maxFallDamage'
    }

    def __init__(self, state=None, can_drop_as_item=None, can_hurt_entities=None, can_place_as_block=None, fall_damage_per_block=None, fall_time=None, max_fall_damage=None):  # noqa: E501
        """FallingBlockData - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._can_drop_as_item = None
        self._can_hurt_entities = None
        self._can_place_as_block = None
        self._fall_damage_per_block = None
        self._fall_time = None
        self._max_fall_damage = None
        self.discriminator = None

        self.state = state
        self.can_drop_as_item = can_drop_as_item
        self.can_hurt_entities = can_hurt_entities
        self.can_place_as_block = can_place_as_block
        self.fall_damage_per_block = fall_damage_per_block
        self.fall_time = fall_time
        self.max_fall_damage = max_fall_damage

    @property
    def state(self):
        """Gets the state of this FallingBlockData.  # noqa: E501

        The state of the falling block  # noqa: E501

        :return: The state of this FallingBlockData.  # noqa: E501
        :rtype: BlockState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FallingBlockData.

        The state of the falling block  # noqa: E501

        :param state: The state of this FallingBlockData.  # noqa: E501
        :type: BlockState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def can_drop_as_item(self):
        """Gets the can_drop_as_item of this FallingBlockData.  # noqa: E501

        True if the block can drop as an item, false otherwise  # noqa: E501

        :return: The can_drop_as_item of this FallingBlockData.  # noqa: E501
        :rtype: bool
        """
        return self._can_drop_as_item

    @can_drop_as_item.setter
    def can_drop_as_item(self, can_drop_as_item):
        """Sets the can_drop_as_item of this FallingBlockData.

        True if the block can drop as an item, false otherwise  # noqa: E501

        :param can_drop_as_item: The can_drop_as_item of this FallingBlockData.  # noqa: E501
        :type: bool
        """
        if can_drop_as_item is None:
            raise ValueError("Invalid value for `can_drop_as_item`, must not be `None`")  # noqa: E501

        self._can_drop_as_item = can_drop_as_item

    @property
    def can_hurt_entities(self):
        """Gets the can_hurt_entities of this FallingBlockData.  # noqa: E501

        True if the block can hurt entities, false otherwise  # noqa: E501

        :return: The can_hurt_entities of this FallingBlockData.  # noqa: E501
        :rtype: bool
        """
        return self._can_hurt_entities

    @can_hurt_entities.setter
    def can_hurt_entities(self, can_hurt_entities):
        """Sets the can_hurt_entities of this FallingBlockData.

        True if the block can hurt entities, false otherwise  # noqa: E501

        :param can_hurt_entities: The can_hurt_entities of this FallingBlockData.  # noqa: E501
        :type: bool
        """
        if can_hurt_entities is None:
            raise ValueError("Invalid value for `can_hurt_entities`, must not be `None`")  # noqa: E501

        self._can_hurt_entities = can_hurt_entities

    @property
    def can_place_as_block(self):
        """Gets the can_place_as_block of this FallingBlockData.  # noqa: E501

        True if this falling block can be placed as a normal block, false otherwise  # noqa: E501

        :return: The can_place_as_block of this FallingBlockData.  # noqa: E501
        :rtype: bool
        """
        return self._can_place_as_block

    @can_place_as_block.setter
    def can_place_as_block(self, can_place_as_block):
        """Sets the can_place_as_block of this FallingBlockData.

        True if this falling block can be placed as a normal block, false otherwise  # noqa: E501

        :param can_place_as_block: The can_place_as_block of this FallingBlockData.  # noqa: E501
        :type: bool
        """
        if can_place_as_block is None:
            raise ValueError("Invalid value for `can_place_as_block`, must not be `None`")  # noqa: E501

        self._can_place_as_block = can_place_as_block

    @property
    def fall_damage_per_block(self):
        """Gets the fall_damage_per_block of this FallingBlockData.  # noqa: E501

        The amount of damage per block this falling block deals  # noqa: E501

        :return: The fall_damage_per_block of this FallingBlockData.  # noqa: E501
        :rtype: float
        """
        return self._fall_damage_per_block

    @fall_damage_per_block.setter
    def fall_damage_per_block(self, fall_damage_per_block):
        """Sets the fall_damage_per_block of this FallingBlockData.

        The amount of damage per block this falling block deals  # noqa: E501

        :param fall_damage_per_block: The fall_damage_per_block of this FallingBlockData.  # noqa: E501
        :type: float
        """
        if fall_damage_per_block is None:
            raise ValueError("Invalid value for `fall_damage_per_block`, must not be `None`")  # noqa: E501

        self._fall_damage_per_block = fall_damage_per_block

    @property
    def fall_time(self):
        """Gets the fall_time of this FallingBlockData.  # noqa: E501

        The amount of time (in ticks) this block has been falling for  # noqa: E501

        :return: The fall_time of this FallingBlockData.  # noqa: E501
        :rtype: int
        """
        return self._fall_time

    @fall_time.setter
    def fall_time(self, fall_time):
        """Sets the fall_time of this FallingBlockData.

        The amount of time (in ticks) this block has been falling for  # noqa: E501

        :param fall_time: The fall_time of this FallingBlockData.  # noqa: E501
        :type: int
        """
        if fall_time is None:
            raise ValueError("Invalid value for `fall_time`, must not be `None`")  # noqa: E501

        self._fall_time = fall_time

    @property
    def max_fall_damage(self):
        """Gets the max_fall_damage of this FallingBlockData.  # noqa: E501

        The maximum amount of damage this block can deal  # noqa: E501

        :return: The max_fall_damage of this FallingBlockData.  # noqa: E501
        :rtype: float
        """
        return self._max_fall_damage

    @max_fall_damage.setter
    def max_fall_damage(self, max_fall_damage):
        """Sets the max_fall_damage of this FallingBlockData.

        The maximum amount of damage this block can deal  # noqa: E501

        :param max_fall_damage: The max_fall_damage of this FallingBlockData.  # noqa: E501
        :type: float
        """
        if max_fall_damage is None:
            raise ValueError("Invalid value for `max_fall_damage`, must not be `None`")  # noqa: E501

        self._max_fall_damage = max_fall_damage

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
        if not isinstance(other, FallingBlockData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other