# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from talon_one.models.export import Export  # noqa: F401,E501


class InlineResponse20026(object):
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
        'total_result_size': 'int',
        'data': 'list[Export]'
    }

    attribute_map = {
        'total_result_size': 'totalResultSize',
        'data': 'data'
    }

    def __init__(self, total_result_size=None, data=None):  # noqa: E501
        """InlineResponse20026 - a model defined in Swagger"""  # noqa: E501

        self._total_result_size = None
        self._data = None
        self.discriminator = None

        self.total_result_size = total_result_size
        self.data = data

    @property
    def total_result_size(self):
        """Gets the total_result_size of this InlineResponse20026.  # noqa: E501


        :return: The total_result_size of this InlineResponse20026.  # noqa: E501
        :rtype: int
        """
        return self._total_result_size

    @total_result_size.setter
    def total_result_size(self, total_result_size):
        """Sets the total_result_size of this InlineResponse20026.


        :param total_result_size: The total_result_size of this InlineResponse20026.  # noqa: E501
        :type: int
        """
        if total_result_size is None:
            raise ValueError("Invalid value for `total_result_size`, must not be `None`")  # noqa: E501

        self._total_result_size = total_result_size

    @property
    def data(self):
        """Gets the data of this InlineResponse20026.  # noqa: E501


        :return: The data of this InlineResponse20026.  # noqa: E501
        :rtype: list[Export]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse20026.


        :param data: The data of this InlineResponse20026.  # noqa: E501
        :type: list[Export]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(InlineResponse20026, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20026):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
