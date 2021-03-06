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


class IntegrationStateV2(object):
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
        'customer_session': 'CustomerSessionV2',
        'customer_profile': 'CustomerProfile',
        'event': 'Event',
        'loyalty': 'Loyalty',
        'referral': 'Referral',
        'coupons': 'list[Coupon]',
        'triggered_campaigns': 'list[Campaign]',
        'effects': 'list[Effect]',
        'created_coupons': 'list[Coupon]',
        'created_referrals': 'list[Referral]'
    }

    attribute_map = {
        'customer_session': 'customerSession',
        'customer_profile': 'customerProfile',
        'event': 'event',
        'loyalty': 'loyalty',
        'referral': 'referral',
        'coupons': 'coupons',
        'triggered_campaigns': 'triggeredCampaigns',
        'effects': 'effects',
        'created_coupons': 'createdCoupons',
        'created_referrals': 'createdReferrals'
    }

    def __init__(self, customer_session=None, customer_profile=None, event=None, loyalty=None, referral=None, coupons=None, triggered_campaigns=None, effects=None, created_coupons=None, created_referrals=None, local_vars_configuration=None):  # noqa: E501
        """IntegrationStateV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._customer_session = None
        self._customer_profile = None
        self._event = None
        self._loyalty = None
        self._referral = None
        self._coupons = None
        self._triggered_campaigns = None
        self._effects = None
        self._created_coupons = None
        self._created_referrals = None
        self.discriminator = None

        if customer_session is not None:
            self.customer_session = customer_session
        if customer_profile is not None:
            self.customer_profile = customer_profile
        if event is not None:
            self.event = event
        if loyalty is not None:
            self.loyalty = loyalty
        if referral is not None:
            self.referral = referral
        if coupons is not None:
            self.coupons = coupons
        if triggered_campaigns is not None:
            self.triggered_campaigns = triggered_campaigns
        self.effects = effects
        self.created_coupons = created_coupons
        self.created_referrals = created_referrals

    @property
    def customer_session(self):
        """Gets the customer_session of this IntegrationStateV2.  # noqa: E501


        :return: The customer_session of this IntegrationStateV2.  # noqa: E501
        :rtype: CustomerSessionV2
        """
        return self._customer_session

    @customer_session.setter
    def customer_session(self, customer_session):
        """Sets the customer_session of this IntegrationStateV2.


        :param customer_session: The customer_session of this IntegrationStateV2.  # noqa: E501
        :type: CustomerSessionV2
        """

        self._customer_session = customer_session

    @property
    def customer_profile(self):
        """Gets the customer_profile of this IntegrationStateV2.  # noqa: E501


        :return: The customer_profile of this IntegrationStateV2.  # noqa: E501
        :rtype: CustomerProfile
        """
        return self._customer_profile

    @customer_profile.setter
    def customer_profile(self, customer_profile):
        """Sets the customer_profile of this IntegrationStateV2.


        :param customer_profile: The customer_profile of this IntegrationStateV2.  # noqa: E501
        :type: CustomerProfile
        """

        self._customer_profile = customer_profile

    @property
    def event(self):
        """Gets the event of this IntegrationStateV2.  # noqa: E501


        :return: The event of this IntegrationStateV2.  # noqa: E501
        :rtype: Event
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this IntegrationStateV2.


        :param event: The event of this IntegrationStateV2.  # noqa: E501
        :type: Event
        """

        self._event = event

    @property
    def loyalty(self):
        """Gets the loyalty of this IntegrationStateV2.  # noqa: E501


        :return: The loyalty of this IntegrationStateV2.  # noqa: E501
        :rtype: Loyalty
        """
        return self._loyalty

    @loyalty.setter
    def loyalty(self, loyalty):
        """Sets the loyalty of this IntegrationStateV2.


        :param loyalty: The loyalty of this IntegrationStateV2.  # noqa: E501
        :type: Loyalty
        """

        self._loyalty = loyalty

    @property
    def referral(self):
        """Gets the referral of this IntegrationStateV2.  # noqa: E501


        :return: The referral of this IntegrationStateV2.  # noqa: E501
        :rtype: Referral
        """
        return self._referral

    @referral.setter
    def referral(self, referral):
        """Sets the referral of this IntegrationStateV2.


        :param referral: The referral of this IntegrationStateV2.  # noqa: E501
        :type: Referral
        """

        self._referral = referral

    @property
    def coupons(self):
        """Gets the coupons of this IntegrationStateV2.  # noqa: E501


        :return: The coupons of this IntegrationStateV2.  # noqa: E501
        :rtype: list[Coupon]
        """
        return self._coupons

    @coupons.setter
    def coupons(self, coupons):
        """Sets the coupons of this IntegrationStateV2.


        :param coupons: The coupons of this IntegrationStateV2.  # noqa: E501
        :type: list[Coupon]
        """

        self._coupons = coupons

    @property
    def triggered_campaigns(self):
        """Gets the triggered_campaigns of this IntegrationStateV2.  # noqa: E501


        :return: The triggered_campaigns of this IntegrationStateV2.  # noqa: E501
        :rtype: list[Campaign]
        """
        return self._triggered_campaigns

    @triggered_campaigns.setter
    def triggered_campaigns(self, triggered_campaigns):
        """Sets the triggered_campaigns of this IntegrationStateV2.


        :param triggered_campaigns: The triggered_campaigns of this IntegrationStateV2.  # noqa: E501
        :type: list[Campaign]
        """

        self._triggered_campaigns = triggered_campaigns

    @property
    def effects(self):
        """Gets the effects of this IntegrationStateV2.  # noqa: E501


        :return: The effects of this IntegrationStateV2.  # noqa: E501
        :rtype: list[Effect]
        """
        return self._effects

    @effects.setter
    def effects(self, effects):
        """Sets the effects of this IntegrationStateV2.


        :param effects: The effects of this IntegrationStateV2.  # noqa: E501
        :type: list[Effect]
        """
        if self.local_vars_configuration.client_side_validation and effects is None:  # noqa: E501
            raise ValueError("Invalid value for `effects`, must not be `None`")  # noqa: E501

        self._effects = effects

    @property
    def created_coupons(self):
        """Gets the created_coupons of this IntegrationStateV2.  # noqa: E501


        :return: The created_coupons of this IntegrationStateV2.  # noqa: E501
        :rtype: list[Coupon]
        """
        return self._created_coupons

    @created_coupons.setter
    def created_coupons(self, created_coupons):
        """Sets the created_coupons of this IntegrationStateV2.


        :param created_coupons: The created_coupons of this IntegrationStateV2.  # noqa: E501
        :type: list[Coupon]
        """
        if self.local_vars_configuration.client_side_validation and created_coupons is None:  # noqa: E501
            raise ValueError("Invalid value for `created_coupons`, must not be `None`")  # noqa: E501

        self._created_coupons = created_coupons

    @property
    def created_referrals(self):
        """Gets the created_referrals of this IntegrationStateV2.  # noqa: E501


        :return: The created_referrals of this IntegrationStateV2.  # noqa: E501
        :rtype: list[Referral]
        """
        return self._created_referrals

    @created_referrals.setter
    def created_referrals(self, created_referrals):
        """Sets the created_referrals of this IntegrationStateV2.


        :param created_referrals: The created_referrals of this IntegrationStateV2.  # noqa: E501
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
        if not isinstance(other, IntegrationStateV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationStateV2):
            return True

        return self.to_dict() != other.to_dict()
