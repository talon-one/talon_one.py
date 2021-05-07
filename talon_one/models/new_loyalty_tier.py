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


class NewLoyaltyTier(object):
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
        'min_points': 'float'
    }

    attribute_map = {
        'name': 'name',
        'min_points': 'minPoints'
    }

    def __init__(self, name=None, min_points=None, local_vars_configuration=None):  # noqa: E501
        """NewLoyaltyTier - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._min_points = None
        self.discriminator = None

        self.name = name
        self.min_points = min_points

    @property
    def name(self):
        """Gets the name of this NewLoyaltyTier.  # noqa: E501

        The name of the tier  # noqa: E501

        :return: The name of this NewLoyaltyTier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewLoyaltyTier.

        The name of the tier  # noqa: E501

        :param name: The name of this NewLoyaltyTier.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def min_points(self):
        """Gets the min_points of this NewLoyaltyTier.  # noqa: E501

        The minimum amount of points required to be eligible for the tier  # noqa: E501

        :return: The min_points of this NewLoyaltyTier.  # noqa: E501
        :rtype: float
        """
        return self._min_points

    @min_points.setter
    def min_points(self, min_points):
        """Sets the min_points of this NewLoyaltyTier.

        The minimum amount of points required to be eligible for the tier  # noqa: E501

        :param min_points: The min_points of this NewLoyaltyTier.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and min_points is None:  # noqa: E501
            raise ValueError("Invalid value for `min_points`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_points is not None and min_points >= 100000000):  # noqa: E501
            raise ValueError("Invalid value for `min_points`, must be a value less than `100000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_points is not None and min_points < 0):  # noqa: E501
            raise ValueError("Invalid value for `min_points`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_points = min_points

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
        if not isinstance(other, NewLoyaltyTier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewLoyaltyTier):
            return True

        return self.to_dict() != other.to_dict()
