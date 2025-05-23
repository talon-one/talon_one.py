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


class ProductSearchMatch(object):
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
        'product_id': 'int',
        'value': 'str',
        'product_sku_id': 'int'
    }

    attribute_map = {
        'product_id': 'productId',
        'value': 'value',
        'product_sku_id': 'productSkuId'
    }

    def __init__(self, product_id=None, value=None, product_sku_id=None, local_vars_configuration=None):  # noqa: E501
        """ProductSearchMatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._product_id = None
        self._value = None
        self._product_sku_id = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        self.value = value
        if product_sku_id is not None:
            self.product_sku_id = product_sku_id

    @property
    def product_id(self):
        """Gets the product_id of this ProductSearchMatch.  # noqa: E501

        The ID of the product.  # noqa: E501

        :return: The product_id of this ProductSearchMatch.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProductSearchMatch.

        The ID of the product.  # noqa: E501

        :param product_id: The product_id of this ProductSearchMatch.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def value(self):
        """Gets the value of this ProductSearchMatch.  # noqa: E501

        The string matching the given value. Either a product name or SKU.  # noqa: E501

        :return: The value of this ProductSearchMatch.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProductSearchMatch.

        The string matching the given value. Either a product name or SKU.  # noqa: E501

        :param value: The value of this ProductSearchMatch.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def product_sku_id(self):
        """Gets the product_sku_id of this ProductSearchMatch.  # noqa: E501

        The ID of the SKU linked to a product. If empty, this is an product.  # noqa: E501

        :return: The product_sku_id of this ProductSearchMatch.  # noqa: E501
        :rtype: int
        """
        return self._product_sku_id

    @product_sku_id.setter
    def product_sku_id(self, product_sku_id):
        """Sets the product_sku_id of this ProductSearchMatch.

        The ID of the SKU linked to a product. If empty, this is an product.  # noqa: E501

        :param product_sku_id: The product_sku_id of this ProductSearchMatch.  # noqa: E501
        :type: int
        """

        self._product_sku_id = product_sku_id

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
        if not isinstance(other, ProductSearchMatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductSearchMatch):
            return True

        return self.to_dict() != other.to_dict()
