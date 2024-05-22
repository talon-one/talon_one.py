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


class CartItem(object):
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
        'sku': 'str',
        'quantity': 'int',
        'returned_quantity': 'int',
        'remaining_quantity': 'int',
        'price': 'float',
        'category': 'str',
        'product': 'Product',
        'weight': 'float',
        'height': 'float',
        'width': 'float',
        'length': 'float',
        'position': 'float',
        'attributes': 'object',
        'additional_costs': 'dict(str, AdditionalCost)',
        'catalog_item_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'sku': 'sku',
        'quantity': 'quantity',
        'returned_quantity': 'returnedQuantity',
        'remaining_quantity': 'remainingQuantity',
        'price': 'price',
        'category': 'category',
        'product': 'product',
        'weight': 'weight',
        'height': 'height',
        'width': 'width',
        'length': 'length',
        'position': 'position',
        'attributes': 'attributes',
        'additional_costs': 'additionalCosts',
        'catalog_item_id': 'catalogItemID'
    }

    def __init__(self, name=None, sku=None, quantity=None, returned_quantity=None, remaining_quantity=None, price=None, category=None, product=None, weight=None, height=None, width=None, length=None, position=None, attributes=None, additional_costs=None, catalog_item_id=None, local_vars_configuration=None):  # noqa: E501
        """CartItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._sku = None
        self._quantity = None
        self._returned_quantity = None
        self._remaining_quantity = None
        self._price = None
        self._category = None
        self._product = None
        self._weight = None
        self._height = None
        self._width = None
        self._length = None
        self._position = None
        self._attributes = None
        self._additional_costs = None
        self._catalog_item_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.sku = sku
        self.quantity = quantity
        if returned_quantity is not None:
            self.returned_quantity = returned_quantity
        if remaining_quantity is not None:
            self.remaining_quantity = remaining_quantity
        if price is not None:
            self.price = price
        if category is not None:
            self.category = category
        if product is not None:
            self.product = product
        if weight is not None:
            self.weight = weight
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if length is not None:
            self.length = length
        if position is not None:
            self.position = position
        if attributes is not None:
            self.attributes = attributes
        if additional_costs is not None:
            self.additional_costs = additional_costs
        if catalog_item_id is not None:
            self.catalog_item_id = catalog_item_id

    @property
    def name(self):
        """Gets the name of this CartItem.  # noqa: E501

        Name of item.  # noqa: E501

        :return: The name of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CartItem.

        Name of item.  # noqa: E501

        :param name: The name of this CartItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sku(self):
        """Gets the sku of this CartItem.  # noqa: E501

        Stock keeping unit of item.  # noqa: E501

        :return: The sku of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this CartItem.

        Stock keeping unit of item.  # noqa: E501

        :param sku: The sku of this CartItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sku is None:  # noqa: E501
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sku is not None and len(sku) < 1):
            raise ValueError("Invalid value for `sku`, length must be greater than or equal to `1`")  # noqa: E501

        self._sku = sku

    @property
    def quantity(self):
        """Gets the quantity of this CartItem.  # noqa: E501

        Number of units of this item. Due to [cart item flattening](https://docs.talon.one/docs/product/rules/understanding-cart-item-flattening), if you provide a quantity greater than 1, the item will be split in as many items as the provided quantity. This will impact the number of **per-item** effects triggered from your campaigns.   # noqa: E501

        :return: The quantity of this CartItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CartItem.

        Number of units of this item. Due to [cart item flattening](https://docs.talon.one/docs/product/rules/understanding-cart-item-flattening), if you provide a quantity greater than 1, the item will be split in as many items as the provided quantity. This will impact the number of **per-item** effects triggered from your campaigns.   # noqa: E501

        :param quantity: The quantity of this CartItem.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                quantity is not None and quantity < 1):  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._quantity = quantity

    @property
    def returned_quantity(self):
        """Gets the returned_quantity of this CartItem.  # noqa: E501

        Number of returned items, calculated internally based on returns of this item.  # noqa: E501

        :return: The returned_quantity of this CartItem.  # noqa: E501
        :rtype: int
        """
        return self._returned_quantity

    @returned_quantity.setter
    def returned_quantity(self, returned_quantity):
        """Sets the returned_quantity of this CartItem.

        Number of returned items, calculated internally based on returns of this item.  # noqa: E501

        :param returned_quantity: The returned_quantity of this CartItem.  # noqa: E501
        :type: int
        """

        self._returned_quantity = returned_quantity

    @property
    def remaining_quantity(self):
        """Gets the remaining_quantity of this CartItem.  # noqa: E501

        Remaining quantity of the item, calculated internally based on returns of this item.  # noqa: E501

        :return: The remaining_quantity of this CartItem.  # noqa: E501
        :rtype: int
        """
        return self._remaining_quantity

    @remaining_quantity.setter
    def remaining_quantity(self, remaining_quantity):
        """Sets the remaining_quantity of this CartItem.

        Remaining quantity of the item, calculated internally based on returns of this item.  # noqa: E501

        :param remaining_quantity: The remaining_quantity of this CartItem.  # noqa: E501
        :type: int
        """

        self._remaining_quantity = remaining_quantity

    @property
    def price(self):
        """Gets the price of this CartItem.  # noqa: E501

        Price of the item in the currency defined by your Application. This field is required if this item is not part of a [catalog](https://docs.talon.one/docs/product/account/dev-tools/managing-cart-item-catalogs). If it is part of a catalog, setting a price here overrides the price from the catalog.   # noqa: E501

        :return: The price of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CartItem.

        Price of the item in the currency defined by your Application. This field is required if this item is not part of a [catalog](https://docs.talon.one/docs/product/account/dev-tools/managing-cart-item-catalogs). If it is part of a catalog, setting a price here overrides the price from the catalog.   # noqa: E501

        :param price: The price of this CartItem.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def category(self):
        """Gets the category of this CartItem.  # noqa: E501

        Type, group or model of the item.  # noqa: E501

        :return: The category of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CartItem.

        Type, group or model of the item.  # noqa: E501

        :param category: The category of this CartItem.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def product(self):
        """Gets the product of this CartItem.  # noqa: E501


        :return: The product of this CartItem.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this CartItem.


        :param product: The product of this CartItem.  # noqa: E501
        :type: Product
        """

        self._product = product

    @property
    def weight(self):
        """Gets the weight of this CartItem.  # noqa: E501

        Weight of item in grams.  # noqa: E501

        :return: The weight of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CartItem.

        Weight of item in grams.  # noqa: E501

        :param weight: The weight of this CartItem.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def height(self):
        """Gets the height of this CartItem.  # noqa: E501

        Height of item in mm.  # noqa: E501

        :return: The height of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CartItem.

        Height of item in mm.  # noqa: E501

        :param height: The height of this CartItem.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this CartItem.  # noqa: E501

        Width of item in mm.  # noqa: E501

        :return: The width of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CartItem.

        Width of item in mm.  # noqa: E501

        :param width: The width of this CartItem.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def length(self):
        """Gets the length of this CartItem.  # noqa: E501

        Length of item in mm.  # noqa: E501

        :return: The length of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CartItem.

        Length of item in mm.  # noqa: E501

        :param length: The length of this CartItem.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def position(self):
        """Gets the position of this CartItem.  # noqa: E501

        Position of the Cart Item in the Cart (calculated internally).  # noqa: E501

        :return: The position of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CartItem.

        Position of the Cart Item in the Cart (calculated internally).  # noqa: E501

        :param position: The position of this CartItem.  # noqa: E501
        :type: float
        """

        self._position = position

    @property
    def attributes(self):
        """Gets the attributes of this CartItem.  # noqa: E501

        Use this property to set a value for the attributes of your choice. [Attributes](https://docs.talon.one/docs/dev/concepts/attributes) represent any information to attach to this cart item.  Custom _cart item_ attributes must be created in the Campaign Manager before you set them with this property.   # noqa: E501

        :return: The attributes of this CartItem.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CartItem.

        Use this property to set a value for the attributes of your choice. [Attributes](https://docs.talon.one/docs/dev/concepts/attributes) represent any information to attach to this cart item.  Custom _cart item_ attributes must be created in the Campaign Manager before you set them with this property.   # noqa: E501

        :param attributes: The attributes of this CartItem.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def additional_costs(self):
        """Gets the additional_costs of this CartItem.  # noqa: E501

        Use this property to set a value for the additional costs of this item, such as a shipping cost. They must be created in the Campaign Manager before you set them with this property. See [Managing additional costs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).   # noqa: E501

        :return: The additional_costs of this CartItem.  # noqa: E501
        :rtype: dict(str, AdditionalCost)
        """
        return self._additional_costs

    @additional_costs.setter
    def additional_costs(self, additional_costs):
        """Sets the additional_costs of this CartItem.

        Use this property to set a value for the additional costs of this item, such as a shipping cost. They must be created in the Campaign Manager before you set them with this property. See [Managing additional costs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).   # noqa: E501

        :param additional_costs: The additional_costs of this CartItem.  # noqa: E501
        :type: dict(str, AdditionalCost)
        """

        self._additional_costs = additional_costs

    @property
    def catalog_item_id(self):
        """Gets the catalog_item_id of this CartItem.  # noqa: E501

        The [catalog item ID](https://docs.talon.one/docs/product/account/dev-tools/managing-cart-item-catalogs/#synchronizing-a-cart-item-catalog).  # noqa: E501

        :return: The catalog_item_id of this CartItem.  # noqa: E501
        :rtype: int
        """
        return self._catalog_item_id

    @catalog_item_id.setter
    def catalog_item_id(self, catalog_item_id):
        """Sets the catalog_item_id of this CartItem.

        The [catalog item ID](https://docs.talon.one/docs/product/account/dev-tools/managing-cart-item-catalogs/#synchronizing-a-cart-item-catalog).  # noqa: E501

        :param catalog_item_id: The catalog_item_id of this CartItem.  # noqa: E501
        :type: int
        """

        self._catalog_item_id = catalog_item_id

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
        if not isinstance(other, CartItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CartItem):
            return True

        return self.to_dict() != other.to_dict()
