# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class CouponCreationJob(object):
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
        'application_id': 'int',
        'account_id': 'int',
        'usage_limit': 'int',
        'discount_limit': 'float',
        'start_date': 'datetime',
        'expiry_date': 'datetime',
        'number_of_coupons': 'int',
        'coupon_settings': 'CodeGeneratorSettings',
        'attributes': 'object',
        'batch_id': 'str',
        'status': 'str',
        'created_amount': 'int',
        'fail_count': 'int',
        'errors': 'list[str]',
        'created_by': 'int',
        'communicated': 'bool',
        'chunk_execution_count': 'int',
        'chunk_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'campaign_id': 'campaignId',
        'application_id': 'applicationId',
        'account_id': 'accountId',
        'usage_limit': 'usageLimit',
        'discount_limit': 'discountLimit',
        'start_date': 'startDate',
        'expiry_date': 'expiryDate',
        'number_of_coupons': 'numberOfCoupons',
        'coupon_settings': 'couponSettings',
        'attributes': 'attributes',
        'batch_id': 'batchId',
        'status': 'status',
        'created_amount': 'createdAmount',
        'fail_count': 'failCount',
        'errors': 'errors',
        'created_by': 'createdBy',
        'communicated': 'communicated',
        'chunk_execution_count': 'chunkExecutionCount',
        'chunk_size': 'chunkSize'
    }

    def __init__(self, id=None, created=None, campaign_id=None, application_id=None, account_id=None, usage_limit=None, discount_limit=None, start_date=None, expiry_date=None, number_of_coupons=None, coupon_settings=None, attributes=None, batch_id=None, status=None, created_amount=None, fail_count=None, errors=None, created_by=None, communicated=None, chunk_execution_count=None, chunk_size=None, local_vars_configuration=None):  # noqa: E501
        """CouponCreationJob - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._campaign_id = None
        self._application_id = None
        self._account_id = None
        self._usage_limit = None
        self._discount_limit = None
        self._start_date = None
        self._expiry_date = None
        self._number_of_coupons = None
        self._coupon_settings = None
        self._attributes = None
        self._batch_id = None
        self._status = None
        self._created_amount = None
        self._fail_count = None
        self._errors = None
        self._created_by = None
        self._communicated = None
        self._chunk_execution_count = None
        self._chunk_size = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.campaign_id = campaign_id
        self.application_id = application_id
        self.account_id = account_id
        self.usage_limit = usage_limit
        if discount_limit is not None:
            self.discount_limit = discount_limit
        if start_date is not None:
            self.start_date = start_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        self.number_of_coupons = number_of_coupons
        if coupon_settings is not None:
            self.coupon_settings = coupon_settings
        self.attributes = attributes
        self.batch_id = batch_id
        self.status = status
        self.created_amount = created_amount
        self.fail_count = fail_count
        self.errors = errors
        self.created_by = created_by
        self.communicated = communicated
        self.chunk_execution_count = chunk_execution_count
        if chunk_size is not None:
            self.chunk_size = chunk_size

    @property
    def id(self):
        """Gets the id of this CouponCreationJob.  # noqa: E501

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :return: The id of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CouponCreationJob.

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :param id: The id of this CouponCreationJob.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this CouponCreationJob.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this CouponCreationJob.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CouponCreationJob.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this CouponCreationJob.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def campaign_id(self):
        """Gets the campaign_id of this CouponCreationJob.  # noqa: E501

        The ID of the campaign that owns this entity.  # noqa: E501

        :return: The campaign_id of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this CouponCreationJob.

        The ID of the campaign that owns this entity.  # noqa: E501

        :param campaign_id: The campaign_id of this CouponCreationJob.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def application_id(self):
        """Gets the application_id of this CouponCreationJob.  # noqa: E501

        The ID of the application that owns this entity.  # noqa: E501

        :return: The application_id of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this CouponCreationJob.

        The ID of the application that owns this entity.  # noqa: E501

        :param application_id: The application_id of this CouponCreationJob.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def account_id(self):
        """Gets the account_id of this CouponCreationJob.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CouponCreationJob.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this CouponCreationJob.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def usage_limit(self):
        """Gets the usage_limit of this CouponCreationJob.  # noqa: E501

        The number of times the coupon code can be redeemed. `0` means unlimited redemptions but any campaign usage limits will still apply.   # noqa: E501

        :return: The usage_limit of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this CouponCreationJob.

        The number of times the coupon code can be redeemed. `0` means unlimited redemptions but any campaign usage limits will still apply.   # noqa: E501

        :param usage_limit: The usage_limit of this CouponCreationJob.  # noqa: E501
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
        """Gets the discount_limit of this CouponCreationJob.  # noqa: E501

        The amount of discounts that can be given with this coupon code.   # noqa: E501

        :return: The discount_limit of this CouponCreationJob.  # noqa: E501
        :rtype: float
        """
        return self._discount_limit

    @discount_limit.setter
    def discount_limit(self, discount_limit):
        """Sets the discount_limit of this CouponCreationJob.

        The amount of discounts that can be given with this coupon code.   # noqa: E501

        :param discount_limit: The discount_limit of this CouponCreationJob.  # noqa: E501
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
        """Gets the start_date of this CouponCreationJob.  # noqa: E501

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :return: The start_date of this CouponCreationJob.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CouponCreationJob.

        Timestamp at which point the coupon becomes valid.  # noqa: E501

        :param start_date: The start_date of this CouponCreationJob.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this CouponCreationJob.  # noqa: E501

        Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :return: The expiry_date of this CouponCreationJob.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this CouponCreationJob.

        Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative.  # noqa: E501

        :param expiry_date: The expiry_date of this CouponCreationJob.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def number_of_coupons(self):
        """Gets the number_of_coupons of this CouponCreationJob.  # noqa: E501

        The number of new coupon codes to generate for the campaign. Must be between 20,001 and 5,000,000.  # noqa: E501

        :return: The number_of_coupons of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._number_of_coupons

    @number_of_coupons.setter
    def number_of_coupons(self, number_of_coupons):
        """Sets the number_of_coupons of this CouponCreationJob.

        The number of new coupon codes to generate for the campaign. Must be between 20,001 and 5,000,000.  # noqa: E501

        :param number_of_coupons: The number_of_coupons of this CouponCreationJob.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_coupons is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_coupons`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_coupons is not None and number_of_coupons > 5000000):  # noqa: E501
            raise ValueError("Invalid value for `number_of_coupons`, must be a value less than or equal to `5000000`")  # noqa: E501

        self._number_of_coupons = number_of_coupons

    @property
    def coupon_settings(self):
        """Gets the coupon_settings of this CouponCreationJob.  # noqa: E501


        :return: The coupon_settings of this CouponCreationJob.  # noqa: E501
        :rtype: CodeGeneratorSettings
        """
        return self._coupon_settings

    @coupon_settings.setter
    def coupon_settings(self, coupon_settings):
        """Sets the coupon_settings of this CouponCreationJob.


        :param coupon_settings: The coupon_settings of this CouponCreationJob.  # noqa: E501
        :type: CodeGeneratorSettings
        """

        self._coupon_settings = coupon_settings

    @property
    def attributes(self):
        """Gets the attributes of this CouponCreationJob.  # noqa: E501

        Arbitrary properties associated with coupons.  # noqa: E501

        :return: The attributes of this CouponCreationJob.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CouponCreationJob.

        Arbitrary properties associated with coupons.  # noqa: E501

        :param attributes: The attributes of this CouponCreationJob.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def batch_id(self):
        """Gets the batch_id of this CouponCreationJob.  # noqa: E501

        The batch ID coupons created by this job will bear.  # noqa: E501

        :return: The batch_id of this CouponCreationJob.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this CouponCreationJob.

        The batch ID coupons created by this job will bear.  # noqa: E501

        :param batch_id: The batch_id of this CouponCreationJob.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and batch_id is None:  # noqa: E501
            raise ValueError("Invalid value for `batch_id`, must not be `None`")  # noqa: E501

        self._batch_id = batch_id

    @property
    def status(self):
        """Gets the status of this CouponCreationJob.  # noqa: E501

        The current status of this request. Possible values: - `pending` - `completed` - `failed` - `coupon pattern full`   # noqa: E501

        :return: The status of this CouponCreationJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CouponCreationJob.

        The current status of this request. Possible values: - `pending` - `completed` - `failed` - `coupon pattern full`   # noqa: E501

        :param status: The status of this CouponCreationJob.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def created_amount(self):
        """Gets the created_amount of this CouponCreationJob.  # noqa: E501

        The number of coupon codes that were already created for this request.  # noqa: E501

        :return: The created_amount of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._created_amount

    @created_amount.setter
    def created_amount(self, created_amount):
        """Sets the created_amount of this CouponCreationJob.

        The number of coupon codes that were already created for this request.  # noqa: E501

        :param created_amount: The created_amount of this CouponCreationJob.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `created_amount`, must not be `None`")  # noqa: E501

        self._created_amount = created_amount

    @property
    def fail_count(self):
        """Gets the fail_count of this CouponCreationJob.  # noqa: E501

        The number of times this job failed.  # noqa: E501

        :return: The fail_count of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._fail_count

    @fail_count.setter
    def fail_count(self, fail_count):
        """Sets the fail_count of this CouponCreationJob.

        The number of times this job failed.  # noqa: E501

        :param fail_count: The fail_count of this CouponCreationJob.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and fail_count is None:  # noqa: E501
            raise ValueError("Invalid value for `fail_count`, must not be `None`")  # noqa: E501

        self._fail_count = fail_count

    @property
    def errors(self):
        """Gets the errors of this CouponCreationJob.  # noqa: E501

        An array of individual problems encountered during the request.  # noqa: E501

        :return: The errors of this CouponCreationJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CouponCreationJob.

        An array of individual problems encountered during the request.  # noqa: E501

        :param errors: The errors of this CouponCreationJob.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and errors is None:  # noqa: E501
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def created_by(self):
        """Gets the created_by of this CouponCreationJob.  # noqa: E501

        ID of the user who created this effect.  # noqa: E501

        :return: The created_by of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CouponCreationJob.

        ID of the user who created this effect.  # noqa: E501

        :param created_by: The created_by of this CouponCreationJob.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def communicated(self):
        """Gets the communicated of this CouponCreationJob.  # noqa: E501

        Whether or not the user that created this job was notified of its final state.  # noqa: E501

        :return: The communicated of this CouponCreationJob.  # noqa: E501
        :rtype: bool
        """
        return self._communicated

    @communicated.setter
    def communicated(self, communicated):
        """Sets the communicated of this CouponCreationJob.

        Whether or not the user that created this job was notified of its final state.  # noqa: E501

        :param communicated: The communicated of this CouponCreationJob.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and communicated is None:  # noqa: E501
            raise ValueError("Invalid value for `communicated`, must not be `None`")  # noqa: E501

        self._communicated = communicated

    @property
    def chunk_execution_count(self):
        """Gets the chunk_execution_count of this CouponCreationJob.  # noqa: E501

        The number of times an attempt to create a chunk of coupons was made during the processing of the job.  # noqa: E501

        :return: The chunk_execution_count of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._chunk_execution_count

    @chunk_execution_count.setter
    def chunk_execution_count(self, chunk_execution_count):
        """Sets the chunk_execution_count of this CouponCreationJob.

        The number of times an attempt to create a chunk of coupons was made during the processing of the job.  # noqa: E501

        :param chunk_execution_count: The chunk_execution_count of this CouponCreationJob.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and chunk_execution_count is None:  # noqa: E501
            raise ValueError("Invalid value for `chunk_execution_count`, must not be `None`")  # noqa: E501

        self._chunk_execution_count = chunk_execution_count

    @property
    def chunk_size(self):
        """Gets the chunk_size of this CouponCreationJob.  # noqa: E501

        The number of coupons that will be created in a single transactions. Coupons will be created in chunks until arriving at the requested amount.  # noqa: E501

        :return: The chunk_size of this CouponCreationJob.  # noqa: E501
        :rtype: int
        """
        return self._chunk_size

    @chunk_size.setter
    def chunk_size(self, chunk_size):
        """Sets the chunk_size of this CouponCreationJob.

        The number of coupons that will be created in a single transactions. Coupons will be created in chunks until arriving at the requested amount.  # noqa: E501

        :param chunk_size: The chunk_size of this CouponCreationJob.  # noqa: E501
        :type: int
        """

        self._chunk_size = chunk_size

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
        if not isinstance(other, CouponCreationJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CouponCreationJob):
            return True

        return self.to_dict() != other.to_dict()