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


class NewApplicationCIFExpression(object):
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
        'cart_item_filter_id': 'int',
        'created_by': 'int',
        'expression': 'list[object]'
    }

    attribute_map = {
        'cart_item_filter_id': 'cartItemFilterId',
        'created_by': 'createdBy',
        'expression': 'expression'
    }

    def __init__(self, cart_item_filter_id=None, created_by=None, expression=None, local_vars_configuration=None):  # noqa: E501
        """NewApplicationCIFExpression - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cart_item_filter_id = None
        self._created_by = None
        self._expression = None
        self.discriminator = None

        if cart_item_filter_id is not None:
            self.cart_item_filter_id = cart_item_filter_id
        if created_by is not None:
            self.created_by = created_by
        if expression is not None:
            self.expression = expression

    @property
    def cart_item_filter_id(self):
        """Gets the cart_item_filter_id of this NewApplicationCIFExpression.  # noqa: E501

        The ID of the Application cart item filter.  # noqa: E501

        :return: The cart_item_filter_id of this NewApplicationCIFExpression.  # noqa: E501
        :rtype: int
        """
        return self._cart_item_filter_id

    @cart_item_filter_id.setter
    def cart_item_filter_id(self, cart_item_filter_id):
        """Sets the cart_item_filter_id of this NewApplicationCIFExpression.

        The ID of the Application cart item filter.  # noqa: E501

        :param cart_item_filter_id: The cart_item_filter_id of this NewApplicationCIFExpression.  # noqa: E501
        :type: int
        """

        self._cart_item_filter_id = cart_item_filter_id

    @property
    def created_by(self):
        """Gets the created_by of this NewApplicationCIFExpression.  # noqa: E501

        The ID of the user who created the Application cart item filter.  # noqa: E501

        :return: The created_by of this NewApplicationCIFExpression.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this NewApplicationCIFExpression.

        The ID of the user who created the Application cart item filter.  # noqa: E501

        :param created_by: The created_by of this NewApplicationCIFExpression.  # noqa: E501
        :type: int
        """

        self._created_by = created_by

    @property
    def expression(self):
        """Gets the expression of this NewApplicationCIFExpression.  # noqa: E501

        Arbitrary additional JSON data associated with the Application cart item filter.  # noqa: E501

        :return: The expression of this NewApplicationCIFExpression.  # noqa: E501
        :rtype: list[object]
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this NewApplicationCIFExpression.

        Arbitrary additional JSON data associated with the Application cart item filter.  # noqa: E501

        :param expression: The expression of this NewApplicationCIFExpression.  # noqa: E501
        :type: list[object]
        """

        self._expression = expression

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
        if not isinstance(other, NewApplicationCIFExpression):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewApplicationCIFExpression):
            return True

        return self.to_dict() != other.to_dict()
