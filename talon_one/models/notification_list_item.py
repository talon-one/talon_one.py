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


class NotificationListItem(object):
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
        'notification_id': 'int',
        'notification_name': 'str',
        'entity_id': 'int',
        'enabled': 'bool'
    }

    attribute_map = {
        'notification_id': 'notificationId',
        'notification_name': 'notificationName',
        'entity_id': 'entityId',
        'enabled': 'enabled'
    }

    def __init__(self, notification_id=None, notification_name=None, entity_id=None, enabled=None, local_vars_configuration=None):  # noqa: E501
        """NotificationListItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._notification_id = None
        self._notification_name = None
        self._entity_id = None
        self._enabled = None
        self.discriminator = None

        self.notification_id = notification_id
        self.notification_name = notification_name
        self.entity_id = entity_id
        self.enabled = enabled

    @property
    def notification_id(self):
        """Gets the notification_id of this NotificationListItem.  # noqa: E501

        The ID of the notification.  # noqa: E501

        :return: The notification_id of this NotificationListItem.  # noqa: E501
        :rtype: int
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this NotificationListItem.

        The ID of the notification.  # noqa: E501

        :param notification_id: The notification_id of this NotificationListItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and notification_id is None:  # noqa: E501
            raise ValueError("Invalid value for `notification_id`, must not be `None`")  # noqa: E501

        self._notification_id = notification_id

    @property
    def notification_name(self):
        """Gets the notification_name of this NotificationListItem.  # noqa: E501

        The name of the notification.  # noqa: E501

        :return: The notification_name of this NotificationListItem.  # noqa: E501
        :rtype: str
        """
        return self._notification_name

    @notification_name.setter
    def notification_name(self, notification_name):
        """Sets the notification_name of this NotificationListItem.

        The name of the notification.  # noqa: E501

        :param notification_name: The notification_name of this NotificationListItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and notification_name is None:  # noqa: E501
            raise ValueError("Invalid value for `notification_name`, must not be `None`")  # noqa: E501

        self._notification_name = notification_name

    @property
    def entity_id(self):
        """Gets the entity_id of this NotificationListItem.  # noqa: E501

        The ID of the entity to which this notification belongs. For example, in case of a loyalty notification, this value is the ID of the loyalty program.   # noqa: E501

        :return: The entity_id of this NotificationListItem.  # noqa: E501
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this NotificationListItem.

        The ID of the entity to which this notification belongs. For example, in case of a loyalty notification, this value is the ID of the loyalty program.   # noqa: E501

        :param entity_id: The entity_id of this NotificationListItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and entity_id is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def enabled(self):
        """Gets the enabled of this NotificationListItem.  # noqa: E501

        Indicates whether the notification is activated.  # noqa: E501

        :return: The enabled of this NotificationListItem.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NotificationListItem.

        Indicates whether the notification is activated.  # noqa: E501

        :param enabled: The enabled of this NotificationListItem.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, NotificationListItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationListItem):
            return True

        return self.to_dict() != other.to_dict()