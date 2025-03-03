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


class ProductSkuUnitAnalytics(object):
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
        'start_time': 'datetime',
        'end_time': 'datetime',
        'purchased_units': 'AnalyticsDataPointWithTrend',
        'sku': 'str'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'purchased_units': 'purchasedUnits',
        'sku': 'sku'
    }

    def __init__(self, start_time=None, end_time=None, purchased_units=None, sku=None, local_vars_configuration=None):  # noqa: E501
        """ProductSkuUnitAnalytics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_time = None
        self._end_time = None
        self._purchased_units = None
        self._sku = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.purchased_units = purchased_units
        self.sku = sku

    @property
    def start_time(self):
        """Gets the start_time of this ProductSkuUnitAnalytics.  # noqa: E501

        The start of the aggregation time frame in UTC.  # noqa: E501

        :return: The start_time of this ProductSkuUnitAnalytics.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ProductSkuUnitAnalytics.

        The start of the aggregation time frame in UTC.  # noqa: E501

        :param start_time: The start_time of this ProductSkuUnitAnalytics.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ProductSkuUnitAnalytics.  # noqa: E501

        The end of the aggregation time frame in UTC.  # noqa: E501

        :return: The end_time of this ProductSkuUnitAnalytics.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ProductSkuUnitAnalytics.

        The end of the aggregation time frame in UTC.  # noqa: E501

        :param end_time: The end_time of this ProductSkuUnitAnalytics.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and end_time is None:  # noqa: E501
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def purchased_units(self):
        """Gets the purchased_units of this ProductSkuUnitAnalytics.  # noqa: E501


        :return: The purchased_units of this ProductSkuUnitAnalytics.  # noqa: E501
        :rtype: AnalyticsDataPointWithTrend
        """
        return self._purchased_units

    @purchased_units.setter
    def purchased_units(self, purchased_units):
        """Sets the purchased_units of this ProductSkuUnitAnalytics.


        :param purchased_units: The purchased_units of this ProductSkuUnitAnalytics.  # noqa: E501
        :type: AnalyticsDataPointWithTrend
        """
        if self.local_vars_configuration.client_side_validation and purchased_units is None:  # noqa: E501
            raise ValueError("Invalid value for `purchased_units`, must not be `None`")  # noqa: E501

        self._purchased_units = purchased_units

    @property
    def sku(self):
        """Gets the sku of this ProductSkuUnitAnalytics.  # noqa: E501

        The SKU linked to the analytics-level product.  # noqa: E501

        :return: The sku of this ProductSkuUnitAnalytics.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this ProductSkuUnitAnalytics.

        The SKU linked to the analytics-level product.  # noqa: E501

        :param sku: The sku of this ProductSkuUnitAnalytics.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sku is None:  # noqa: E501
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501

        self._sku = sku

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
        if not isinstance(other, ProductSkuUnitAnalytics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductSkuUnitAnalytics):
            return True

        return self.to_dict() != other.to_dict()
