# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class InlineResponse2004(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'total_result_size': 'int',
        'data': 'list[Ruleset]'
    }

    attribute_map = {
        'total_result_size': 'totalResultSize',
        'data': 'data'
    }

    def __init__(self, total_result_size=None, data=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2004 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_result_size = None
        self._data = None
        self.discriminator = None

        self.total_result_size = total_result_size
        self.data = data

    @property
    def total_result_size(self):
        """Gets the total_result_size of this InlineResponse2004.  # noqa: E501


        :return: The total_result_size of this InlineResponse2004.  # noqa: E501
        :rtype: int
        """
        return self._total_result_size

    @total_result_size.setter
    def total_result_size(self, total_result_size):
        """Sets the total_result_size of this InlineResponse2004.


        :param total_result_size: The total_result_size of this InlineResponse2004.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_result_size is None:  # noqa: E501
            raise ValueError("Invalid value for `total_result_size`, must not be `None`")  # noqa: E501

        self._total_result_size = total_result_size

    @property
    def data(self):
        """Gets the data of this InlineResponse2004.  # noqa: E501


        :return: The data of this InlineResponse2004.  # noqa: E501
        :rtype: list[Ruleset]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse2004.


        :param data: The data of this InlineResponse2004.  # noqa: E501
        :type: list[Ruleset]
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, InlineResponse2004):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2004):
            return True

        return self.to_dict() != other.to_dict()
