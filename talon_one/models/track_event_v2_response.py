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


class TrackEventV2Response(object):
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
        'customer_profile': 'CustomerProfile',
        'event': 'Event',
        'loyalty': 'Loyalty',
        'triggered_campaigns': 'list[Campaign]',
        'rule_failure_reasons': 'list[RuleFailureReason]',
        'awarded_giveaways': 'list[Giveaway]',
        'effects': 'list[Effect]',
        'created_coupons': 'list[Coupon]',
        'created_referrals': 'list[Referral]'
    }

    attribute_map = {
        'customer_profile': 'customerProfile',
        'event': 'event',
        'loyalty': 'loyalty',
        'triggered_campaigns': 'triggeredCampaigns',
        'rule_failure_reasons': 'ruleFailureReasons',
        'awarded_giveaways': 'awardedGiveaways',
        'effects': 'effects',
        'created_coupons': 'createdCoupons',
        'created_referrals': 'createdReferrals'
    }

    def __init__(self, customer_profile=None, event=None, loyalty=None, triggered_campaigns=None, rule_failure_reasons=None, awarded_giveaways=None, effects=None, created_coupons=None, created_referrals=None, local_vars_configuration=None):  # noqa: E501
        """TrackEventV2Response - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._customer_profile = None
        self._event = None
        self._loyalty = None
        self._triggered_campaigns = None
        self._rule_failure_reasons = None
        self._awarded_giveaways = None
        self._effects = None
        self._created_coupons = None
        self._created_referrals = None
        self.discriminator = None

        if customer_profile is not None:
            self.customer_profile = customer_profile
        if event is not None:
            self.event = event
        if loyalty is not None:
            self.loyalty = loyalty
        if triggered_campaigns is not None:
            self.triggered_campaigns = triggered_campaigns
        if rule_failure_reasons is not None:
            self.rule_failure_reasons = rule_failure_reasons
        if awarded_giveaways is not None:
            self.awarded_giveaways = awarded_giveaways
        self.effects = effects
        self.created_coupons = created_coupons
        self.created_referrals = created_referrals

    @property
    def customer_profile(self):
        """Gets the customer_profile of this TrackEventV2Response.  # noqa: E501


        :return: The customer_profile of this TrackEventV2Response.  # noqa: E501
        :rtype: CustomerProfile
        """
        return self._customer_profile

    @customer_profile.setter
    def customer_profile(self, customer_profile):
        """Sets the customer_profile of this TrackEventV2Response.


        :param customer_profile: The customer_profile of this TrackEventV2Response.  # noqa: E501
        :type: CustomerProfile
        """

        self._customer_profile = customer_profile

    @property
    def event(self):
        """Gets the event of this TrackEventV2Response.  # noqa: E501


        :return: The event of this TrackEventV2Response.  # noqa: E501
        :rtype: Event
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this TrackEventV2Response.


        :param event: The event of this TrackEventV2Response.  # noqa: E501
        :type: Event
        """

        self._event = event

    @property
    def loyalty(self):
        """Gets the loyalty of this TrackEventV2Response.  # noqa: E501


        :return: The loyalty of this TrackEventV2Response.  # noqa: E501
        :rtype: Loyalty
        """
        return self._loyalty

    @loyalty.setter
    def loyalty(self, loyalty):
        """Sets the loyalty of this TrackEventV2Response.


        :param loyalty: The loyalty of this TrackEventV2Response.  # noqa: E501
        :type: Loyalty
        """

        self._loyalty = loyalty

    @property
    def triggered_campaigns(self):
        """Gets the triggered_campaigns of this TrackEventV2Response.  # noqa: E501


        :return: The triggered_campaigns of this TrackEventV2Response.  # noqa: E501
        :rtype: list[Campaign]
        """
        return self._triggered_campaigns

    @triggered_campaigns.setter
    def triggered_campaigns(self, triggered_campaigns):
        """Sets the triggered_campaigns of this TrackEventV2Response.


        :param triggered_campaigns: The triggered_campaigns of this TrackEventV2Response.  # noqa: E501
        :type: list[Campaign]
        """

        self._triggered_campaigns = triggered_campaigns

    @property
    def rule_failure_reasons(self):
        """Gets the rule_failure_reasons of this TrackEventV2Response.  # noqa: E501


        :return: The rule_failure_reasons of this TrackEventV2Response.  # noqa: E501
        :rtype: list[RuleFailureReason]
        """
        return self._rule_failure_reasons

    @rule_failure_reasons.setter
    def rule_failure_reasons(self, rule_failure_reasons):
        """Sets the rule_failure_reasons of this TrackEventV2Response.


        :param rule_failure_reasons: The rule_failure_reasons of this TrackEventV2Response.  # noqa: E501
        :type: list[RuleFailureReason]
        """

        self._rule_failure_reasons = rule_failure_reasons

    @property
    def awarded_giveaways(self):
        """Gets the awarded_giveaways of this TrackEventV2Response.  # noqa: E501


        :return: The awarded_giveaways of this TrackEventV2Response.  # noqa: E501
        :rtype: list[Giveaway]
        """
        return self._awarded_giveaways

    @awarded_giveaways.setter
    def awarded_giveaways(self, awarded_giveaways):
        """Sets the awarded_giveaways of this TrackEventV2Response.


        :param awarded_giveaways: The awarded_giveaways of this TrackEventV2Response.  # noqa: E501
        :type: list[Giveaway]
        """

        self._awarded_giveaways = awarded_giveaways

    @property
    def effects(self):
        """Gets the effects of this TrackEventV2Response.  # noqa: E501

        The effects generated by the rules in your running campaigns. See [API effects](https://docs.talon.one/docs/dev/integration-api/api-effects).  # noqa: E501

        :return: The effects of this TrackEventV2Response.  # noqa: E501
        :rtype: list[Effect]
        """
        return self._effects

    @effects.setter
    def effects(self, effects):
        """Sets the effects of this TrackEventV2Response.

        The effects generated by the rules in your running campaigns. See [API effects](https://docs.talon.one/docs/dev/integration-api/api-effects).  # noqa: E501

        :param effects: The effects of this TrackEventV2Response.  # noqa: E501
        :type: list[Effect]
        """
        if self.local_vars_configuration.client_side_validation and effects is None:  # noqa: E501
            raise ValueError("Invalid value for `effects`, must not be `None`")  # noqa: E501

        self._effects = effects

    @property
    def created_coupons(self):
        """Gets the created_coupons of this TrackEventV2Response.  # noqa: E501


        :return: The created_coupons of this TrackEventV2Response.  # noqa: E501
        :rtype: list[Coupon]
        """
        return self._created_coupons

    @created_coupons.setter
    def created_coupons(self, created_coupons):
        """Sets the created_coupons of this TrackEventV2Response.


        :param created_coupons: The created_coupons of this TrackEventV2Response.  # noqa: E501
        :type: list[Coupon]
        """
        if self.local_vars_configuration.client_side_validation and created_coupons is None:  # noqa: E501
            raise ValueError("Invalid value for `created_coupons`, must not be `None`")  # noqa: E501

        self._created_coupons = created_coupons

    @property
    def created_referrals(self):
        """Gets the created_referrals of this TrackEventV2Response.  # noqa: E501


        :return: The created_referrals of this TrackEventV2Response.  # noqa: E501
        :rtype: list[Referral]
        """
        return self._created_referrals

    @created_referrals.setter
    def created_referrals(self, created_referrals):
        """Sets the created_referrals of this TrackEventV2Response.


        :param created_referrals: The created_referrals of this TrackEventV2Response.  # noqa: E501
        :type: list[Referral]
        """
        if self.local_vars_configuration.client_side_validation and created_referrals is None:  # noqa: E501
            raise ValueError("Invalid value for `created_referrals`, must not be `None`")  # noqa: E501

        self._created_referrals = created_referrals

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
        if not isinstance(other, TrackEventV2Response):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackEventV2Response):
            return True

        return self.to_dict() != other.to_dict()
