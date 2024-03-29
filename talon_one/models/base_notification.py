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


class BaseNotification(object):
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
        'webhook': 'BaseNotificationWebhook',
        'id': 'int'
    }

    attribute_map = {
        'policy': 'policy',
        'webhook': 'webhook',
        'id': 'id'
    }

    def __init__(self, policy=None, webhook=None, id=None, local_vars_configuration=None):  # noqa: E501
        """BaseNotification - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._policy = None
        self._webhook = None
        self._id = None
        self.discriminator = None

        self.policy = policy
        self.webhook = webhook
        self.id = id

    @property
    def policy(self):
        """Gets the policy of this BaseNotification.  # noqa: E501


        :return: The policy of this BaseNotification.  # noqa: E501
        :rtype: object
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this BaseNotification.


        :param policy: The policy of this BaseNotification.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and policy is None:  # noqa: E501
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def webhook(self):
        """Gets the webhook of this BaseNotification.  # noqa: E501


        :return: The webhook of this BaseNotification.  # noqa: E501
        :rtype: BaseNotificationWebhook
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this BaseNotification.


        :param webhook: The webhook of this BaseNotification.  # noqa: E501
        :type: BaseNotificationWebhook
        """
        if self.local_vars_configuration.client_side_validation and webhook is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook`, must not be `None`")  # noqa: E501

        self._webhook = webhook

    @property
    def id(self):
        """Gets the id of this BaseNotification.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this BaseNotification.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseNotification.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this BaseNotification.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and id < 1):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, BaseNotification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseNotification):
            return True

        return self.to_dict() != other.to_dict()
