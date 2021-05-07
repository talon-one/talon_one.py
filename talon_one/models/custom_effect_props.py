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


class CustomEffectProps(object):
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
        'type': 'str',
        'payload': 'object'
    }

    attribute_map = {
        'type': 'type',
        'payload': 'payload'
    }

    def __init__(self, type=None, payload=None, local_vars_configuration=None):  # noqa: E501
        """CustomEffectProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._payload = None
        self.discriminator = None

        self.type = type
        self.payload = payload

    @property
    def type(self):
        """Gets the type of this CustomEffectProps.  # noqa: E501

        The type of the custom effect.  # noqa: E501

        :return: The type of this CustomEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomEffectProps.

        The type of the custom effect.  # noqa: E501

        :param type: The type of this CustomEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def payload(self):
        """Gets the payload of this CustomEffectProps.  # noqa: E501

        The JSON payload of the custom effect.  # noqa: E501

        :return: The payload of this CustomEffectProps.  # noqa: E501
        :rtype: object
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this CustomEffectProps.

        The JSON payload of the custom effect.  # noqa: E501

        :param payload: The payload of this CustomEffectProps.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and payload is None:  # noqa: E501
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

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
        if not isinstance(other, CustomEffectProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomEffectProps):
            return True

        return self.to_dict() != other.to_dict()
