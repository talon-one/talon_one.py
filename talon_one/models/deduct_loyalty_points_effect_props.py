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


class DeductLoyaltyPointsEffectProps(object):
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
        'rule_title': 'str',
        'program_id': 'int',
        'sub_ledger_id': 'str',
        'value': 'float'
    }

    attribute_map = {
        'rule_title': 'ruleTitle',
        'program_id': 'programId',
        'sub_ledger_id': 'subLedgerId',
        'value': 'value'
    }

    def __init__(self, rule_title=None, program_id=None, sub_ledger_id=None, value=None, local_vars_configuration=None):  # noqa: E501
        """DeductLoyaltyPointsEffectProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rule_title = None
        self._program_id = None
        self._sub_ledger_id = None
        self._value = None
        self.discriminator = None

        self.rule_title = rule_title
        self.program_id = program_id
        self.sub_ledger_id = sub_ledger_id
        self.value = value

    @property
    def rule_title(self):
        """Gets the rule_title of this DeductLoyaltyPointsEffectProps.  # noqa: E501

        The title of the rule that contained triggered this points deduction  # noqa: E501

        :return: The rule_title of this DeductLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._rule_title

    @rule_title.setter
    def rule_title(self, rule_title):
        """Sets the rule_title of this DeductLoyaltyPointsEffectProps.

        The title of the rule that contained triggered this points deduction  # noqa: E501

        :param rule_title: The rule_title of this DeductLoyaltyPointsEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_title is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_title`, must not be `None`")  # noqa: E501

        self._rule_title = rule_title

    @property
    def program_id(self):
        """Gets the program_id of this DeductLoyaltyPointsEffectProps.  # noqa: E501

        The ID of the loyalty program where these points were added  # noqa: E501

        :return: The program_id of this DeductLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this DeductLoyaltyPointsEffectProps.

        The ID of the loyalty program where these points were added  # noqa: E501

        :param program_id: The program_id of this DeductLoyaltyPointsEffectProps.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and program_id is None:  # noqa: E501
            raise ValueError("Invalid value for `program_id`, must not be `None`")  # noqa: E501

        self._program_id = program_id

    @property
    def sub_ledger_id(self):
        """Gets the sub_ledger_id of this DeductLoyaltyPointsEffectProps.  # noqa: E501

        The ID of the subledger within the loyalty program where these points were added  # noqa: E501

        :return: The sub_ledger_id of this DeductLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._sub_ledger_id

    @sub_ledger_id.setter
    def sub_ledger_id(self, sub_ledger_id):
        """Sets the sub_ledger_id of this DeductLoyaltyPointsEffectProps.

        The ID of the subledger within the loyalty program where these points were added  # noqa: E501

        :param sub_ledger_id: The sub_ledger_id of this DeductLoyaltyPointsEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_ledger_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_ledger_id`, must not be `None`")  # noqa: E501

        self._sub_ledger_id = sub_ledger_id

    @property
    def value(self):
        """Gets the value of this DeductLoyaltyPointsEffectProps.  # noqa: E501

        The amount of points that were deducted  # noqa: E501

        :return: The value of this DeductLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DeductLoyaltyPointsEffectProps.

        The amount of points that were deducted  # noqa: E501

        :param value: The value of this DeductLoyaltyPointsEffectProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, DeductLoyaltyPointsEffectProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeductLoyaltyPointsEffectProps):
            return True

        return self.to_dict() != other.to_dict()
