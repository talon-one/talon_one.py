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


class StrikethroughChangedItem(object):
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
        'id': 'int',
        'catalog_id': 'int',
        'sku': 'str',
        'version': 'int',
        'price': 'float',
        'evaluated_at': 'datetime',
        'effects': 'list[StrikethroughEffect]'
    }

    attribute_map = {
        'id': 'id',
        'catalog_id': 'catalogId',
        'sku': 'sku',
        'version': 'version',
        'price': 'price',
        'evaluated_at': 'evaluatedAt',
        'effects': 'effects'
    }

    def __init__(self, id=None, catalog_id=None, sku=None, version=None, price=None, evaluated_at=None, effects=None, local_vars_configuration=None):  # noqa: E501
        """StrikethroughChangedItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._catalog_id = None
        self._sku = None
        self._version = None
        self._price = None
        self._evaluated_at = None
        self._effects = None
        self.discriminator = None

        self.id = id
        self.catalog_id = catalog_id
        self.sku = sku
        self.version = version
        self.price = price
        self.evaluated_at = evaluated_at
        if effects is not None:
            self.effects = effects

    @property
    def id(self):
        """Gets the id of this StrikethroughChangedItem.  # noqa: E501

        The ID of the event that triggered the strikethrough labeling.  # noqa: E501

        :return: The id of this StrikethroughChangedItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StrikethroughChangedItem.

        The ID of the event that triggered the strikethrough labeling.  # noqa: E501

        :param id: The id of this StrikethroughChangedItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def catalog_id(self):
        """Gets the catalog_id of this StrikethroughChangedItem.  # noqa: E501

        The ID of the catalog that the changed item belongs to.  # noqa: E501

        :return: The catalog_id of this StrikethroughChangedItem.  # noqa: E501
        :rtype: int
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this StrikethroughChangedItem.

        The ID of the catalog that the changed item belongs to.  # noqa: E501

        :param catalog_id: The catalog_id of this StrikethroughChangedItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and catalog_id is None:  # noqa: E501
            raise ValueError("Invalid value for `catalog_id`, must not be `None`")  # noqa: E501

        self._catalog_id = catalog_id

    @property
    def sku(self):
        """Gets the sku of this StrikethroughChangedItem.  # noqa: E501

        The unique SKU of the changed item.  # noqa: E501

        :return: The sku of this StrikethroughChangedItem.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this StrikethroughChangedItem.

        The unique SKU of the changed item.  # noqa: E501

        :param sku: The sku of this StrikethroughChangedItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sku is None:  # noqa: E501
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501

        self._sku = sku

    @property
    def version(self):
        """Gets the version of this StrikethroughChangedItem.  # noqa: E501

        The version of the changed item.  # noqa: E501

        :return: The version of this StrikethroughChangedItem.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StrikethroughChangedItem.

        The version of the changed item.  # noqa: E501

        :param version: The version of this StrikethroughChangedItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and version < 1):  # noqa: E501
            raise ValueError("Invalid value for `version`, must be a value greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def price(self):
        """Gets the price of this StrikethroughChangedItem.  # noqa: E501

        The price of the changed item.  # noqa: E501

        :return: The price of this StrikethroughChangedItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this StrikethroughChangedItem.

        The price of the changed item.  # noqa: E501

        :param price: The price of this StrikethroughChangedItem.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and price is None:  # noqa: E501
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def evaluated_at(self):
        """Gets the evaluated_at of this StrikethroughChangedItem.  # noqa: E501

        The evaluation time of the changed item.  # noqa: E501

        :return: The evaluated_at of this StrikethroughChangedItem.  # noqa: E501
        :rtype: datetime
        """
        return self._evaluated_at

    @evaluated_at.setter
    def evaluated_at(self, evaluated_at):
        """Sets the evaluated_at of this StrikethroughChangedItem.

        The evaluation time of the changed item.  # noqa: E501

        :param evaluated_at: The evaluated_at of this StrikethroughChangedItem.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and evaluated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `evaluated_at`, must not be `None`")  # noqa: E501

        self._evaluated_at = evaluated_at

    @property
    def effects(self):
        """Gets the effects of this StrikethroughChangedItem.  # noqa: E501


        :return: The effects of this StrikethroughChangedItem.  # noqa: E501
        :rtype: list[StrikethroughEffect]
        """
        return self._effects

    @effects.setter
    def effects(self, effects):
        """Sets the effects of this StrikethroughChangedItem.


        :param effects: The effects of this StrikethroughChangedItem.  # noqa: E501
        :type: list[StrikethroughEffect]
        """

        self._effects = effects

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
        if not isinstance(other, StrikethroughChangedItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StrikethroughChangedItem):
            return True

        return self.to_dict() != other.to_dict()
