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


class ReferralConstraints(object):
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
        'start_date': 'datetime',
        'expiry_date': 'datetime',
        'usage_limit': 'int'
    }

    attribute_map = {
        'start_date': 'startDate',
        'expiry_date': 'expiryDate',
        'usage_limit': 'usageLimit'
    }

    def __init__(self, start_date=None, expiry_date=None, usage_limit=None, local_vars_configuration=None):  # noqa: E501
        """ReferralConstraints - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._expiry_date = None
        self._usage_limit = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if usage_limit is not None:
            self.usage_limit = usage_limit

    @property
    def start_date(self):
        """Gets the start_date of this ReferralConstraints.  # noqa: E501

        Timestamp at which point the referral code becomes valid.  # noqa: E501

        :return: The start_date of this ReferralConstraints.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ReferralConstraints.

        Timestamp at which point the referral code becomes valid.  # noqa: E501

        :param start_date: The start_date of this ReferralConstraints.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this ReferralConstraints.  # noqa: E501

        Expiration date of the referral code. Referral never expires if this is omitted.  # noqa: E501

        :return: The expiry_date of this ReferralConstraints.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this ReferralConstraints.

        Expiration date of the referral code. Referral never expires if this is omitted.  # noqa: E501

        :param expiry_date: The expiry_date of this ReferralConstraints.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def usage_limit(self):
        """Gets the usage_limit of this ReferralConstraints.  # noqa: E501

        The number of times a referral code can be used. `0` means no limit but any campaign usage limits will still apply.   # noqa: E501

        :return: The usage_limit of this ReferralConstraints.  # noqa: E501
        :rtype: int
        """
        return self._usage_limit

    @usage_limit.setter
    def usage_limit(self, usage_limit):
        """Sets the usage_limit of this ReferralConstraints.

        The number of times a referral code can be used. `0` means no limit but any campaign usage limits will still apply.   # noqa: E501

        :param usage_limit: The usage_limit of this ReferralConstraints.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                usage_limit is not None and usage_limit > 999999):  # noqa: E501
            raise ValueError("Invalid value for `usage_limit`, must be a value less than or equal to `999999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                usage_limit is not None and usage_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `usage_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._usage_limit = usage_limit

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
        if not isinstance(other, ReferralConstraints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReferralConstraints):
            return True

        return self.to_dict() != other.to_dict()
