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


class GenerateLoyaltyCard(object):
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
        'status': 'str',
        'customer_profile_ids': 'list[str]'
    }

    attribute_map = {
        'status': 'status',
        'customer_profile_ids': 'customerProfileIds'
    }

    def __init__(self, status='active', customer_profile_ids=None, local_vars_configuration=None):  # noqa: E501
        """GenerateLoyaltyCard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._customer_profile_ids = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if customer_profile_ids is not None:
            self.customer_profile_ids = customer_profile_ids

    @property
    def status(self):
        """Gets the status of this GenerateLoyaltyCard.  # noqa: E501

        Status of the loyalty card.  # noqa: E501

        :return: The status of this GenerateLoyaltyCard.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GenerateLoyaltyCard.

        Status of the loyalty card.  # noqa: E501

        :param status: The status of this GenerateLoyaltyCard.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def customer_profile_ids(self):
        """Gets the customer_profile_ids of this GenerateLoyaltyCard.  # noqa: E501

        Integration IDs of the customer profiles linked to the card.  # noqa: E501

        :return: The customer_profile_ids of this GenerateLoyaltyCard.  # noqa: E501
        :rtype: list[str]
        """
        return self._customer_profile_ids

    @customer_profile_ids.setter
    def customer_profile_ids(self, customer_profile_ids):
        """Sets the customer_profile_ids of this GenerateLoyaltyCard.

        Integration IDs of the customer profiles linked to the card.  # noqa: E501

        :param customer_profile_ids: The customer_profile_ids of this GenerateLoyaltyCard.  # noqa: E501
        :type: list[str]
        """

        self._customer_profile_ids = customer_profile_ids

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
        if not isinstance(other, GenerateLoyaltyCard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GenerateLoyaltyCard):
            return True

        return self.to_dict() != other.to_dict()
