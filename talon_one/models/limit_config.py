# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LimitConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'str',
        'limit': 'float',
        'entities': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'limit': 'limit',
        'entities': 'entities'
    }

    def __init__(self, action=None, limit=None, entities=None):  # noqa: E501
        """LimitConfig - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._limit = None
        self._entities = None
        self.discriminator = None

        self.action = action
        self.limit = limit
        self.entities = entities

    @property
    def action(self):
        """Gets the action of this LimitConfig.  # noqa: E501

        The limitable action to which this limit will be applied  # noqa: E501

        :return: The action of this LimitConfig.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this LimitConfig.

        The limitable action to which this limit will be applied  # noqa: E501

        :param action: The action of this LimitConfig.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["redeemCoupon", "redeemReferral", "setDiscount", "createCoupon"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def limit(self):
        """Gets the limit of this LimitConfig.  # noqa: E501

        The value to set for the limit  # noqa: E501

        :return: The limit of this LimitConfig.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this LimitConfig.

        The value to set for the limit  # noqa: E501

        :param limit: The limit of this LimitConfig.  # noqa: E501
        :type: float
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501
        if limit is not None and limit < 0:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._limit = limit

    @property
    def entities(self):
        """Gets the entities of this LimitConfig.  # noqa: E501

        The entities that make the address of this limit  # noqa: E501

        :return: The entities of this LimitConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this LimitConfig.

        The entities that make the address of this limit  # noqa: E501

        :param entities: The entities of this LimitConfig.  # noqa: E501
        :type: list[str]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")  # noqa: E501
        allowed_values = ["Coupon", "Referral", "Profile", "Identifier"]  # noqa: E501
        if not set(entities).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `entities` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(entities) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._entities = entities

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(LimitConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LimitConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other