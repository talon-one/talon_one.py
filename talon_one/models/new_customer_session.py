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


class NewCustomerSession(object):
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
        'profile_id': 'str',
        'coupon': 'str',
        'referral': 'str',
        'state': 'str',
        'cart_items': 'list[CartItem]',
        'identifiers': 'list[str]',
        'total': 'float',
        'attributes': 'object'
    }

    attribute_map = {
        'profile_id': 'profileId',
        'coupon': 'coupon',
        'referral': 'referral',
        'state': 'state',
        'cart_items': 'cartItems',
        'identifiers': 'identifiers',
        'total': 'total',
        'attributes': 'attributes'
    }

    def __init__(self, profile_id=None, coupon=None, referral=None, state='open', cart_items=None, identifiers=None, total=None, attributes=None, local_vars_configuration=None):  # noqa: E501
        """NewCustomerSession - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._profile_id = None
        self._coupon = None
        self._referral = None
        self._state = None
        self._cart_items = None
        self._identifiers = None
        self._total = None
        self._attributes = None
        self.discriminator = None

        if profile_id is not None:
            self.profile_id = profile_id
        if coupon is not None:
            self.coupon = coupon
        if referral is not None:
            self.referral = referral
        if state is not None:
            self.state = state
        if cart_items is not None:
            self.cart_items = cart_items
        if identifiers is not None:
            self.identifiers = identifiers
        if total is not None:
            self.total = total
        if attributes is not None:
            self.attributes = attributes

    @property
    def profile_id(self):
        """Gets the profile_id of this NewCustomerSession.  # noqa: E501

        ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known `profileId`, we recommend you use a guest `profileId`.   # noqa: E501

        :return: The profile_id of this NewCustomerSession.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this NewCustomerSession.

        ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known `profileId`, we recommend you use a guest `profileId`.   # noqa: E501

        :param profile_id: The profile_id of this NewCustomerSession.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def coupon(self):
        """Gets the coupon of this NewCustomerSession.  # noqa: E501

        Any coupon code entered.  # noqa: E501

        :return: The coupon of this NewCustomerSession.  # noqa: E501
        :rtype: str
        """
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        """Sets the coupon of this NewCustomerSession.

        Any coupon code entered.  # noqa: E501

        :param coupon: The coupon of this NewCustomerSession.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                coupon is not None and len(coupon) > 100):
            raise ValueError("Invalid value for `coupon`, length must be less than or equal to `100`")  # noqa: E501

        self._coupon = coupon

    @property
    def referral(self):
        """Gets the referral of this NewCustomerSession.  # noqa: E501

        Any referral code entered.  # noqa: E501

        :return: The referral of this NewCustomerSession.  # noqa: E501
        :rtype: str
        """
        return self._referral

    @referral.setter
    def referral(self, referral):
        """Sets the referral of this NewCustomerSession.

        Any referral code entered.  # noqa: E501

        :param referral: The referral of this NewCustomerSession.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                referral is not None and len(referral) > 100):
            raise ValueError("Invalid value for `referral`, length must be less than or equal to `100`")  # noqa: E501

        self._referral = referral

    @property
    def state(self):
        """Gets the state of this NewCustomerSession.  # noqa: E501

        Indicates the current state of the session. Sessions can be created as `open` or `closed`. The state transitions are:  1. `open` → `closed` 2. `open` → `cancelled` 3. `closed` → `cancelled` or `partially_returned` 4. `partially_returned` → `cancelled`  For more information, see [Customer session states](https://docs.talon.one/docs/dev/concepts/entities/customer-sessions).   # noqa: E501

        :return: The state of this NewCustomerSession.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NewCustomerSession.

        Indicates the current state of the session. Sessions can be created as `open` or `closed`. The state transitions are:  1. `open` → `closed` 2. `open` → `cancelled` 3. `closed` → `cancelled` or `partially_returned` 4. `partially_returned` → `cancelled`  For more information, see [Customer session states](https://docs.talon.one/docs/dev/concepts/entities/customer-sessions).   # noqa: E501

        :param state: The state of this NewCustomerSession.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "closed", "partially_returned", "cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def cart_items(self):
        """Gets the cart_items of this NewCustomerSession.  # noqa: E501

        Serialized JSON representation.  # noqa: E501

        :return: The cart_items of this NewCustomerSession.  # noqa: E501
        :rtype: list[CartItem]
        """
        return self._cart_items

    @cart_items.setter
    def cart_items(self, cart_items):
        """Sets the cart_items of this NewCustomerSession.

        Serialized JSON representation.  # noqa: E501

        :param cart_items: The cart_items of this NewCustomerSession.  # noqa: E501
        :type: list[CartItem]
        """

        self._cart_items = cart_items

    @property
    def identifiers(self):
        """Gets the identifiers of this NewCustomerSession.  # noqa: E501

        Session custom identifiers that you can set limits on or use inside your rules.  For example, you can use IP addresses as identifiers to potentially identify devices and limit discounts abuse in case of customers creating multiple accounts. See the [tutorial](https://docs.talon.one/docs/dev/tutorials/using-identifiers).   # noqa: E501

        :return: The identifiers of this NewCustomerSession.  # noqa: E501
        :rtype: list[str]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this NewCustomerSession.

        Session custom identifiers that you can set limits on or use inside your rules.  For example, you can use IP addresses as identifiers to potentially identify devices and limit discounts abuse in case of customers creating multiple accounts. See the [tutorial](https://docs.talon.one/docs/dev/tutorials/using-identifiers).   # noqa: E501

        :param identifiers: The identifiers of this NewCustomerSession.  # noqa: E501
        :type: list[str]
        """

        self._identifiers = identifiers

    @property
    def total(self):
        """Gets the total of this NewCustomerSession.  # noqa: E501

        The total sum of the cart in one session.  # noqa: E501

        :return: The total of this NewCustomerSession.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NewCustomerSession.

        The total sum of the cart in one session.  # noqa: E501

        :param total: The total of this NewCustomerSession.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def attributes(self):
        """Gets the attributes of this NewCustomerSession.  # noqa: E501

        A key-value map of the sessions attributes. The potentially valid attributes are configured in your accounts developer settings.   # noqa: E501

        :return: The attributes of this NewCustomerSession.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NewCustomerSession.

        A key-value map of the sessions attributes. The potentially valid attributes are configured in your accounts developer settings.   # noqa: E501

        :param attributes: The attributes of this NewCustomerSession.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

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
        if not isinstance(other, NewCustomerSession):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewCustomerSession):
            return True

        return self.to_dict() != other.to_dict()
