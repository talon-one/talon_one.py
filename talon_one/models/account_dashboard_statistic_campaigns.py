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


class AccountDashboardStatisticCampaigns(object):
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
        'live': 'int',
        'ending_soon': 'int'
    }

    attribute_map = {
        'live': 'live',
        'ending_soon': 'endingSoon'
    }

    def __init__(self, live=None, ending_soon=None, local_vars_configuration=None):  # noqa: E501
        """AccountDashboardStatisticCampaigns - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._live = None
        self._ending_soon = None
        self.discriminator = None

        self.live = live
        self.ending_soon = ending_soon

    @property
    def live(self):
        """Gets the live of this AccountDashboardStatisticCampaigns.  # noqa: E501

        Number of campaigns that are active and live (across all Applications).  # noqa: E501

        :return: The live of this AccountDashboardStatisticCampaigns.  # noqa: E501
        :rtype: int
        """
        return self._live

    @live.setter
    def live(self, live):
        """Sets the live of this AccountDashboardStatisticCampaigns.

        Number of campaigns that are active and live (across all Applications).  # noqa: E501

        :param live: The live of this AccountDashboardStatisticCampaigns.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and live is None:  # noqa: E501
            raise ValueError("Invalid value for `live`, must not be `None`")  # noqa: E501

        self._live = live

    @property
    def ending_soon(self):
        """Gets the ending_soon of this AccountDashboardStatisticCampaigns.  # noqa: E501

        Campaigns with a schedule ending in 7 days or with only 10% of budget left.  # noqa: E501

        :return: The ending_soon of this AccountDashboardStatisticCampaigns.  # noqa: E501
        :rtype: int
        """
        return self._ending_soon

    @ending_soon.setter
    def ending_soon(self, ending_soon):
        """Sets the ending_soon of this AccountDashboardStatisticCampaigns.

        Campaigns with a schedule ending in 7 days or with only 10% of budget left.  # noqa: E501

        :param ending_soon: The ending_soon of this AccountDashboardStatisticCampaigns.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ending_soon is None:  # noqa: E501
            raise ValueError("Invalid value for `ending_soon`, must not be `None`")  # noqa: E501

        self._ending_soon = ending_soon

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
        if not isinstance(other, AccountDashboardStatisticCampaigns):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountDashboardStatisticCampaigns):
            return True

        return self.to_dict() != other.to_dict()
