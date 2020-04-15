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


class NewCoupons(object):
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
        'start_date': 'datetime',
        'expiry_date': 'datetime',
        'valid_characters': 'list[str]',
        'coupon_pattern': 'str',
        'number_of_coupons': 'int',
        'unique_prefix': 'str',
        'attributes': 'object',
        'recipient_integration_id': 'str'
    }

    attribute_map = {
        'usage_limit': 'usageLimit',
        'start_date': 'startDate',
        'expiry_date': 'expiryDate',
        'valid_characters': 'validCharacters',
        'coupon_pattern': 'couponPattern',
        'number_of_coupons': 'numberOfCoupons',
        'unique_prefix': 'uniquePrefix',
        'attributes': 'attributes',
        'recipient_integration_id': 'recipientIntegrationId'
    }

    def __init__(self, usage_limit=None, start_date=None, expiry_date=None, valid_characters=None, coupon_pattern=None, number_of_coupons=None, unique_prefix=None, attributes=None, recipient_integration_id=None, local_vars_configuration=None):  # noqa: E501
        """NewCoupons - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._usage_limit = None
        self._start_date = None
        self._expiry_date = None
        self._valid_characters = None
        self._coupon_pattern = None
        self._number_of_coupons = None
        self._unique_prefix = None
        self._attributes = None
        self._recipient_integration_id = None
        self.discriminator = None

        self.usage_limit = usage_limit
        if start_date is not None:
            self.start_date = start_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        self.valid_characters = valid_characters
        self.coupon_pattern = coupon_pattern
        self.number_of_coupons = number_of_coupons
        if unique_prefix is not None:
            self.unique_prefix = unique_prefix
        if attributes is not None:
            self.attributes = attributes
        if recipient_integration_id is not None:
            self.recipient_integration_id = recipient_integration_id

    @property
    def usage_limit(self):
        """Gets the usage_limit of this NewCoupons.  # noqa: E501

        The number of times a coupon code can be redeemed. This can be set to 0 for no limit, but any campaign usage limits will still apply.   # noqa: E501

        :return: The usage_limit of this NewCoupons.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this NewCoupons.

        The number of times a coupon code can be redeemed. This can be set to 0 for no limit, but any campaign usage limits will still apply.   # noqa: E501

        :param usage_limit: The usage_limit of this NewCoupons.  # noqa: E501
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
    def start_date(self):
        """Gets the start_date of this NewCoupons.  # noqa: E501

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :return: The start_date of this NewCoupons.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this NewCoupons.

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :param start_date: The start_date of this NewCoupons.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this NewCoupons.  # noqa: E501

        Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :return: The expiry_date of this NewCoupons.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this NewCoupons.

        Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :param expiry_date: The expiry_date of this NewCoupons.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def valid_characters(self):
        """Gets the valid_characters of this NewCoupons.  # noqa: E501

        Set of characters to be used when generating random part of code. Defaults to [A-Z, 0-9] (in terms of RegExp).  # noqa: E501

        :return: The valid_characters of this NewCoupons.  # noqa: E501
        :rtype: list[str]
        """
        return self._valid_characters

    @valid_characters.setter
    def valid_characters(self, valid_characters):
        """Sets the valid_characters of this NewCoupons.

        Set of characters to be used when generating random part of code. Defaults to [A-Z, 0-9] (in terms of RegExp).  # noqa: E501

        :param valid_characters: The valid_characters of this NewCoupons.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and valid_characters is None:  # noqa: E501
            raise ValueError("Invalid value for `valid_characters`, must not be `None`")  # noqa: E501

        self._valid_characters = valid_characters

    @property
    def coupon_pattern(self):
        """Gets the coupon_pattern of this NewCoupons.  # noqa: E501

        The pattern that will be used to generate coupon codes. The character `#` acts as a placeholder and will be replaced by a random character from the `validCharacters` set.   # noqa: E501

        :return: The coupon_pattern of this NewCoupons.  # noqa: E501
        :rtype: str
        """
        return self._coupon_pattern

    @coupon_pattern.setter
    def coupon_pattern(self, coupon_pattern):
        """Sets the coupon_pattern of this NewCoupons.

        The pattern that will be used to generate coupon codes. The character `#` acts as a placeholder and will be replaced by a random character from the `validCharacters` set.   # noqa: E501

        :param coupon_pattern: The coupon_pattern of this NewCoupons.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and coupon_pattern is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_pattern`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                coupon_pattern is not None and len(coupon_pattern) < 3):
            raise ValueError("Invalid value for `coupon_pattern`, length must be greater than or equal to `3`")  # noqa: E501

        self._coupon_pattern = coupon_pattern

    @property
    def number_of_coupons(self):
        """Gets the number_of_coupons of this NewCoupons.  # noqa: E501

        The number of new coupon codes to generate for the campaign. Must be at least 1.  # noqa: E501

        :return: The number_of_coupons of this NewCoupons.  # noqa: E501
        :rtype: int
        """
        return self._number_of_coupons

    @number_of_coupons.setter
    def number_of_coupons(self, number_of_coupons):
        """Sets the number_of_coupons of this NewCoupons.

        The number of new coupon codes to generate for the campaign. Must be at least 1.  # noqa: E501

        :param number_of_coupons: The number_of_coupons of this NewCoupons.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_coupons is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_coupons`, must not be `None`")  # noqa: E501

        self._number_of_coupons = number_of_coupons

    @property
    def unique_prefix(self):
        """Gets the unique_prefix of this NewCoupons.  # noqa: E501

        A unique prefix to prepend to all generated coupons.  # noqa: E501

        :return: The unique_prefix of this NewCoupons.  # noqa: E501
        :rtype: str
        """
        return self._unique_prefix

    @unique_prefix.setter
    def unique_prefix(self, unique_prefix):
        """Sets the unique_prefix of this NewCoupons.

        A unique prefix to prepend to all generated coupons.  # noqa: E501

        :param unique_prefix: The unique_prefix of this NewCoupons.  # noqa: E501
        :type: str
        """

        self._unique_prefix = unique_prefix

    @property
    def attributes(self):
        """Gets the attributes of this NewCoupons.  # noqa: E501

        Arbitrary properties associated with this item  # noqa: E501

        :return: The attributes of this NewCoupons.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NewCoupons.

        Arbitrary properties associated with this item  # noqa: E501

        :param attributes: The attributes of this NewCoupons.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def recipient_integration_id(self):
        """Gets the recipient_integration_id of this NewCoupons.  # noqa: E501

        The integration ID for this coupon's beneficiary's profile  # noqa: E501

        :return: The recipient_integration_id of this NewCoupons.  # noqa: E501
        :rtype: str
        """
        return self._recipient_integration_id

    @recipient_integration_id.setter
    def recipient_integration_id(self, recipient_integration_id):
        """Sets the recipient_integration_id of this NewCoupons.

        The integration ID for this coupon's beneficiary's profile  # noqa: E501

        :param recipient_integration_id: The recipient_integration_id of this NewCoupons.  # noqa: E501
        :type: str
        """

        self._recipient_integration_id = recipient_integration_id

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
        if not isinstance(other, NewCoupons):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewCoupons):
            return True

        return self.to_dict() != other.to_dict()
