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


class LoyaltyLedger(object):
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
        'ledger': 'LoyaltySubLedger',
        'sub_ledgers': 'dict(str, LoyaltySubLedger)'
    }

    attribute_map = {
        'ledger': 'ledger',
        'sub_ledgers': 'subLedgers'
    }

    def __init__(self, ledger=None, sub_ledgers=None, local_vars_configuration=None):  # noqa: E501
        """LoyaltyLedger - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ledger = None
        self._sub_ledgers = None
        self.discriminator = None

        self.ledger = ledger
        if sub_ledgers is not None:
            self.sub_ledgers = sub_ledgers

    @property
    def ledger(self):
        """Gets the ledger of this LoyaltyLedger.  # noqa: E501


        :return: The ledger of this LoyaltyLedger.  # noqa: E501
        :rtype: LoyaltySubLedger
        """
        return self._ledger

    @ledger.setter
    def ledger(self, ledger):
        """Sets the ledger of this LoyaltyLedger.


        :param ledger: The ledger of this LoyaltyLedger.  # noqa: E501
        :type: LoyaltySubLedger
        """
        if self.local_vars_configuration.client_side_validation and ledger is None:  # noqa: E501
            raise ValueError("Invalid value for `ledger`, must not be `None`")  # noqa: E501

        self._ledger = ledger

    @property
    def sub_ledgers(self):
        """Gets the sub_ledgers of this LoyaltyLedger.  # noqa: E501

        A map containing a list of all loyalty subledger balances  # noqa: E501

        :return: The sub_ledgers of this LoyaltyLedger.  # noqa: E501
        :rtype: dict(str, LoyaltySubLedger)
        """
        return self._sub_ledgers

    @sub_ledgers.setter
    def sub_ledgers(self, sub_ledgers):
        """Sets the sub_ledgers of this LoyaltyLedger.

        A map containing a list of all loyalty subledger balances  # noqa: E501

        :param sub_ledgers: The sub_ledgers of this LoyaltyLedger.  # noqa: E501
        :type: dict(str, LoyaltySubLedger)
        """

        self._sub_ledgers = sub_ledgers

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
        if not isinstance(other, LoyaltyLedger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyLedger):
            return True

        return self.to_dict() != other.to_dict()
