# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class UpdateCatalog(object):
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
        'description': 'str',
        'name': 'str',
        'subscribed_applications_ids': 'list[int]'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'subscribed_applications_ids': 'subscribedApplicationsIds'
    }

    def __init__(self, description=None, name=None, subscribed_applications_ids=None, local_vars_configuration=None):  # noqa: E501
        """UpdateCatalog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._name = None
        self._subscribed_applications_ids = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if subscribed_applications_ids is not None:
            self.subscribed_applications_ids = subscribed_applications_ids

    @property
    def description(self):
        """Gets the description of this UpdateCatalog.  # noqa: E501

        A description of this cart item catalog.  # noqa: E501

        :return: The description of this UpdateCatalog.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCatalog.

        A description of this cart item catalog.  # noqa: E501

        :param description: The description of this UpdateCatalog.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateCatalog.  # noqa: E501

        Name of this cart item catalog.  # noqa: E501

        :return: The name of this UpdateCatalog.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCatalog.

        Name of this cart item catalog.  # noqa: E501

        :param name: The name of this UpdateCatalog.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def subscribed_applications_ids(self):
        """Gets the subscribed_applications_ids of this UpdateCatalog.  # noqa: E501

        A list of the IDs of the applications that are subscribed to this catalog.  # noqa: E501

        :return: The subscribed_applications_ids of this UpdateCatalog.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscribed_applications_ids

    @subscribed_applications_ids.setter
    def subscribed_applications_ids(self, subscribed_applications_ids):
        """Sets the subscribed_applications_ids of this UpdateCatalog.

        A list of the IDs of the applications that are subscribed to this catalog.  # noqa: E501

        :param subscribed_applications_ids: The subscribed_applications_ids of this UpdateCatalog.  # noqa: E501
        :type: list[int]
        """

        self._subscribed_applications_ids = subscribed_applications_ids

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
        if not isinstance(other, UpdateCatalog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateCatalog):
            return True

        return self.to_dict() != other.to_dict()
