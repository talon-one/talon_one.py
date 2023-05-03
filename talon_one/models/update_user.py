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


class UpdateUser(object):
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
        'policy': 'str',
        'state': 'str',
        'roles': 'list[int]',
        'application_notification_subscriptions': 'object'
    }

    attribute_map = {
        'name': 'name',
        'policy': 'policy',
        'state': 'state',
        'roles': 'roles',
        'application_notification_subscriptions': 'applicationNotificationSubscriptions'
    }

    def __init__(self, name=None, policy=None, state=None, roles=None, application_notification_subscriptions=None, local_vars_configuration=None):  # noqa: E501
        """UpdateUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._policy = None
        self._state = None
        self._roles = None
        self._application_notification_subscriptions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if policy is not None:
            self.policy = policy
        if state is not None:
            self.state = state
        if roles is not None:
            self.roles = roles
        if application_notification_subscriptions is not None:
            self.application_notification_subscriptions = application_notification_subscriptions

    @property
    def name(self):
        """Gets the name of this UpdateUser.  # noqa: E501

        The user name.  # noqa: E501

        :return: The name of this UpdateUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateUser.

        The user name.  # noqa: E501

        :param name: The name of this UpdateUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def policy(self):
        """Gets the policy of this UpdateUser.  # noqa: E501

        The `Access Control List` json defining the role of the user. This represents the access control on the user level.  # noqa: E501

        :return: The policy of this UpdateUser.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this UpdateUser.

        The `Access Control List` json defining the role of the user. This represents the access control on the user level.  # noqa: E501

        :param policy: The policy of this UpdateUser.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def state(self):
        """Gets the state of this UpdateUser.  # noqa: E501

        New state (\"deactivated\" or \"active\") for the user. Only usable by admins for the user.  # noqa: E501

        :return: The state of this UpdateUser.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateUser.

        New state (\"deactivated\" or \"active\") for the user. Only usable by admins for the user.  # noqa: E501

        :param state: The state of this UpdateUser.  # noqa: E501
        :type: str
        """
        allowed_values = ["deactivated", "active"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def roles(self):
        """Gets the roles of this UpdateUser.  # noqa: E501

        List of roles to assign to the user.  # noqa: E501

        :return: The roles of this UpdateUser.  # noqa: E501
        :rtype: list[int]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UpdateUser.

        List of roles to assign to the user.  # noqa: E501

        :param roles: The roles of this UpdateUser.  # noqa: E501
        :type: list[int]
        """

        self._roles = roles

    @property
    def application_notification_subscriptions(self):
        """Gets the application_notification_subscriptions of this UpdateUser.  # noqa: E501


        :return: The application_notification_subscriptions of this UpdateUser.  # noqa: E501
        :rtype: object
        """
        return self._application_notification_subscriptions

    @application_notification_subscriptions.setter
    def application_notification_subscriptions(self, application_notification_subscriptions):
        """Sets the application_notification_subscriptions of this UpdateUser.


        :param application_notification_subscriptions: The application_notification_subscriptions of this UpdateUser.  # noqa: E501
        :type: object
        """

        self._application_notification_subscriptions = application_notification_subscriptions

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
        if not isinstance(other, UpdateUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUser):
            return True

        return self.to_dict() != other.to_dict()
