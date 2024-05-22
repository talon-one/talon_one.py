# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one/`, the URL for the [updateCustomerSessionV2](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class InlineResponse20034(object):
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
        'data': 'list[Attribute]'
    }

    attribute_map = {
        'total_result_size': 'totalResultSize',
        'data': 'data'
    }

    def __init__(self, total_result_size=None, data=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20034 - a model defined in OpenAPI"""  # noqa: E501
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
        """Gets the total_result_size of this InlineResponse20034.  # noqa: E501


        :return: The total_result_size of this InlineResponse20034.  # noqa: E501
        :rtype: int
        """
        return self._total_result_size

    @total_result_size.setter
    def total_result_size(self, total_result_size):
        """Sets the total_result_size of this InlineResponse20034.


        :param total_result_size: The total_result_size of this InlineResponse20034.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_result_size is None:  # noqa: E501
            raise ValueError("Invalid value for `total_result_size`, must not be `None`")  # noqa: E501

        self._total_result_size = total_result_size

    @property
    def data(self):
        """Gets the data of this InlineResponse20034.  # noqa: E501


        :return: The data of this InlineResponse20034.  # noqa: E501
        :rtype: list[Attribute]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse20034.


        :param data: The data of this InlineResponse20034.  # noqa: E501
        :type: list[Attribute]
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
        if not isinstance(other, InlineResponse20034):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20034):
            return True

        return self.to_dict() != other.to_dict()
