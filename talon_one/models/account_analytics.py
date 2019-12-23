# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountAnalytics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'applications': 'int',
        'active_campaigns': 'int',
        'campaigns': 'int',
        'coupons': 'int',
        'active_coupons': 'int',
        'expired_coupons': 'int',
        'custom_attributes': 'int',
        'referral_codes': 'int',
        'active_referral_codes': 'int',
        'expired_referral_codes': 'int',
        'users': 'int',
        'roles': 'int',
        'webhooks': 'int',
        'loyalty_programs': 'int',
        'active_rules': 'int'
    }

    attribute_map = {
        'applications': 'applications',
        'active_campaigns': 'activeCampaigns',
        'campaigns': 'campaigns',
        'coupons': 'coupons',
        'active_coupons': 'activeCoupons',
        'expired_coupons': 'expiredCoupons',
        'custom_attributes': 'customAttributes',
        'referral_codes': 'referralCodes',
        'active_referral_codes': 'activeReferralCodes',
        'expired_referral_codes': 'expiredReferralCodes',
        'users': 'users',
        'roles': 'roles',
        'webhooks': 'webhooks',
        'loyalty_programs': 'loyaltyPrograms',
        'active_rules': 'activeRules'
    }

    def __init__(self, applications=None, active_campaigns=None, campaigns=None, coupons=None, active_coupons=None, expired_coupons=None, custom_attributes=None, referral_codes=None, active_referral_codes=None, expired_referral_codes=None, users=None, roles=None, webhooks=None, loyalty_programs=None, active_rules=None):  # noqa: E501
        """AccountAnalytics - a model defined in Swagger"""  # noqa: E501

        self._applications = None
        self._active_campaigns = None
        self._campaigns = None
        self._coupons = None
        self._active_coupons = None
        self._expired_coupons = None
        self._custom_attributes = None
        self._referral_codes = None
        self._active_referral_codes = None
        self._expired_referral_codes = None
        self._users = None
        self._roles = None
        self._webhooks = None
        self._loyalty_programs = None
        self._active_rules = None
        self.discriminator = None

        self.applications = applications
        self.active_campaigns = active_campaigns
        self.campaigns = campaigns
        self.coupons = coupons
        self.active_coupons = active_coupons
        self.expired_coupons = expired_coupons
        self.custom_attributes = custom_attributes
        self.referral_codes = referral_codes
        self.active_referral_codes = active_referral_codes
        self.expired_referral_codes = expired_referral_codes
        self.users = users
        self.roles = roles
        self.webhooks = webhooks
        self.loyalty_programs = loyalty_programs
        self.active_rules = active_rules

    @property
    def applications(self):
        """Gets the applications of this AccountAnalytics.  # noqa: E501

        Total Number of Applications inside the account  # noqa: E501

        :return: The applications of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this AccountAnalytics.

        Total Number of Applications inside the account  # noqa: E501

        :param applications: The applications of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if applications is None:
            raise ValueError("Invalid value for `applications`, must not be `None`")  # noqa: E501

        self._applications = applications

    @property
    def active_campaigns(self):
        """Gets the active_campaigns of this AccountAnalytics.  # noqa: E501

        Total Number of Active Applications inside the account  # noqa: E501

        :return: The active_campaigns of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._active_campaigns

    @active_campaigns.setter
    def active_campaigns(self, active_campaigns):
        """Sets the active_campaigns of this AccountAnalytics.

        Total Number of Active Applications inside the account  # noqa: E501

        :param active_campaigns: The active_campaigns of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if active_campaigns is None:
            raise ValueError("Invalid value for `active_campaigns`, must not be `None`")  # noqa: E501

        self._active_campaigns = active_campaigns

    @property
    def campaigns(self):
        """Gets the campaigns of this AccountAnalytics.  # noqa: E501

        Total Number of campaigns inside the account  # noqa: E501

        :return: The campaigns of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._campaigns

    @campaigns.setter
    def campaigns(self, campaigns):
        """Sets the campaigns of this AccountAnalytics.

        Total Number of campaigns inside the account  # noqa: E501

        :param campaigns: The campaigns of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if campaigns is None:
            raise ValueError("Invalid value for `campaigns`, must not be `None`")  # noqa: E501

        self._campaigns = campaigns

    @property
    def coupons(self):
        """Gets the coupons of this AccountAnalytics.  # noqa: E501

        Total Number of coupons inside the account  # noqa: E501

        :return: The coupons of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._coupons

    @coupons.setter
    def coupons(self, coupons):
        """Sets the coupons of this AccountAnalytics.

        Total Number of coupons inside the account  # noqa: E501

        :param coupons: The coupons of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if coupons is None:
            raise ValueError("Invalid value for `coupons`, must not be `None`")  # noqa: E501

        self._coupons = coupons

    @property
    def active_coupons(self):
        """Gets the active_coupons of this AccountAnalytics.  # noqa: E501

        Total Number of active coupons inside the account  # noqa: E501

        :return: The active_coupons of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._active_coupons

    @active_coupons.setter
    def active_coupons(self, active_coupons):
        """Sets the active_coupons of this AccountAnalytics.

        Total Number of active coupons inside the account  # noqa: E501

        :param active_coupons: The active_coupons of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if active_coupons is None:
            raise ValueError("Invalid value for `active_coupons`, must not be `None`")  # noqa: E501

        self._active_coupons = active_coupons

    @property
    def expired_coupons(self):
        """Gets the expired_coupons of this AccountAnalytics.  # noqa: E501

        Total Number of expired coupons inside the account  # noqa: E501

        :return: The expired_coupons of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._expired_coupons

    @expired_coupons.setter
    def expired_coupons(self, expired_coupons):
        """Sets the expired_coupons of this AccountAnalytics.

        Total Number of expired coupons inside the account  # noqa: E501

        :param expired_coupons: The expired_coupons of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if expired_coupons is None:
            raise ValueError("Invalid value for `expired_coupons`, must not be `None`")  # noqa: E501

        self._expired_coupons = expired_coupons

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this AccountAnalytics.  # noqa: E501

        Total Number of custom attributes inside the account  # noqa: E501

        :return: The custom_attributes of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this AccountAnalytics.

        Total Number of custom attributes inside the account  # noqa: E501

        :param custom_attributes: The custom_attributes of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if custom_attributes is None:
            raise ValueError("Invalid value for `custom_attributes`, must not be `None`")  # noqa: E501

        self._custom_attributes = custom_attributes

    @property
    def referral_codes(self):
        """Gets the referral_codes of this AccountAnalytics.  # noqa: E501

        Total Number of referral codes inside the account  # noqa: E501

        :return: The referral_codes of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._referral_codes

    @referral_codes.setter
    def referral_codes(self, referral_codes):
        """Sets the referral_codes of this AccountAnalytics.

        Total Number of referral codes inside the account  # noqa: E501

        :param referral_codes: The referral_codes of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if referral_codes is None:
            raise ValueError("Invalid value for `referral_codes`, must not be `None`")  # noqa: E501

        self._referral_codes = referral_codes

    @property
    def active_referral_codes(self):
        """Gets the active_referral_codes of this AccountAnalytics.  # noqa: E501

        Total Number of active referral codes inside the account  # noqa: E501

        :return: The active_referral_codes of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._active_referral_codes

    @active_referral_codes.setter
    def active_referral_codes(self, active_referral_codes):
        """Sets the active_referral_codes of this AccountAnalytics.

        Total Number of active referral codes inside the account  # noqa: E501

        :param active_referral_codes: The active_referral_codes of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if active_referral_codes is None:
            raise ValueError("Invalid value for `active_referral_codes`, must not be `None`")  # noqa: E501

        self._active_referral_codes = active_referral_codes

    @property
    def expired_referral_codes(self):
        """Gets the expired_referral_codes of this AccountAnalytics.  # noqa: E501

        Total Number of expired referral codes inside the account  # noqa: E501

        :return: The expired_referral_codes of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._expired_referral_codes

    @expired_referral_codes.setter
    def expired_referral_codes(self, expired_referral_codes):
        """Sets the expired_referral_codes of this AccountAnalytics.

        Total Number of expired referral codes inside the account  # noqa: E501

        :param expired_referral_codes: The expired_referral_codes of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if expired_referral_codes is None:
            raise ValueError("Invalid value for `expired_referral_codes`, must not be `None`")  # noqa: E501

        self._expired_referral_codes = expired_referral_codes

    @property
    def users(self):
        """Gets the users of this AccountAnalytics.  # noqa: E501

        Total Number of users inside the account  # noqa: E501

        :return: The users of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this AccountAnalytics.

        Total Number of users inside the account  # noqa: E501

        :param users: The users of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

    @property
    def roles(self):
        """Gets the roles of this AccountAnalytics.  # noqa: E501

        Total Number of roles inside the account  # noqa: E501

        :return: The roles of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AccountAnalytics.

        Total Number of roles inside the account  # noqa: E501

        :param roles: The roles of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")  # noqa: E501

        self._roles = roles

    @property
    def webhooks(self):
        """Gets the webhooks of this AccountAnalytics.  # noqa: E501

        Total Number of webhooks inside the account  # noqa: E501

        :return: The webhooks of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        """Sets the webhooks of this AccountAnalytics.

        Total Number of webhooks inside the account  # noqa: E501

        :param webhooks: The webhooks of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if webhooks is None:
            raise ValueError("Invalid value for `webhooks`, must not be `None`")  # noqa: E501

        self._webhooks = webhooks

    @property
    def loyalty_programs(self):
        """Gets the loyalty_programs of this AccountAnalytics.  # noqa: E501

        Total Number of loyalty programs inside the account  # noqa: E501

        :return: The loyalty_programs of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._loyalty_programs

    @loyalty_programs.setter
    def loyalty_programs(self, loyalty_programs):
        """Sets the loyalty_programs of this AccountAnalytics.

        Total Number of loyalty programs inside the account  # noqa: E501

        :param loyalty_programs: The loyalty_programs of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if loyalty_programs is None:
            raise ValueError("Invalid value for `loyalty_programs`, must not be `None`")  # noqa: E501

        self._loyalty_programs = loyalty_programs

    @property
    def active_rules(self):
        """Gets the active_rules of this AccountAnalytics.  # noqa: E501

        Total Number of active rules in the account  # noqa: E501

        :return: The active_rules of this AccountAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._active_rules

    @active_rules.setter
    def active_rules(self, active_rules):
        """Sets the active_rules of this AccountAnalytics.

        Total Number of active rules in the account  # noqa: E501

        :param active_rules: The active_rules of this AccountAnalytics.  # noqa: E501
        :type: int
        """
        if active_rules is None:
            raise ValueError("Invalid value for `active_rules`, must not be `None`")  # noqa: E501

        self._active_rules = active_rules

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AccountAnalytics, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountAnalytics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
