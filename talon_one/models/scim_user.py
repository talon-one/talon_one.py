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


class ScimUser(object):
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
        'active': 'bool',
        'display_name': 'str',
        'user_name': 'str',
        'name': 'ScimBaseUserName',
        'id': 'str'
    }

    attribute_map = {
        'active': 'active',
        'display_name': 'displayName',
        'user_name': 'userName',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, active=None, display_name=None, user_name=None, name=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ScimUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._display_name = None
        self._user_name = None
        self._name = None
        self._id = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if display_name is not None:
            self.display_name = display_name
        self.user_name = user_name
        if name is not None:
            self.name = name
        self.id = id

    @property
    def active(self):
        """Gets the active of this ScimUser.  # noqa: E501

        Status of the user.  # noqa: E501

        :return: The active of this ScimUser.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ScimUser.

        Status of the user.  # noqa: E501

        :param active: The active of this ScimUser.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def display_name(self):
        """Gets the display_name of this ScimUser.  # noqa: E501

        Display name of the user.  # noqa: E501

        :return: The display_name of this ScimUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ScimUser.

        Display name of the user.  # noqa: E501

        :param display_name: The display_name of this ScimUser.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def user_name(self):
        """Gets the user_name of this ScimUser.  # noqa: E501

        Unique identifier of the user. This is usually an email address.  # noqa: E501

        :return: The user_name of this ScimUser.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ScimUser.

        Unique identifier of the user. This is usually an email address.  # noqa: E501

        :param user_name: The user_name of this ScimUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_name is None:  # noqa: E501
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def name(self):
        """Gets the name of this ScimUser.  # noqa: E501


        :return: The name of this ScimUser.  # noqa: E501
        :rtype: ScimBaseUserName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScimUser.


        :param name: The name of this ScimUser.  # noqa: E501
        :type: ScimBaseUserName
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this ScimUser.  # noqa: E501

        ID of the user.  # noqa: E501

        :return: The id of this ScimUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScimUser.

        ID of the user.  # noqa: E501

        :param id: The id of this ScimUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, ScimUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScimUser):
            return True

        return self.to_dict() != other.to_dict()
