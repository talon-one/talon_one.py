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


class NewCouponsForMultipleRecipients(object):
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
        'usage_limit': 'int',
        'discount_limit': 'float',
        'reservation_limit': 'int',
        'start_date': 'datetime',
        'expiry_date': 'datetime',
        'attributes': 'object',
        'recipients_integration_ids': 'list[str]',
        'valid_characters': 'list[str]',
        'coupon_pattern': 'str'
    }

    attribute_map = {
        'usage_limit': 'usageLimit',
        'discount_limit': 'discountLimit',
        'reservation_limit': 'reservationLimit',
        'start_date': 'startDate',
        'expiry_date': 'expiryDate',
        'attributes': 'attributes',
        'recipients_integration_ids': 'recipientsIntegrationIds',
        'valid_characters': 'validCharacters',
        'coupon_pattern': 'couponPattern'
    }

    def __init__(self, usage_limit=None, discount_limit=None, reservation_limit=None, start_date=None, expiry_date=None, attributes=None, recipients_integration_ids=None, valid_characters=None, coupon_pattern=None, local_vars_configuration=None):  # noqa: E501
        """NewCouponsForMultipleRecipients - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._usage_limit = None
        self._discount_limit = None
        self._reservation_limit = None
        self._start_date = None
        self._expiry_date = None
        self._attributes = None
        self._recipients_integration_ids = None
        self._valid_characters = None
        self._coupon_pattern = None
        self.discriminator = None

        self.usage_limit = usage_limit
        if discount_limit is not None:
            self.discount_limit = discount_limit
        if reservation_limit is not None:
            self.reservation_limit = reservation_limit
        if start_date is not None:
            self.start_date = start_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if attributes is not None:
            self.attributes = attributes
        self.recipients_integration_ids = recipients_integration_ids
        if valid_characters is not None:
            self.valid_characters = valid_characters
        if coupon_pattern is not None:
            self.coupon_pattern = coupon_pattern

    @property
    def usage_limit(self):
        """Gets the usage_limit of this NewCouponsForMultipleRecipients.  # noqa: E501

        The number of times the coupon code can be redeemed. `0` means unlimited redemptions but any campaign usage limits will still apply.   # noqa: E501

        :return: The usage_limit of this NewCouponsForMultipleRecipients.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this NewCouponsForMultipleRecipients.

        The number of times the coupon code can be redeemed. `0` means unlimited redemptions but any campaign usage limits will still apply.   # noqa: E501

        :param usage_limit: The usage_limit of this NewCouponsForMultipleRecipients.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and usage_limit is None:  # noqa: E501
            raise ValueError("Invalid value for `usage_limit`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                usage_limit is not None and usage_limit > 999999):  # noqa: E501
            raise ValueError("Invalid value for `usage_limit`, must be a value less than or equal to `999999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                usage_limit is not None and usage_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `usage_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._usage_limit = usage_limit

    @property
    def discount_limit(self):
        """Gets the discount_limit of this NewCouponsForMultipleRecipients.  # noqa: E501

        The total discount value that the code can give. Typically used to represent a gift card value.   # noqa: E501

        :return: The discount_limit of this NewCouponsForMultipleRecipients.  # noqa: E501
        :rtype: float
        """
        return self._discount_limit

    @discount_limit.setter
    def discount_limit(self, discount_limit):
        """Sets the discount_limit of this NewCouponsForMultipleRecipients.

        The total discount value that the code can give. Typically used to represent a gift card value.   # noqa: E501

        :param discount_limit: The discount_limit of this NewCouponsForMultipleRecipients.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                discount_limit is not None and discount_limit > 999999):  # noqa: E501
            raise ValueError("Invalid value for `discount_limit`, must be a value less than or equal to `999999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                discount_limit is not None and discount_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `discount_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._discount_limit = discount_limit

    @property
    def reservation_limit(self):
        """Gets the reservation_limit of this NewCouponsForMultipleRecipients.  # noqa: E501

        The number of reservations that can be made with this coupon code.   # noqa: E501

        :return: The reservation_limit of this NewCouponsForMultipleRecipients.  # noqa: E501
        :rtype: int
        """
        return self._reservation_limit

    @reservation_limit.setter
    def reservation_limit(self, reservation_limit):
        """Sets the reservation_limit of this NewCouponsForMultipleRecipients.

        The number of reservations that can be made with this coupon code.   # noqa: E501

        :param reservation_limit: The reservation_limit of this NewCouponsForMultipleRecipients.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                reservation_limit is not None and reservation_limit > 999999):  # noqa: E501
            raise ValueError("Invalid value for `reservation_limit`, must be a value less than or equal to `999999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reservation_limit is not None and reservation_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `reservation_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reservation_limit = reservation_limit

    @property
    def start_date(self):
        """Gets the start_date of this NewCouponsForMultipleRecipients.  # noqa: E501

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :return: The start_date of this NewCouponsForMultipleRecipients.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this NewCouponsForMultipleRecipients.

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :param start_date: The start_date of this NewCouponsForMultipleRecipients.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this NewCouponsForMultipleRecipients.  # noqa: E501

        Expiration date of the coupon. Coupon never expires if this is omitted.  # noqa: E501

        :return: The expiry_date of this NewCouponsForMultipleRecipients.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this NewCouponsForMultipleRecipients.

        Expiration date of the coupon. Coupon never expires if this is omitted.  # noqa: E501

        :param expiry_date: The expiry_date of this NewCouponsForMultipleRecipients.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def attributes(self):
        """Gets the attributes of this NewCouponsForMultipleRecipients.  # noqa: E501

        Arbitrary properties associated with this item.  # noqa: E501

        :return: The attributes of this NewCouponsForMultipleRecipients.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NewCouponsForMultipleRecipients.

        Arbitrary properties associated with this item.  # noqa: E501

        :param attributes: The attributes of this NewCouponsForMultipleRecipients.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def recipients_integration_ids(self):
        """Gets the recipients_integration_ids of this NewCouponsForMultipleRecipients.  # noqa: E501

        The integration IDs for recipients.  # noqa: E501

        :return: The recipients_integration_ids of this NewCouponsForMultipleRecipients.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients_integration_ids

    @recipients_integration_ids.setter
    def recipients_integration_ids(self, recipients_integration_ids):
        """Sets the recipients_integration_ids of this NewCouponsForMultipleRecipients.

        The integration IDs for recipients.  # noqa: E501

        :param recipients_integration_ids: The recipients_integration_ids of this NewCouponsForMultipleRecipients.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and recipients_integration_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `recipients_integration_ids`, must not be `None`")  # noqa: E501

        self._recipients_integration_ids = recipients_integration_ids

    @property
    def valid_characters(self):
        """Gets the valid_characters of this NewCouponsForMultipleRecipients.  # noqa: E501

        List of characters used to generate the random parts of a code. By default, the list of characters is equivalent to the `[A-Z, 0-9]` regular expression.   # noqa: E501

        :return: The valid_characters of this NewCouponsForMultipleRecipients.  # noqa: E501
        :rtype: list[str]
        """
        return self._valid_characters

    @valid_characters.setter
    def valid_characters(self, valid_characters):
        """Sets the valid_characters of this NewCouponsForMultipleRecipients.

        List of characters used to generate the random parts of a code. By default, the list of characters is equivalent to the `[A-Z, 0-9]` regular expression.   # noqa: E501

        :param valid_characters: The valid_characters of this NewCouponsForMultipleRecipients.  # noqa: E501
        :type: list[str]
        """

        self._valid_characters = valid_characters

    @property
    def coupon_pattern(self):
        """Gets the coupon_pattern of this NewCouponsForMultipleRecipients.  # noqa: E501

        The pattern used to generate coupon codes. The character `#` is a placeholder and is replaced by a random character from the `validCharacters` set.   # noqa: E501

        :return: The coupon_pattern of this NewCouponsForMultipleRecipients.  # noqa: E501
        :rtype: str
        """
        return self._coupon_pattern

    @coupon_pattern.setter
    def coupon_pattern(self, coupon_pattern):
        """Sets the coupon_pattern of this NewCouponsForMultipleRecipients.

        The pattern used to generate coupon codes. The character `#` is a placeholder and is replaced by a random character from the `validCharacters` set.   # noqa: E501

        :param coupon_pattern: The coupon_pattern of this NewCouponsForMultipleRecipients.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                coupon_pattern is not None and len(coupon_pattern) > 100):
            raise ValueError("Invalid value for `coupon_pattern`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                coupon_pattern is not None and len(coupon_pattern) < 3):
            raise ValueError("Invalid value for `coupon_pattern`, length must be greater than or equal to `3`")  # noqa: E501

        self._coupon_pattern = coupon_pattern

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
        if not isinstance(other, NewCouponsForMultipleRecipients):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewCouponsForMultipleRecipients):
            return True

        return self.to_dict() != other.to_dict()
