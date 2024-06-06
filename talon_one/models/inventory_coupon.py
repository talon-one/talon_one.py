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


class InventoryCoupon(object):
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
        'created': 'datetime',
        'campaign_id': 'int',
        'value': 'str',
        'usage_limit': 'int',
        'discount_limit': 'float',
        'reservation_limit': 'int',
        'start_date': 'datetime',
        'expiry_date': 'datetime',
        'limits': 'list[LimitConfig]',
        'usage_counter': 'int',
        'discount_counter': 'float',
        'discount_remainder': 'float',
        'reservation_counter': 'float',
        'attributes': 'object',
        'referral_id': 'int',
        'recipient_integration_id': 'str',
        'import_id': 'int',
        'reservation': 'bool',
        'batch_id': 'str',
        'is_reservation_mandatory': 'bool',
        'implicitly_reserved': 'bool',
        'profile_redemption_count': 'int',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'campaign_id': 'campaignId',
        'value': 'value',
        'usage_limit': 'usageLimit',
        'discount_limit': 'discountLimit',
        'reservation_limit': 'reservationLimit',
        'start_date': 'startDate',
        'expiry_date': 'expiryDate',
        'limits': 'limits',
        'usage_counter': 'usageCounter',
        'discount_counter': 'discountCounter',
        'discount_remainder': 'discountRemainder',
        'reservation_counter': 'reservationCounter',
        'attributes': 'attributes',
        'referral_id': 'referralId',
        'recipient_integration_id': 'recipientIntegrationId',
        'import_id': 'importId',
        'reservation': 'reservation',
        'batch_id': 'batchId',
        'is_reservation_mandatory': 'isReservationMandatory',
        'implicitly_reserved': 'implicitlyReserved',
        'profile_redemption_count': 'profileRedemptionCount',
        'state': 'state'
    }

    def __init__(self, id=None, created=None, campaign_id=None, value=None, usage_limit=None, discount_limit=None, reservation_limit=None, start_date=None, expiry_date=None, limits=None, usage_counter=None, discount_counter=None, discount_remainder=None, reservation_counter=None, attributes=None, referral_id=None, recipient_integration_id=None, import_id=None, reservation=True, batch_id=None, is_reservation_mandatory=False, implicitly_reserved=None, profile_redemption_count=None, state=None, local_vars_configuration=None):  # noqa: E501
        """InventoryCoupon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._campaign_id = None
        self._value = None
        self._usage_limit = None
        self._discount_limit = None
        self._reservation_limit = None
        self._start_date = None
        self._expiry_date = None
        self._limits = None
        self._usage_counter = None
        self._discount_counter = None
        self._discount_remainder = None
        self._reservation_counter = None
        self._attributes = None
        self._referral_id = None
        self._recipient_integration_id = None
        self._import_id = None
        self._reservation = None
        self._batch_id = None
        self._is_reservation_mandatory = None
        self._implicitly_reserved = None
        self._profile_redemption_count = None
        self._state = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.campaign_id = campaign_id
        self.value = value
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
        self.usage_counter = usage_counter
        if discount_counter is not None:
            self.discount_counter = discount_counter
        if discount_remainder is not None:
            self.discount_remainder = discount_remainder
        if reservation_counter is not None:
            self.reservation_counter = reservation_counter
        if attributes is not None:
            self.attributes = attributes
        if referral_id is not None:
            self.referral_id = referral_id
        if recipient_integration_id is not None:
            self.recipient_integration_id = recipient_integration_id
        if import_id is not None:
            self.import_id = import_id
        if reservation is not None:
            self.reservation = reservation
        if batch_id is not None:
            self.batch_id = batch_id
        if is_reservation_mandatory is not None:
            self.is_reservation_mandatory = is_reservation_mandatory
        if implicitly_reserved is not None:
            self.implicitly_reserved = implicitly_reserved
        self.profile_redemption_count = profile_redemption_count
        self.state = state

    @property
    def id(self):
        """Gets the id of this InventoryCoupon.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this InventoryCoupon.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryCoupon.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this InventoryCoupon.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this InventoryCoupon.  # noqa: E501

        The time this entity was created.  # noqa: E501

        :return: The created of this InventoryCoupon.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this InventoryCoupon.

        The time this entity was created.  # noqa: E501

        :param created: The created of this InventoryCoupon.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def campaign_id(self):
        """Gets the campaign_id of this InventoryCoupon.  # noqa: E501

        The ID of the campaign that owns this entity.  # noqa: E501

        :return: The campaign_id of this InventoryCoupon.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this InventoryCoupon.

        The ID of the campaign that owns this entity.  # noqa: E501

        :param campaign_id: The campaign_id of this InventoryCoupon.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def value(self):
        """Gets the value of this InventoryCoupon.  # noqa: E501

        The coupon code.  # noqa: E501

        :return: The value of this InventoryCoupon.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this InventoryCoupon.

        The coupon code.  # noqa: E501

        :param value: The value of this InventoryCoupon.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) < 4):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `4`")  # noqa: E501

        self._value = value

    @property
    def usage_limit(self):
        """Gets the usage_limit of this InventoryCoupon.  # noqa: E501

        The number of times the coupon code can be redeemed. `0` means unlimited redemptions but any campaign usage limits will still apply.   # noqa: E501

        :return: The usage_limit of this InventoryCoupon.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this InventoryCoupon.

        The number of times the coupon code can be redeemed. `0` means unlimited redemptions but any campaign usage limits will still apply.   # noqa: E501

        :param usage_limit: The usage_limit of this InventoryCoupon.  # noqa: E501
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
        """Gets the discount_limit of this InventoryCoupon.  # noqa: E501

        The total discount value that the code can give. Typically used to represent a gift card value.   # noqa: E501

        :return: The discount_limit of this InventoryCoupon.  # noqa: E501
        :rtype: float
        """
        return self._discount_limit

    @discount_limit.setter
    def discount_limit(self, discount_limit):
        """Sets the discount_limit of this InventoryCoupon.

        The total discount value that the code can give. Typically used to represent a gift card value.   # noqa: E501

        :param discount_limit: The discount_limit of this InventoryCoupon.  # noqa: E501
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
        """Gets the reservation_limit of this InventoryCoupon.  # noqa: E501

        The number of reservations that can be made with this coupon code.   # noqa: E501

        :return: The reservation_limit of this InventoryCoupon.  # noqa: E501
        :rtype: int
        """
        return self._reservation_limit

    @reservation_limit.setter
    def reservation_limit(self, reservation_limit):
        """Sets the reservation_limit of this InventoryCoupon.

        The number of reservations that can be made with this coupon code.   # noqa: E501

        :param reservation_limit: The reservation_limit of this InventoryCoupon.  # noqa: E501
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
        """Gets the start_date of this InventoryCoupon.  # noqa: E501

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :return: The start_date of this InventoryCoupon.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InventoryCoupon.

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :param start_date: The start_date of this InventoryCoupon.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this InventoryCoupon.  # noqa: E501

        Expiration date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :return: The expiry_date of this InventoryCoupon.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this InventoryCoupon.

        Expiration date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :param expiry_date: The expiry_date of this InventoryCoupon.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def limits(self):
        """Gets the limits of this InventoryCoupon.  # noqa: E501

        Limits configuration for a coupon. These limits will override the limits set from the campaign.  **Note:** Only usable when creating a single coupon which is not tied to a specific recipient. Only per-profile limits are allowed to be configured.   # noqa: E501

        :return: The limits of this InventoryCoupon.  # noqa: E501
        :rtype: list[LimitConfig]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this InventoryCoupon.

        Limits configuration for a coupon. These limits will override the limits set from the campaign.  **Note:** Only usable when creating a single coupon which is not tied to a specific recipient. Only per-profile limits are allowed to be configured.   # noqa: E501

        :param limits: The limits of this InventoryCoupon.  # noqa: E501
        :type: list[LimitConfig]
        """

        self._limits = limits

    @property
    def usage_counter(self):
        """Gets the usage_counter of this InventoryCoupon.  # noqa: E501

        The number of times the coupon has been successfully redeemed.  # noqa: E501

        :return: The usage_counter of this InventoryCoupon.  # noqa: E501
        :rtype: int
        """
        return self._usage_counter

    @usage_counter.setter
    def usage_counter(self, usage_counter):
        """Sets the usage_counter of this InventoryCoupon.

        The number of times the coupon has been successfully redeemed.  # noqa: E501

        :param usage_counter: The usage_counter of this InventoryCoupon.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and usage_counter is None:  # noqa: E501
            raise ValueError("Invalid value for `usage_counter`, must not be `None`")  # noqa: E501

        self._usage_counter = usage_counter

    @property
    def discount_counter(self):
        """Gets the discount_counter of this InventoryCoupon.  # noqa: E501

        The amount of discounts given on rules redeeming this coupon. Only usable if a coupon discount budget was set for this coupon.  # noqa: E501

        :return: The discount_counter of this InventoryCoupon.  # noqa: E501
        :rtype: float
        """
        return self._discount_counter

    @discount_counter.setter
    def discount_counter(self, discount_counter):
        """Sets the discount_counter of this InventoryCoupon.

        The amount of discounts given on rules redeeming this coupon. Only usable if a coupon discount budget was set for this coupon.  # noqa: E501

        :param discount_counter: The discount_counter of this InventoryCoupon.  # noqa: E501
        :type: float
        """

        self._discount_counter = discount_counter

    @property
    def discount_remainder(self):
        """Gets the discount_remainder of this InventoryCoupon.  # noqa: E501

        The remaining discount this coupon can give.  # noqa: E501

        :return: The discount_remainder of this InventoryCoupon.  # noqa: E501
        :rtype: float
        """
        return self._discount_remainder

    @discount_remainder.setter
    def discount_remainder(self, discount_remainder):
        """Sets the discount_remainder of this InventoryCoupon.

        The remaining discount this coupon can give.  # noqa: E501

        :param discount_remainder: The discount_remainder of this InventoryCoupon.  # noqa: E501
        :type: float
        """

        self._discount_remainder = discount_remainder

    @property
    def reservation_counter(self):
        """Gets the reservation_counter of this InventoryCoupon.  # noqa: E501

        The number of times this coupon has been reserved.  # noqa: E501

        :return: The reservation_counter of this InventoryCoupon.  # noqa: E501
        :rtype: float
        """
        return self._reservation_counter

    @reservation_counter.setter
    def reservation_counter(self, reservation_counter):
        """Sets the reservation_counter of this InventoryCoupon.

        The number of times this coupon has been reserved.  # noqa: E501

        :param reservation_counter: The reservation_counter of this InventoryCoupon.  # noqa: E501
        :type: float
        """

        self._reservation_counter = reservation_counter

    @property
    def attributes(self):
        """Gets the attributes of this InventoryCoupon.  # noqa: E501

        Custom attributes associated with this coupon.  # noqa: E501

        :return: The attributes of this InventoryCoupon.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InventoryCoupon.

        Custom attributes associated with this coupon.  # noqa: E501

        :param attributes: The attributes of this InventoryCoupon.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def referral_id(self):
        """Gets the referral_id of this InventoryCoupon.  # noqa: E501

        The integration ID of the referring customer (if any) for whom this coupon was created as an effect.  # noqa: E501

        :return: The referral_id of this InventoryCoupon.  # noqa: E501
        :rtype: int
        """
        return self._referral_id

    @referral_id.setter
    def referral_id(self, referral_id):
        """Sets the referral_id of this InventoryCoupon.

        The integration ID of the referring customer (if any) for whom this coupon was created as an effect.  # noqa: E501

        :param referral_id: The referral_id of this InventoryCoupon.  # noqa: E501
        :type: int
        """

        self._referral_id = referral_id

    @property
    def recipient_integration_id(self):
        """Gets the recipient_integration_id of this InventoryCoupon.  # noqa: E501

        The Integration ID of the customer that is allowed to redeem this coupon.  # noqa: E501

        :return: The recipient_integration_id of this InventoryCoupon.  # noqa: E501
        :rtype: str
        """
        return self._recipient_integration_id

    @recipient_integration_id.setter
    def recipient_integration_id(self, recipient_integration_id):
        """Sets the recipient_integration_id of this InventoryCoupon.

        The Integration ID of the customer that is allowed to redeem this coupon.  # noqa: E501

        :param recipient_integration_id: The recipient_integration_id of this InventoryCoupon.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                recipient_integration_id is not None and len(recipient_integration_id) > 1000):
            raise ValueError("Invalid value for `recipient_integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._recipient_integration_id = recipient_integration_id

    @property
    def import_id(self):
        """Gets the import_id of this InventoryCoupon.  # noqa: E501

        The ID of the Import which created this coupon.  # noqa: E501

        :return: The import_id of this InventoryCoupon.  # noqa: E501
        :rtype: int
        """
        return self._import_id

    @import_id.setter
    def import_id(self, import_id):
        """Sets the import_id of this InventoryCoupon.

        The ID of the Import which created this coupon.  # noqa: E501

        :param import_id: The import_id of this InventoryCoupon.  # noqa: E501
        :type: int
        """

        self._import_id = import_id

    @property
    def reservation(self):
        """Gets the reservation of this InventoryCoupon.  # noqa: E501

        Defines the reservation type: - `true`: The coupon can be reserved for multiple customers. - `false`: The coupon can be reserved only for one customer. It is a personal code.   # noqa: E501

        :return: The reservation of this InventoryCoupon.  # noqa: E501
        :rtype: bool
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this InventoryCoupon.

        Defines the reservation type: - `true`: The coupon can be reserved for multiple customers. - `false`: The coupon can be reserved only for one customer. It is a personal code.   # noqa: E501

        :param reservation: The reservation of this InventoryCoupon.  # noqa: E501
        :type: bool
        """

        self._reservation = reservation

    @property
    def batch_id(self):
        """Gets the batch_id of this InventoryCoupon.  # noqa: E501

        The id of the batch the coupon belongs to.  # noqa: E501

        :return: The batch_id of this InventoryCoupon.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this InventoryCoupon.

        The id of the batch the coupon belongs to.  # noqa: E501

        :param batch_id: The batch_id of this InventoryCoupon.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def is_reservation_mandatory(self):
        """Gets the is_reservation_mandatory of this InventoryCoupon.  # noqa: E501

        An indication of whether the code can be redeemed only if it has been reserved first.  # noqa: E501

        :return: The is_reservation_mandatory of this InventoryCoupon.  # noqa: E501
        :rtype: bool
        """
        return self._is_reservation_mandatory

    @is_reservation_mandatory.setter
    def is_reservation_mandatory(self, is_reservation_mandatory):
        """Sets the is_reservation_mandatory of this InventoryCoupon.

        An indication of whether the code can be redeemed only if it has been reserved first.  # noqa: E501

        :param is_reservation_mandatory: The is_reservation_mandatory of this InventoryCoupon.  # noqa: E501
        :type: bool
        """

        self._is_reservation_mandatory = is_reservation_mandatory

    @property
    def implicitly_reserved(self):
        """Gets the implicitly_reserved of this InventoryCoupon.  # noqa: E501

        An indication of whether the coupon is implicitly reserved for all customers.  # noqa: E501

        :return: The implicitly_reserved of this InventoryCoupon.  # noqa: E501
        :rtype: bool
        """
        return self._implicitly_reserved

    @implicitly_reserved.setter
    def implicitly_reserved(self, implicitly_reserved):
        """Sets the implicitly_reserved of this InventoryCoupon.

        An indication of whether the coupon is implicitly reserved for all customers.  # noqa: E501

        :param implicitly_reserved: The implicitly_reserved of this InventoryCoupon.  # noqa: E501
        :type: bool
        """

        self._implicitly_reserved = implicitly_reserved

    @property
    def profile_redemption_count(self):
        """Gets the profile_redemption_count of this InventoryCoupon.  # noqa: E501

        The number of times the coupon was redeemed by the profile.  # noqa: E501

        :return: The profile_redemption_count of this InventoryCoupon.  # noqa: E501
        :rtype: int
        """
        return self._profile_redemption_count

    @profile_redemption_count.setter
    def profile_redemption_count(self, profile_redemption_count):
        """Sets the profile_redemption_count of this InventoryCoupon.

        The number of times the coupon was redeemed by the profile.  # noqa: E501

        :param profile_redemption_count: The profile_redemption_count of this InventoryCoupon.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and profile_redemption_count is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_redemption_count`, must not be `None`")  # noqa: E501

        self._profile_redemption_count = profile_redemption_count

    @property
    def state(self):
        """Gets the state of this InventoryCoupon.  # noqa: E501

        Can be:  - `active`: The coupon can be used. It is a reserved coupon that is not pending, used, or expired, and it has a non-exhausted limit counter.    **Note:** This coupon state is returned for [scheduled campaigns](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-schedule), but the coupon cannot be used until the campaign is **running**. - `used`: The coupon has been redeemed and cannot be used again. It is not pending and has reached its redemption limit or was redeemed by the profile before expiration. - `expired`: The coupon was never redeemed, and it is now expired. It is non-pending, non-active, and non-used by the profile. - `pending`: The coupon will be usable in the future. - `disabled`: The coupon is part of a non-active campaign.   # noqa: E501

        :return: The state of this InventoryCoupon.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InventoryCoupon.

        Can be:  - `active`: The coupon can be used. It is a reserved coupon that is not pending, used, or expired, and it has a non-exhausted limit counter.    **Note:** This coupon state is returned for [scheduled campaigns](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-schedule), but the coupon cannot be used until the campaign is **running**. - `used`: The coupon has been redeemed and cannot be used again. It is not pending and has reached its redemption limit or was redeemed by the profile before expiration. - `expired`: The coupon was never redeemed, and it is now expired. It is non-pending, non-active, and non-used by the profile. - `pending`: The coupon will be usable in the future. - `disabled`: The coupon is part of a non-active campaign.   # noqa: E501

        :param state: The state of this InventoryCoupon.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

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
        if not isinstance(other, InventoryCoupon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InventoryCoupon):
            return True

        return self.to_dict() != other.to_dict()
