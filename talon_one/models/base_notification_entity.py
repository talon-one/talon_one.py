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


class BaseNotificationEntity(object):
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
        'policy': 'object',
        'enabled': 'bool'
    }

    attribute_map = {
        'policy': 'policy',
        'enabled': 'enabled'
    }

    def __init__(self, policy=None, enabled=True, local_vars_configuration=None):  # noqa: E501
        """BaseNotificationEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._policy = None
        self._enabled = None
        self.discriminator = None

        self.policy = policy
        if enabled is not None:
            self.enabled = enabled

    @property
    def policy(self):
        """Gets the policy of this BaseNotificationEntity.  # noqa: E501


        :return: The policy of this BaseNotificationEntity.  # noqa: E501
        :rtype: object
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this BaseNotificationEntity.


        :param policy: The policy of this BaseNotificationEntity.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and policy is None:  # noqa: E501
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def enabled(self):
        """Gets the enabled of this BaseNotificationEntity.  # noqa: E501

        Indicates whether the notification is activated.  # noqa: E501

        :return: The enabled of this BaseNotificationEntity.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this BaseNotificationEntity.

        Indicates whether the notification is activated.  # noqa: E501

        :param enabled: The enabled of this BaseNotificationEntity.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, BaseNotificationEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseNotificationEntity):
            return True

        return self.to_dict() != other.to_dict()
