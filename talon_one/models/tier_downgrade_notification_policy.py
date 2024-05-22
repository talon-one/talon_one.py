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


class TierDowngradeNotificationPolicy(object):
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
        'name': 'str',
        'batching_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'batching_enabled': 'batchingEnabled'
    }

    def __init__(self, name=None, batching_enabled=True, local_vars_configuration=None):  # noqa: E501
        """TierDowngradeNotificationPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._batching_enabled = None
        self.discriminator = None

        self.name = name
        if batching_enabled is not None:
            self.batching_enabled = batching_enabled

    @property
    def name(self):
        """Gets the name of this TierDowngradeNotificationPolicy.  # noqa: E501

        The name of the notification.  # noqa: E501

        :return: The name of this TierDowngradeNotificationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TierDowngradeNotificationPolicy.

        The name of the notification.  # noqa: E501

        :param name: The name of this TierDowngradeNotificationPolicy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def batching_enabled(self):
        """Gets the batching_enabled of this TierDowngradeNotificationPolicy.  # noqa: E501

        Indicates whether batching is activated.  # noqa: E501

        :return: The batching_enabled of this TierDowngradeNotificationPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._batching_enabled

    @batching_enabled.setter
    def batching_enabled(self, batching_enabled):
        """Sets the batching_enabled of this TierDowngradeNotificationPolicy.

        Indicates whether batching is activated.  # noqa: E501

        :param batching_enabled: The batching_enabled of this TierDowngradeNotificationPolicy.  # noqa: E501
        :type: bool
        """

        self._batching_enabled = batching_enabled

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
        if not isinstance(other, TierDowngradeNotificationPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TierDowngradeNotificationPolicy):
            return True

        return self.to_dict() != other.to_dict()
