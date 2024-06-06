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


class UpdateCoupon(object):
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
        'limits': 'list[LimitConfig]',
        'recipient_integration_id': 'str',
        'attributes': 'object',
        'is_reservation_mandatory': 'bool',
        'implicitly_reserved': 'bool'
    }

    attribute_map = {
        'usage_limit': 'usageLimit',
        'discount_limit': 'discountLimit',
        'reservation_limit': 'reservationLimit',
        'start_date': 'startDate',
        'expiry_date': 'expiryDate',
        'limits': 'limits',
        'recipient_integration_id': 'recipientIntegrationId',
        'attributes': 'attributes',
        'is_reservation_mandatory': 'isReservationMandatory',
        'implicitly_reserved': 'implicitlyReserved'
    }

    def __init__(self, usage_limit=None, discount_limit=None, reservation_limit=None, start_date=None, expiry_date=None, limits=None, recipient_integration_id=None, attributes=None, is_reservation_mandatory=False, implicitly_reserved=None, local_vars_configuration=None):  # noqa: E501
        """UpdateCoupon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._usage_limit = None
        self._discount_limit = None
        self._reservation_limit = None
        self._start_date = None
        self._expiry_date = None
        self._limits = None
        self._recipient_integration_id = None
        self._attributes = None
        self._is_reservation_mandatory = None
        self._implicitly_reserved = None
        self.discriminator = None

        if usage_limit is not None:
            self.usage_limit = usage_limit
        if discount_limit is not None:
            self.discount_limit = discount_limit
        if reservation_limit is not None:
            self.reservation_limit = reservation_limit
        if start_date is not None:
            self.start_date = start_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if limits is not None:
            self.limits = limits
        if recipient_integration_id is not None:
            self.recipient_integration_id = recipient_integration_id
        if attributes is not None:
            self.attributes = attributes
        if is_reservation_mandatory is not None:
            self.is_reservation_mandatory = is_reservation_mandatory
        if implicitly_reserved is not None:
            self.implicitly_reserved = implicitly_reserved

    @property
    def usage_limit(self):
        """Gets the usage_limit of this UpdateCoupon.  # noqa: E501

        The number of times the coupon code can be redeemed. `0` means unlimited redemptions but any campaign usage limits will still apply.   # noqa: E501

        :return: The usage_limit of this UpdateCoupon.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this UpdateCoupon.

        The number of times the coupon code can be redeemed. `0` means unlimited redemptions but any campaign usage limits will still apply.   # noqa: E501

        :param usage_limit: The usage_limit of this UpdateCoupon.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                usage_limit is not None and usage_limit > 999999):  # noqa: E501
            raise ValueError("Invalid value for `usage_limit`, must be a value less than or equal to `999999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                usage_limit is not None and usage_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `usage_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._usage_limit = usage_limit

    @property
    def discount_limit(self):
        """Gets the discount_limit of this UpdateCoupon.  # noqa: E501

        The total discount value that the code can give. Typically used to represent a gift card value.   # noqa: E501

        :return: The discount_limit of this UpdateCoupon.  # noqa: E501
        :rtype: float
        """
        return self._discount_limit

    @discount_limit.setter
    def discount_limit(self, discount_limit):
        """Sets the discount_limit of this UpdateCoupon.

        The total discount value that the code can give. Typically used to represent a gift card value.   # noqa: E501

        :param discount_limit: The discount_limit of this UpdateCoupon.  # noqa: E501
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
        """Gets the reservation_limit of this UpdateCoupon.  # noqa: E501

        The number of reservations that can be made with this coupon code.   # noqa: E501

        :return: The reservation_limit of this UpdateCoupon.  # noqa: E501
        :rtype: int
        """
        return self._reservation_limit

    @reservation_limit.setter
    def reservation_limit(self, reservation_limit):
        """Sets the reservation_limit of this UpdateCoupon.

        The number of reservations that can be made with this coupon code.   # noqa: E501

        :param reservation_limit: The reservation_limit of this UpdateCoupon.  # noqa: E501
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
        """Gets the start_date of this UpdateCoupon.  # noqa: E501

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :return: The start_date of this UpdateCoupon.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this UpdateCoupon.

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :param start_date: The start_date of this UpdateCoupon.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this UpdateCoupon.  # noqa: E501

        Expiration date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :return: The expiry_date of this UpdateCoupon.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this UpdateCoupon.

        Expiration date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :param expiry_date: The expiry_date of this UpdateCoupon.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def limits(self):
        """Gets the limits of this UpdateCoupon.  # noqa: E501

        Limits configuration for a coupon. These limits will override the limits set from the campaign.  **Note:** Only usable when creating a single coupon which is not tied to a specific recipient. Only per-profile limits are allowed to be configured.   # noqa: E501

        :return: The limits of this UpdateCoupon.  # noqa: E501
        :rtype: list[LimitConfig]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this UpdateCoupon.

        Limits configuration for a coupon. These limits will override the limits set from the campaign.  **Note:** Only usable when creating a single coupon which is not tied to a specific recipient. Only per-profile limits are allowed to be configured.   # noqa: E501

        :param limits: The limits of this UpdateCoupon.  # noqa: E501
        :type: list[LimitConfig]
        """

        self._limits = limits

    @property
    def recipient_integration_id(self):
        """Gets the recipient_integration_id of this UpdateCoupon.  # noqa: E501

        The integration ID for this coupon's beneficiary's profile.  # noqa: E501

        :return: The recipient_integration_id of this UpdateCoupon.  # noqa: E501
        :rtype: str
        """
        return self._recipient_integration_id

    @recipient_integration_id.setter
    def recipient_integration_id(self, recipient_integration_id):
        """Sets the recipient_integration_id of this UpdateCoupon.

        The integration ID for this coupon's beneficiary's profile.  # noqa: E501

        :param recipient_integration_id: The recipient_integration_id of this UpdateCoupon.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                recipient_integration_id is not None and len(recipient_integration_id) > 1000):
            raise ValueError("Invalid value for `recipient_integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._recipient_integration_id = recipient_integration_id

    @property
    def attributes(self):
        """Gets the attributes of this UpdateCoupon.  # noqa: E501

        Arbitrary properties associated with this item.  # noqa: E501

        :return: The attributes of this UpdateCoupon.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this UpdateCoupon.

        Arbitrary properties associated with this item.  # noqa: E501

        :param attributes: The attributes of this UpdateCoupon.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def is_reservation_mandatory(self):
        """Gets the is_reservation_mandatory of this UpdateCoupon.  # noqa: E501

        An indication of whether the code can be redeemed only if it has been reserved first.  # noqa: E501

        :return: The is_reservation_mandatory of this UpdateCoupon.  # noqa: E501
        :rtype: bool
        """
        return self._is_reservation_mandatory

    @is_reservation_mandatory.setter
    def is_reservation_mandatory(self, is_reservation_mandatory):
        """Sets the is_reservation_mandatory of this UpdateCoupon.

        An indication of whether the code can be redeemed only if it has been reserved first.  # noqa: E501

        :param is_reservation_mandatory: The is_reservation_mandatory of this UpdateCoupon.  # noqa: E501
        :type: bool
        """

        self._is_reservation_mandatory = is_reservation_mandatory

    @property
    def implicitly_reserved(self):
        """Gets the implicitly_reserved of this UpdateCoupon.  # noqa: E501

        An indication of whether the coupon is implicitly reserved for all customers.  # noqa: E501

        :return: The implicitly_reserved of this UpdateCoupon.  # noqa: E501
        :rtype: bool
        """
        return self._implicitly_reserved

    @implicitly_reserved.setter
    def implicitly_reserved(self, implicitly_reserved):
        """Sets the implicitly_reserved of this UpdateCoupon.

        An indication of whether the coupon is implicitly reserved for all customers.  # noqa: E501

        :param implicitly_reserved: The implicitly_reserved of this UpdateCoupon.  # noqa: E501
        :type: bool
        """

        self._implicitly_reserved = implicitly_reserved

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
        if not isinstance(other, UpdateCoupon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateCoupon):
            return True

        return self.to_dict() != other.to_dict()
