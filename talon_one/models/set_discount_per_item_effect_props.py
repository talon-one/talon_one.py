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


class SetDiscountPerItemEffectProps(object):
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
        'value': 'float',
        'position': 'float'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'position': 'position'
    }

    def __init__(self, name=None, value=None, position=None, local_vars_configuration=None):  # noqa: E501
        """SetDiscountPerItemEffectProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._value = None
        self._position = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.position = position

    @property
    def name(self):
        """Gets the name of this SetDiscountPerItemEffectProps.  # noqa: E501

        The name/description of this discount  # noqa: E501

        :return: The name of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SetDiscountPerItemEffectProps.

        The name/description of this discount  # noqa: E501

        :param name: The name of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this SetDiscountPerItemEffectProps.  # noqa: E501

        The total monetary value of the discount  # noqa: E501

        :return: The value of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SetDiscountPerItemEffectProps.

        The total monetary value of the discount  # noqa: E501

        :param value: The value of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def position(self):
        """Gets the position of this SetDiscountPerItemEffectProps.  # noqa: E501

        The index of the item in the cart items list on which this discount should be applied  # noqa: E501

        :return: The position of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this SetDiscountPerItemEffectProps.

        The index of the item in the cart items list on which this discount should be applied  # noqa: E501

        :param position: The position of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and position is None:  # noqa: E501
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

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
        if not isinstance(other, SetDiscountPerItemEffectProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetDiscountPerItemEffectProps):
            return True

        return self.to_dict() != other.to_dict()
