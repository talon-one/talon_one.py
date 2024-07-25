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


class TransferLoyaltyCard(object):
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
        'new_card_identifier': 'str',
        'block_reason': 'str'
    }

    attribute_map = {
        'new_card_identifier': 'newCardIdentifier',
        'block_reason': 'blockReason'
    }

    def __init__(self, new_card_identifier=None, block_reason=None, local_vars_configuration=None):  # noqa: E501
        """TransferLoyaltyCard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._new_card_identifier = None
        self._block_reason = None
        self.discriminator = None

        self.new_card_identifier = new_card_identifier
        if block_reason is not None:
            self.block_reason = block_reason

    @property
    def new_card_identifier(self):
        """Gets the new_card_identifier of this TransferLoyaltyCard.  # noqa: E501

        The alphanumeric identifier of the loyalty card.   # noqa: E501

        :return: The new_card_identifier of this TransferLoyaltyCard.  # noqa: E501
        :rtype: str
        """
        return self._new_card_identifier

    @new_card_identifier.setter
    def new_card_identifier(self, new_card_identifier):
        """Sets the new_card_identifier of this TransferLoyaltyCard.

        The alphanumeric identifier of the loyalty card.   # noqa: E501

        :param new_card_identifier: The new_card_identifier of this TransferLoyaltyCard.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and new_card_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `new_card_identifier`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                new_card_identifier is not None and len(new_card_identifier) > 108):
            raise ValueError("Invalid value for `new_card_identifier`, length must be less than or equal to `108`")  # noqa: E501

        self._new_card_identifier = new_card_identifier

    @property
    def block_reason(self):
        """Gets the block_reason of this TransferLoyaltyCard.  # noqa: E501

        Reason for transferring and blocking the loyalty card.   # noqa: E501

        :return: The block_reason of this TransferLoyaltyCard.  # noqa: E501
        :rtype: str
        """
        return self._block_reason

    @block_reason.setter
    def block_reason(self, block_reason):
        """Sets the block_reason of this TransferLoyaltyCard.

        Reason for transferring and blocking the loyalty card.   # noqa: E501

        :param block_reason: The block_reason of this TransferLoyaltyCard.  # noqa: E501
        :type: str
        """

        self._block_reason = block_reason

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
        if not isinstance(other, TransferLoyaltyCard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransferLoyaltyCard):
            return True

        return self.to_dict() != other.to_dict()
