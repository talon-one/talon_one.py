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


class Coupon(object):
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
        'start_date': 'datetime',
        'expiry_date': 'datetime',
        'usage_counter': 'int',
        'discount_counter': 'float',
        'discount_remainder': 'float',
        'attributes': 'object',
        'referral_id': 'int',
        'recipient_integration_id': 'str',
        'import_id': 'int',
        'reservation': 'bool',
        'batch_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'campaign_id': 'campaignId',
        'value': 'value',
        'usage_limit': 'usageLimit',
        'discount_limit': 'discountLimit',
        'start_date': 'startDate',
        'expiry_date': 'expiryDate',
        'usage_counter': 'usageCounter',
        'discount_counter': 'discountCounter',
        'discount_remainder': 'discountRemainder',
        'attributes': 'attributes',
        'referral_id': 'referralId',
        'recipient_integration_id': 'recipientIntegrationId',
        'import_id': 'importId',
        'reservation': 'reservation',
        'batch_id': 'batchId'
    }

    def __init__(self, id=None, created=None, campaign_id=None, value=None, usage_limit=None, discount_limit=None, start_date=None, expiry_date=None, usage_counter=None, discount_counter=None, discount_remainder=None, attributes=None, referral_id=None, recipient_integration_id=None, import_id=None, reservation=None, batch_id=None, local_vars_configuration=None):  # noqa: E501
        """Coupon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._campaign_id = None
        self._value = None
        self._usage_limit = None
        self._discount_limit = None
        self._start_date = None
        self._expiry_date = None
        self._usage_counter = None
        self._discount_counter = None
        self._discount_remainder = None
        self._attributes = None
        self._referral_id = None
        self._recipient_integration_id = None
        self._import_id = None
        self._reservation = None
        self._batch_id = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.campaign_id = campaign_id
        self.value = value
        self.usage_limit = usage_limit
        if discount_limit is not None:
            self.discount_limit = discount_limit
        if start_date is not None:
            self.start_date = start_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        self.usage_counter = usage_counter
        if discount_counter is not None:
            self.discount_counter = discount_counter
        if discount_remainder is not None:
            self.discount_remainder = discount_remainder
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

    @property
    def id(self):
        """Gets the id of this Coupon.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Coupon.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this Coupon.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Coupon.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this Coupon.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Coupon.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this Coupon.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def campaign_id(self):
        """Gets the campaign_id of this Coupon.  # noqa: E501

        The ID of the campaign that owns this entity.  # noqa: E501

        :return: The campaign_id of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this Coupon.

        The ID of the campaign that owns this entity.  # noqa: E501

        :param campaign_id: The campaign_id of this Coupon.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def value(self):
        """Gets the value of this Coupon.  # noqa: E501

        The actual coupon code.  # noqa: E501

        :return: The value of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Coupon.

        The actual coupon code.  # noqa: E501

        :param value: The value of this Coupon.  # noqa: E501
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
        """Gets the usage_limit of this Coupon.  # noqa: E501

        The number of times a coupon code can be redeemed. This can be set to 0 for no limit, but any campaign usage limits will still apply.   # noqa: E501

        :return: The usage_limit of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this Coupon.

        The number of times a coupon code can be redeemed. This can be set to 0 for no limit, but any campaign usage limits will still apply.   # noqa: E501

        :param usage_limit: The usage_limit of this Coupon.  # noqa: E501
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
        """Gets the discount_limit of this Coupon.  # noqa: E501

        The amount of discounts that can be given with this coupon code.   # noqa: E501

        :return: The discount_limit of this Coupon.  # noqa: E501
        :rtype: float
        """
        return self._discount_limit

    @discount_limit.setter
    def discount_limit(self, discount_limit):
        """Sets the discount_limit of this Coupon.

        The amount of discounts that can be given with this coupon code.   # noqa: E501

        :param discount_limit: The discount_limit of this Coupon.  # noqa: E501
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
    def start_date(self):
        """Gets the start_date of this Coupon.  # noqa: E501

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :return: The start_date of this Coupon.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Coupon.

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :param start_date: The start_date of this Coupon.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this Coupon.  # noqa: E501

        Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :return: The expiry_date of this Coupon.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this Coupon.

        Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :param expiry_date: The expiry_date of this Coupon.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def usage_counter(self):
        """Gets the usage_counter of this Coupon.  # noqa: E501

        The number of times this coupon has been successfully used.  # noqa: E501

        :return: The usage_counter of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._usage_counter

    @usage_counter.setter
    def usage_counter(self, usage_counter):
        """Sets the usage_counter of this Coupon.

        The number of times this coupon has been successfully used.  # noqa: E501

        :param usage_counter: The usage_counter of this Coupon.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and usage_counter is None:  # noqa: E501
            raise ValueError("Invalid value for `usage_counter`, must not be `None`")  # noqa: E501

        self._usage_counter = usage_counter

    @property
    def discount_counter(self):
        """Gets the discount_counter of this Coupon.  # noqa: E501

        The amount of discounts given on rules redeeming this coupon. Only usable if a coupon discount budget was set for this coupon.  # noqa: E501

        :return: The discount_counter of this Coupon.  # noqa: E501
        :rtype: float
        """
        return self._discount_counter

    @discount_counter.setter
    def discount_counter(self, discount_counter):
        """Sets the discount_counter of this Coupon.

        The amount of discounts given on rules redeeming this coupon. Only usable if a coupon discount budget was set for this coupon.  # noqa: E501

        :param discount_counter: The discount_counter of this Coupon.  # noqa: E501
        :type: float
        """

        self._discount_counter = discount_counter

    @property
    def discount_remainder(self):
        """Gets the discount_remainder of this Coupon.  # noqa: E501

        The remaining discount this coupon can give.  # noqa: E501

        :return: The discount_remainder of this Coupon.  # noqa: E501
        :rtype: float
        """
        return self._discount_remainder

    @discount_remainder.setter
    def discount_remainder(self, discount_remainder):
        """Sets the discount_remainder of this Coupon.

        The remaining discount this coupon can give.  # noqa: E501

        :param discount_remainder: The discount_remainder of this Coupon.  # noqa: E501
        :type: float
        """

        self._discount_remainder = discount_remainder

    @property
    def attributes(self):
        """Gets the attributes of this Coupon.  # noqa: E501

        Arbitrary properties associated with this item  # noqa: E501

        :return: The attributes of this Coupon.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Coupon.

        Arbitrary properties associated with this item  # noqa: E501

        :param attributes: The attributes of this Coupon.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def referral_id(self):
        """Gets the referral_id of this Coupon.  # noqa: E501

        The integration ID of the referring customer (if any) for whom this coupon was created as an effect.  # noqa: E501

        :return: The referral_id of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._referral_id

    @referral_id.setter
    def referral_id(self, referral_id):
        """Sets the referral_id of this Coupon.

        The integration ID of the referring customer (if any) for whom this coupon was created as an effect.  # noqa: E501

        :param referral_id: The referral_id of this Coupon.  # noqa: E501
        :type: int
        """

        self._referral_id = referral_id

    @property
    def recipient_integration_id(self):
        """Gets the recipient_integration_id of this Coupon.  # noqa: E501

        The Integration ID of the customer that is allowed to redeem this coupon.  # noqa: E501

        :return: The recipient_integration_id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._recipient_integration_id

    @recipient_integration_id.setter
    def recipient_integration_id(self, recipient_integration_id):
        """Sets the recipient_integration_id of this Coupon.

        The Integration ID of the customer that is allowed to redeem this coupon.  # noqa: E501

        :param recipient_integration_id: The recipient_integration_id of this Coupon.  # noqa: E501
        :type: str
        """

        self._recipient_integration_id = recipient_integration_id

    @property
    def import_id(self):
        """Gets the import_id of this Coupon.  # noqa: E501

        The ID of the Import which created this coupon.  # noqa: E501

        :return: The import_id of this Coupon.  # noqa: E501
        :rtype: int
        """
        return self._import_id

    @import_id.setter
    def import_id(self, import_id):
        """Sets the import_id of this Coupon.

        The ID of the Import which created this coupon.  # noqa: E501

        :param import_id: The import_id of this Coupon.  # noqa: E501
        :type: int
        """

        self._import_id = import_id

    @property
    def reservation(self):
        """Gets the reservation of this Coupon.  # noqa: E501

        This value controls what reservations mean to a coupon. If set to true the coupon reservation is used to mark it as a favourite, if set to false the coupon reservation is used as a requirement of usage. This value defaults to true if not specified.  # noqa: E501

        :return: The reservation of this Coupon.  # noqa: E501
        :rtype: bool
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this Coupon.

        This value controls what reservations mean to a coupon. If set to true the coupon reservation is used to mark it as a favourite, if set to false the coupon reservation is used as a requirement of usage. This value defaults to true if not specified.  # noqa: E501

        :param reservation: The reservation of this Coupon.  # noqa: E501
        :type: bool
        """

        self._reservation = reservation

    @property
    def batch_id(self):
        """Gets the batch_id of this Coupon.  # noqa: E501

        The id of the batch the coupon belongs to.  # noqa: E501

        :return: The batch_id of this Coupon.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this Coupon.

        The id of the batch the coupon belongs to.  # noqa: E501

        :param batch_id: The batch_id of this Coupon.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

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
        if not isinstance(other, Coupon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Coupon):
            return True

        return self.to_dict() != other.to_dict()
