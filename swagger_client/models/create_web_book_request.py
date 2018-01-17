# coding: utf-8

"""
    WebAPI

    Access Sponge powered Minecraft servers through a WebAPI  # Introduction This is the documentation of the various API routes offered by the WebAPI plugin.  This documentation assumes that you are familiar with the basic concepts of Web API's, such as `GET`, `PUT`, `POST` and `DELETE` methods, request `HEADERS` and `RESPONSE CODES` and `JSON` data.  By default this documentation can be found at http:/localhost:8080 (while your minecraft server is running) and the various routes start with http:/localhost:8080/api/...  As a quick test try reaching the route http:/localhost:8080/api/info (remember that you can only access \"localhost\" routes on the server on which you are running minecraft). This route should show you basic information about your server, like the motd and player count.  # Additional data Certain endpoints (such as `/player`, `/entity` and `/tile-entity` have additional properties which are not documented here, because the data depends on the concrete object type (eg. `Sheep` have a wool color, others do not) and on the other plugins/mods that are running on your server which might add additional data.  You can also find more information in the github docs (https:/github.com/Valandur/Web-API/tree/master/docs/DATA.md) 

    OpenAPI spec version: <version>
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateWebBookRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'title': 'str',
        'lines': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'lines': 'lines'
    }

    def __init__(self, id=None, title=None, lines=None):
        """
        CreateWebBookRequest - a model defined in Swagger
        """

        self._id = None
        self._title = None
        self._lines = None

        if id is not None:
          self.id = id
        if title is not None:
          self.title = title
        if lines is not None:
          self.lines = lines

    @property
    def id(self):
        """
        Gets the id of this CreateWebBookRequest.
        The unique id of the web book.

        :return: The id of this CreateWebBookRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CreateWebBookRequest.
        The unique id of the web book.

        :param id: The id of this CreateWebBookRequest.
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this CreateWebBookRequest.
        The title of the web book.

        :return: The title of this CreateWebBookRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CreateWebBookRequest.
        The title of the web book.

        :param title: The title of this CreateWebBookRequest.
        :type: str
        """

        self._title = title

    @property
    def lines(self):
        """
        Gets the lines of this CreateWebBookRequest.
        The lines that make up the content of the book.

        :return: The lines of this CreateWebBookRequest.
        :rtype: list[str]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this CreateWebBookRequest.
        The lines that make up the content of the book.

        :param lines: The lines of this CreateWebBookRequest.
        :type: list[str]
        """

        self._lines = lines

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CreateWebBookRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
