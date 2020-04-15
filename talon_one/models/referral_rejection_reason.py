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


class ReferralRejectionReason(object):
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
        'campaign_id': 'int',
        'referral_id': 'int',
        'reason': 'str'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'referral_id': 'referralId',
        'reason': 'reason'
    }

    def __init__(self, campaign_id=None, referral_id=None, reason=None, local_vars_configuration=None):  # noqa: E501
        """ReferralRejectionReason - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._campaign_id = None
        self._referral_id = None
        self._reason = None
        self.discriminator = None

        self.campaign_id = campaign_id
        self.referral_id = referral_id
        self.reason = reason

    @property
    def campaign_id(self):
        """Gets the campaign_id of this ReferralRejectionReason.  # noqa: E501


        :return: The campaign_id of this ReferralRejectionReason.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this ReferralRejectionReason.


        :param campaign_id: The campaign_id of this ReferralRejectionReason.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def referral_id(self):
        """Gets the referral_id of this ReferralRejectionReason.  # noqa: E501


        :return: The referral_id of this ReferralRejectionReason.  # noqa: E501
        :rtype: int
        """
        return self._referral_id

    @referral_id.setter
    def referral_id(self, referral_id):
        """Sets the referral_id of this ReferralRejectionReason.


        :param referral_id: The referral_id of this ReferralRejectionReason.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and referral_id is None:  # noqa: E501
            raise ValueError("Invalid value for `referral_id`, must not be `None`")  # noqa: E501

        self._referral_id = referral_id

    @property
    def reason(self):
        """Gets the reason of this ReferralRejectionReason.  # noqa: E501


        :return: The reason of this ReferralRejectionReason.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ReferralRejectionReason.


        :param reason: The reason of this ReferralRejectionReason.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reason is None:  # noqa: E501
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501
        allowed_values = ["ReferralNotFound", "ReferralRecipientIdSameAsAdvocate", "ReferralPartOfNotRunningCampaign", "ReferralValidConditionMissing", "ReferralLimitReached", "CampaignLimitReached", "ProfileLimitReached", "ReferralRecipientDoesNotMatch", "ReferralExpired", "ReferralStartDateInFuture", "ReferralRejectedByCondition", "EffectCouldNotBeApplied"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

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
        if not isinstance(other, ReferralRejectionReason):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReferralRejectionReason):
            return True

        return self.to_dict() != other.to_dict()
