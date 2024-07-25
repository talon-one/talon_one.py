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


class ChangeLoyaltyTierLevelEffectProps(object):
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
        'previous_tier_name': 'str',
        'new_tier_name': 'str',
        'expiry_date': 'datetime'
    }

    attribute_map = {
        'rule_title': 'ruleTitle',
        'program_id': 'programId',
        'sub_ledger_id': 'subLedgerId',
        'previous_tier_name': 'previousTierName',
        'new_tier_name': 'newTierName',
        'expiry_date': 'expiryDate'
    }

    def __init__(self, rule_title=None, program_id=None, sub_ledger_id=None, previous_tier_name=None, new_tier_name=None, expiry_date=None, local_vars_configuration=None):  # noqa: E501
        """ChangeLoyaltyTierLevelEffectProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rule_title = None
        self._program_id = None
        self._sub_ledger_id = None
        self._previous_tier_name = None
        self._new_tier_name = None
        self._expiry_date = None
        self.discriminator = None

        self.rule_title = rule_title
        self.program_id = program_id
        self.sub_ledger_id = sub_ledger_id
        if previous_tier_name is not None:
            self.previous_tier_name = previous_tier_name
        self.new_tier_name = new_tier_name
        if expiry_date is not None:
            self.expiry_date = expiry_date

    @property
    def rule_title(self):
        """Gets the rule_title of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501

        The title of the rule that triggered the tier upgrade.  # noqa: E501

        :return: The rule_title of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._rule_title

    @rule_title.setter
    def rule_title(self, rule_title):
        """Sets the rule_title of this ChangeLoyaltyTierLevelEffectProps.

        The title of the rule that triggered the tier upgrade.  # noqa: E501

        :param rule_title: The rule_title of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_title is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_title`, must not be `None`")  # noqa: E501

        self._rule_title = rule_title

    @property
    def program_id(self):
        """Gets the program_id of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501

        The ID of the loyalty program where these points were added.  # noqa: E501

        :return: The program_id of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this ChangeLoyaltyTierLevelEffectProps.

        The ID of the loyalty program where these points were added.  # noqa: E501

        :param program_id: The program_id of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and program_id is None:  # noqa: E501
            raise ValueError("Invalid value for `program_id`, must not be `None`")  # noqa: E501

        self._program_id = program_id

    @property
    def sub_ledger_id(self):
        """Gets the sub_ledger_id of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501

        The ID of the subledger within the loyalty program where these points were added.  # noqa: E501

        :return: The sub_ledger_id of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._sub_ledger_id

    @sub_ledger_id.setter
    def sub_ledger_id(self, sub_ledger_id):
        """Sets the sub_ledger_id of this ChangeLoyaltyTierLevelEffectProps.

        The ID of the subledger within the loyalty program where these points were added.  # noqa: E501

        :param sub_ledger_id: The sub_ledger_id of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_ledger_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_ledger_id`, must not be `None`")  # noqa: E501

        self._sub_ledger_id = sub_ledger_id

    @property
    def previous_tier_name(self):
        """Gets the previous_tier_name of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501

        The name of the tier from which the user was upgraded.  # noqa: E501

        :return: The previous_tier_name of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._previous_tier_name

    @previous_tier_name.setter
    def previous_tier_name(self, previous_tier_name):
        """Sets the previous_tier_name of this ChangeLoyaltyTierLevelEffectProps.

        The name of the tier from which the user was upgraded.  # noqa: E501

        :param previous_tier_name: The previous_tier_name of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :type: str
        """

        self._previous_tier_name = previous_tier_name

    @property
    def new_tier_name(self):
        """Gets the new_tier_name of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501

        The name of the tier to which the user has been upgraded.  # noqa: E501

        :return: The new_tier_name of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._new_tier_name

    @new_tier_name.setter
    def new_tier_name(self, new_tier_name):
        """Sets the new_tier_name of this ChangeLoyaltyTierLevelEffectProps.

        The name of the tier to which the user has been upgraded.  # noqa: E501

        :param new_tier_name: The new_tier_name of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and new_tier_name is None:  # noqa: E501
            raise ValueError("Invalid value for `new_tier_name`, must not be `None`")  # noqa: E501

        self._new_tier_name = new_tier_name

    @property
    def expiry_date(self):
        """Gets the expiry_date of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501

        The expiration date of the new tier.  # noqa: E501

        :return: The expiry_date of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this ChangeLoyaltyTierLevelEffectProps.

        The expiration date of the new tier.  # noqa: E501

        :param expiry_date: The expiry_date of this ChangeLoyaltyTierLevelEffectProps.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

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
        if not isinstance(other, ChangeLoyaltyTierLevelEffectProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeLoyaltyTierLevelEffectProps):
            return True

        return self.to_dict() != other.to_dict()