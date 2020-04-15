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


class CampaignAnalytics(object):
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
        'date': 'datetime',
        'campaign_revenue': 'float',
        'total_campaign_revenue': 'float',
        'campaign_refund': 'float',
        'total_campaign_refund': 'float',
        'campaign_discount_costs': 'float',
        'total_campaign_discount_costs': 'float',
        'campaign_refunded_discounts': 'float',
        'total_campaign_refunded_discounts': 'float',
        'campaign_free_items': 'int',
        'total_campaign_free_items': 'int',
        'coupon_redemptions': 'int',
        'total_coupon_redemptions': 'int',
        'coupon_rolledback_redemptions': 'int',
        'total_coupon_rolledback_redemptions': 'int',
        'referral_redemptions': 'int',
        'total_referral_redemptions': 'int',
        'coupons_created': 'int',
        'total_coupons_created': 'int',
        'referrals_created': 'int',
        'total_referrals_created': 'int'
    }

    attribute_map = {
        'date': 'date',
        'campaign_revenue': 'campaignRevenue',
        'total_campaign_revenue': 'totalCampaignRevenue',
        'campaign_refund': 'campaignRefund',
        'total_campaign_refund': 'totalCampaignRefund',
        'campaign_discount_costs': 'campaignDiscountCosts',
        'total_campaign_discount_costs': 'totalCampaignDiscountCosts',
        'campaign_refunded_discounts': 'campaignRefundedDiscounts',
        'total_campaign_refunded_discounts': 'totalCampaignRefundedDiscounts',
        'campaign_free_items': 'campaignFreeItems',
        'total_campaign_free_items': 'totalCampaignFreeItems',
        'coupon_redemptions': 'couponRedemptions',
        'total_coupon_redemptions': 'totalCouponRedemptions',
        'coupon_rolledback_redemptions': 'couponRolledbackRedemptions',
        'total_coupon_rolledback_redemptions': 'totalCouponRolledbackRedemptions',
        'referral_redemptions': 'referralRedemptions',
        'total_referral_redemptions': 'totalReferralRedemptions',
        'coupons_created': 'couponsCreated',
        'total_coupons_created': 'totalCouponsCreated',
        'referrals_created': 'referralsCreated',
        'total_referrals_created': 'totalReferralsCreated'
    }

    def __init__(self, date=None, campaign_revenue=None, total_campaign_revenue=None, campaign_refund=None, total_campaign_refund=None, campaign_discount_costs=None, total_campaign_discount_costs=None, campaign_refunded_discounts=None, total_campaign_refunded_discounts=None, campaign_free_items=None, total_campaign_free_items=None, coupon_redemptions=None, total_coupon_redemptions=None, coupon_rolledback_redemptions=None, total_coupon_rolledback_redemptions=None, referral_redemptions=None, total_referral_redemptions=None, coupons_created=None, total_coupons_created=None, referrals_created=None, total_referrals_created=None, local_vars_configuration=None):  # noqa: E501
        """CampaignAnalytics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._campaign_revenue = None
        self._total_campaign_revenue = None
        self._campaign_refund = None
        self._total_campaign_refund = None
        self._campaign_discount_costs = None
        self._total_campaign_discount_costs = None
        self._campaign_refunded_discounts = None
        self._total_campaign_refunded_discounts = None
        self._campaign_free_items = None
        self._total_campaign_free_items = None
        self._coupon_redemptions = None
        self._total_coupon_redemptions = None
        self._coupon_rolledback_redemptions = None
        self._total_coupon_rolledback_redemptions = None
        self._referral_redemptions = None
        self._total_referral_redemptions = None
        self._coupons_created = None
        self._total_coupons_created = None
        self._referrals_created = None
        self._total_referrals_created = None
        self.discriminator = None

        self.date = date
        self.campaign_revenue = campaign_revenue
        self.total_campaign_revenue = total_campaign_revenue
        self.campaign_refund = campaign_refund
        self.total_campaign_refund = total_campaign_refund
        self.campaign_discount_costs = campaign_discount_costs
        self.total_campaign_discount_costs = total_campaign_discount_costs
        self.campaign_refunded_discounts = campaign_refunded_discounts
        self.total_campaign_refunded_discounts = total_campaign_refunded_discounts
        self.campaign_free_items = campaign_free_items
        self.total_campaign_free_items = total_campaign_free_items
        self.coupon_redemptions = coupon_redemptions
        self.total_coupon_redemptions = total_coupon_redemptions
        self.coupon_rolledback_redemptions = coupon_rolledback_redemptions
        self.total_coupon_rolledback_redemptions = total_coupon_rolledback_redemptions
        self.referral_redemptions = referral_redemptions
        self.total_referral_redemptions = total_referral_redemptions
        self.coupons_created = coupons_created
        self.total_coupons_created = total_coupons_created
        self.referrals_created = referrals_created
        self.total_referrals_created = total_referrals_created

    @property
    def date(self):
        """Gets the date of this CampaignAnalytics.  # noqa: E501


        :return: The date of this CampaignAnalytics.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this CampaignAnalytics.


        :param date: The date of this CampaignAnalytics.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def campaign_revenue(self):
        """Gets the campaign_revenue of this CampaignAnalytics.  # noqa: E501

        Amount of revenue in this campaign (for coupon or discount sessions).  # noqa: E501

        :return: The campaign_revenue of this CampaignAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._campaign_revenue

    @campaign_revenue.setter
    def campaign_revenue(self, campaign_revenue):
        """Sets the campaign_revenue of this CampaignAnalytics.

        Amount of revenue in this campaign (for coupon or discount sessions).  # noqa: E501

        :param campaign_revenue: The campaign_revenue of this CampaignAnalytics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and campaign_revenue is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_revenue`, must not be `None`")  # noqa: E501

        self._campaign_revenue = campaign_revenue

    @property
    def total_campaign_revenue(self):
        """Gets the total_campaign_revenue of this CampaignAnalytics.  # noqa: E501

        Amount of revenue in this campaign since it began (for coupon or discount sessions).  # noqa: E501

        :return: The total_campaign_revenue of this CampaignAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._total_campaign_revenue

    @total_campaign_revenue.setter
    def total_campaign_revenue(self, total_campaign_revenue):
        """Sets the total_campaign_revenue of this CampaignAnalytics.

        Amount of revenue in this campaign since it began (for coupon or discount sessions).  # noqa: E501

        :param total_campaign_revenue: The total_campaign_revenue of this CampaignAnalytics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_campaign_revenue is None:  # noqa: E501
            raise ValueError("Invalid value for `total_campaign_revenue`, must not be `None`")  # noqa: E501

        self._total_campaign_revenue = total_campaign_revenue

    @property
    def campaign_refund(self):
        """Gets the campaign_refund of this CampaignAnalytics.  # noqa: E501

        Amount of refunds in this campaign (for coupon or discount sessions).  # noqa: E501

        :return: The campaign_refund of this CampaignAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._campaign_refund

    @campaign_refund.setter
    def campaign_refund(self, campaign_refund):
        """Sets the campaign_refund of this CampaignAnalytics.

        Amount of refunds in this campaign (for coupon or discount sessions).  # noqa: E501

        :param campaign_refund: The campaign_refund of this CampaignAnalytics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and campaign_refund is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_refund`, must not be `None`")  # noqa: E501

        self._campaign_refund = campaign_refund

    @property
    def total_campaign_refund(self):
        """Gets the total_campaign_refund of this CampaignAnalytics.  # noqa: E501

        Amount of refunds in this campaign since it began (for coupon or discount sessions).  # noqa: E501

        :return: The total_campaign_refund of this CampaignAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._total_campaign_refund

    @total_campaign_refund.setter
    def total_campaign_refund(self, total_campaign_refund):
        """Sets the total_campaign_refund of this CampaignAnalytics.

        Amount of refunds in this campaign since it began (for coupon or discount sessions).  # noqa: E501

        :param total_campaign_refund: The total_campaign_refund of this CampaignAnalytics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_campaign_refund is None:  # noqa: E501
            raise ValueError("Invalid value for `total_campaign_refund`, must not be `None`")  # noqa: E501

        self._total_campaign_refund = total_campaign_refund

    @property
    def campaign_discount_costs(self):
        """Gets the campaign_discount_costs of this CampaignAnalytics.  # noqa: E501

        Amount of cost caused by discounts given in the campaign.  # noqa: E501

        :return: The campaign_discount_costs of this CampaignAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._campaign_discount_costs

    @campaign_discount_costs.setter
    def campaign_discount_costs(self, campaign_discount_costs):
        """Sets the campaign_discount_costs of this CampaignAnalytics.

        Amount of cost caused by discounts given in the campaign.  # noqa: E501

        :param campaign_discount_costs: The campaign_discount_costs of this CampaignAnalytics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and campaign_discount_costs is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_discount_costs`, must not be `None`")  # noqa: E501

        self._campaign_discount_costs = campaign_discount_costs

    @property
    def total_campaign_discount_costs(self):
        """Gets the total_campaign_discount_costs of this CampaignAnalytics.  # noqa: E501

        Amount of cost caused by discounts given in the campaign since it began.  # noqa: E501

        :return: The total_campaign_discount_costs of this CampaignAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._total_campaign_discount_costs

    @total_campaign_discount_costs.setter
    def total_campaign_discount_costs(self, total_campaign_discount_costs):
        """Sets the total_campaign_discount_costs of this CampaignAnalytics.

        Amount of cost caused by discounts given in the campaign since it began.  # noqa: E501

        :param total_campaign_discount_costs: The total_campaign_discount_costs of this CampaignAnalytics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_campaign_discount_costs is None:  # noqa: E501
            raise ValueError("Invalid value for `total_campaign_discount_costs`, must not be `None`")  # noqa: E501

        self._total_campaign_discount_costs = total_campaign_discount_costs

    @property
    def campaign_refunded_discounts(self):
        """Gets the campaign_refunded_discounts of this CampaignAnalytics.  # noqa: E501

        Amount of discounts rolledback due to refund in the campaign.  # noqa: E501

        :return: The campaign_refunded_discounts of this CampaignAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._campaign_refunded_discounts

    @campaign_refunded_discounts.setter
    def campaign_refunded_discounts(self, campaign_refunded_discounts):
        """Sets the campaign_refunded_discounts of this CampaignAnalytics.

        Amount of discounts rolledback due to refund in the campaign.  # noqa: E501

        :param campaign_refunded_discounts: The campaign_refunded_discounts of this CampaignAnalytics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and campaign_refunded_discounts is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_refunded_discounts`, must not be `None`")  # noqa: E501

        self._campaign_refunded_discounts = campaign_refunded_discounts

    @property
    def total_campaign_refunded_discounts(self):
        """Gets the total_campaign_refunded_discounts of this CampaignAnalytics.  # noqa: E501

        Amount of discounts rolledback due to refund in the campaign since it began.  # noqa: E501

        :return: The total_campaign_refunded_discounts of this CampaignAnalytics.  # noqa: E501
        :rtype: float
        """
        return self._total_campaign_refunded_discounts

    @total_campaign_refunded_discounts.setter
    def total_campaign_refunded_discounts(self, total_campaign_refunded_discounts):
        """Sets the total_campaign_refunded_discounts of this CampaignAnalytics.

        Amount of discounts rolledback due to refund in the campaign since it began.  # noqa: E501

        :param total_campaign_refunded_discounts: The total_campaign_refunded_discounts of this CampaignAnalytics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_campaign_refunded_discounts is None:  # noqa: E501
            raise ValueError("Invalid value for `total_campaign_refunded_discounts`, must not be `None`")  # noqa: E501

        self._total_campaign_refunded_discounts = total_campaign_refunded_discounts

    @property
    def campaign_free_items(self):
        """Gets the campaign_free_items of this CampaignAnalytics.  # noqa: E501

        Amount of free items given in the campaign.  # noqa: E501

        :return: The campaign_free_items of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._campaign_free_items

    @campaign_free_items.setter
    def campaign_free_items(self, campaign_free_items):
        """Sets the campaign_free_items of this CampaignAnalytics.

        Amount of free items given in the campaign.  # noqa: E501

        :param campaign_free_items: The campaign_free_items of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_free_items is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_free_items`, must not be `None`")  # noqa: E501

        self._campaign_free_items = campaign_free_items

    @property
    def total_campaign_free_items(self):
        """Gets the total_campaign_free_items of this CampaignAnalytics.  # noqa: E501

        Amount of free items given in the campaign since it began.  # noqa: E501

        :return: The total_campaign_free_items of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._total_campaign_free_items

    @total_campaign_free_items.setter
    def total_campaign_free_items(self, total_campaign_free_items):
        """Sets the total_campaign_free_items of this CampaignAnalytics.

        Amount of free items given in the campaign since it began.  # noqa: E501

        :param total_campaign_free_items: The total_campaign_free_items of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_campaign_free_items is None:  # noqa: E501
            raise ValueError("Invalid value for `total_campaign_free_items`, must not be `None`")  # noqa: E501

        self._total_campaign_free_items = total_campaign_free_items

    @property
    def coupon_redemptions(self):
        """Gets the coupon_redemptions of this CampaignAnalytics.  # noqa: E501

        Number of coupon redemptions in the campaign.  # noqa: E501

        :return: The coupon_redemptions of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._coupon_redemptions

    @coupon_redemptions.setter
    def coupon_redemptions(self, coupon_redemptions):
        """Sets the coupon_redemptions of this CampaignAnalytics.

        Number of coupon redemptions in the campaign.  # noqa: E501

        :param coupon_redemptions: The coupon_redemptions of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and coupon_redemptions is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_redemptions`, must not be `None`")  # noqa: E501

        self._coupon_redemptions = coupon_redemptions

    @property
    def total_coupon_redemptions(self):
        """Gets the total_coupon_redemptions of this CampaignAnalytics.  # noqa: E501

        Number of coupon redemptions in the campaign since it began.  # noqa: E501

        :return: The total_coupon_redemptions of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._total_coupon_redemptions

    @total_coupon_redemptions.setter
    def total_coupon_redemptions(self, total_coupon_redemptions):
        """Sets the total_coupon_redemptions of this CampaignAnalytics.

        Number of coupon redemptions in the campaign since it began.  # noqa: E501

        :param total_coupon_redemptions: The total_coupon_redemptions of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_coupon_redemptions is None:  # noqa: E501
            raise ValueError("Invalid value for `total_coupon_redemptions`, must not be `None`")  # noqa: E501

        self._total_coupon_redemptions = total_coupon_redemptions

    @property
    def coupon_rolledback_redemptions(self):
        """Gets the coupon_rolledback_redemptions of this CampaignAnalytics.  # noqa: E501

        Number of coupon redemptions that have been rolled back (due to canceling closed session) in the campaign.  # noqa: E501

        :return: The coupon_rolledback_redemptions of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._coupon_rolledback_redemptions

    @coupon_rolledback_redemptions.setter
    def coupon_rolledback_redemptions(self, coupon_rolledback_redemptions):
        """Sets the coupon_rolledback_redemptions of this CampaignAnalytics.

        Number of coupon redemptions that have been rolled back (due to canceling closed session) in the campaign.  # noqa: E501

        :param coupon_rolledback_redemptions: The coupon_rolledback_redemptions of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and coupon_rolledback_redemptions is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_rolledback_redemptions`, must not be `None`")  # noqa: E501

        self._coupon_rolledback_redemptions = coupon_rolledback_redemptions

    @property
    def total_coupon_rolledback_redemptions(self):
        """Gets the total_coupon_rolledback_redemptions of this CampaignAnalytics.  # noqa: E501

        Number of coupon redemptions that have been rolled back (due to canceling closed session) in the campaign since it began.  # noqa: E501

        :return: The total_coupon_rolledback_redemptions of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._total_coupon_rolledback_redemptions

    @total_coupon_rolledback_redemptions.setter
    def total_coupon_rolledback_redemptions(self, total_coupon_rolledback_redemptions):
        """Sets the total_coupon_rolledback_redemptions of this CampaignAnalytics.

        Number of coupon redemptions that have been rolled back (due to canceling closed session) in the campaign since it began.  # noqa: E501

        :param total_coupon_rolledback_redemptions: The total_coupon_rolledback_redemptions of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_coupon_rolledback_redemptions is None:  # noqa: E501
            raise ValueError("Invalid value for `total_coupon_rolledback_redemptions`, must not be `None`")  # noqa: E501

        self._total_coupon_rolledback_redemptions = total_coupon_rolledback_redemptions

    @property
    def referral_redemptions(self):
        """Gets the referral_redemptions of this CampaignAnalytics.  # noqa: E501

        Number of referral redemptions in the campaign.  # noqa: E501

        :return: The referral_redemptions of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._referral_redemptions

    @referral_redemptions.setter
    def referral_redemptions(self, referral_redemptions):
        """Sets the referral_redemptions of this CampaignAnalytics.

        Number of referral redemptions in the campaign.  # noqa: E501

        :param referral_redemptions: The referral_redemptions of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and referral_redemptions is None:  # noqa: E501
            raise ValueError("Invalid value for `referral_redemptions`, must not be `None`")  # noqa: E501

        self._referral_redemptions = referral_redemptions

    @property
    def total_referral_redemptions(self):
        """Gets the total_referral_redemptions of this CampaignAnalytics.  # noqa: E501

        Number of referral redemptions in the campaign since it began.  # noqa: E501

        :return: The total_referral_redemptions of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._total_referral_redemptions

    @total_referral_redemptions.setter
    def total_referral_redemptions(self, total_referral_redemptions):
        """Sets the total_referral_redemptions of this CampaignAnalytics.

        Number of referral redemptions in the campaign since it began.  # noqa: E501

        :param total_referral_redemptions: The total_referral_redemptions of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_referral_redemptions is None:  # noqa: E501
            raise ValueError("Invalid value for `total_referral_redemptions`, must not be `None`")  # noqa: E501

        self._total_referral_redemptions = total_referral_redemptions

    @property
    def coupons_created(self):
        """Gets the coupons_created of this CampaignAnalytics.  # noqa: E501

        Number of coupons created in the campaign by the rule engine.  # noqa: E501

        :return: The coupons_created of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._coupons_created

    @coupons_created.setter
    def coupons_created(self, coupons_created):
        """Sets the coupons_created of this CampaignAnalytics.

        Number of coupons created in the campaign by the rule engine.  # noqa: E501

        :param coupons_created: The coupons_created of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and coupons_created is None:  # noqa: E501
            raise ValueError("Invalid value for `coupons_created`, must not be `None`")  # noqa: E501

        self._coupons_created = coupons_created

    @property
    def total_coupons_created(self):
        """Gets the total_coupons_created of this CampaignAnalytics.  # noqa: E501

        Number of coupons created in the campaign by the rule engine since it began.  # noqa: E501

        :return: The total_coupons_created of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._total_coupons_created

    @total_coupons_created.setter
    def total_coupons_created(self, total_coupons_created):
        """Sets the total_coupons_created of this CampaignAnalytics.

        Number of coupons created in the campaign by the rule engine since it began.  # noqa: E501

        :param total_coupons_created: The total_coupons_created of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_coupons_created is None:  # noqa: E501
            raise ValueError("Invalid value for `total_coupons_created`, must not be `None`")  # noqa: E501

        self._total_coupons_created = total_coupons_created

    @property
    def referrals_created(self):
        """Gets the referrals_created of this CampaignAnalytics.  # noqa: E501

        Number of referrals created in the campaign by the rule engine.  # noqa: E501

        :return: The referrals_created of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._referrals_created

    @referrals_created.setter
    def referrals_created(self, referrals_created):
        """Sets the referrals_created of this CampaignAnalytics.

        Number of referrals created in the campaign by the rule engine.  # noqa: E501

        :param referrals_created: The referrals_created of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and referrals_created is None:  # noqa: E501
            raise ValueError("Invalid value for `referrals_created`, must not be `None`")  # noqa: E501

        self._referrals_created = referrals_created

    @property
    def total_referrals_created(self):
        """Gets the total_referrals_created of this CampaignAnalytics.  # noqa: E501

        Number of referrals created in the campaign by the rule engine since it began.  # noqa: E501

        :return: The total_referrals_created of this CampaignAnalytics.  # noqa: E501
        :rtype: int
        """
        return self._total_referrals_created

    @total_referrals_created.setter
    def total_referrals_created(self, total_referrals_created):
        """Sets the total_referrals_created of this CampaignAnalytics.

        Number of referrals created in the campaign by the rule engine since it began.  # noqa: E501

        :param total_referrals_created: The total_referrals_created of this CampaignAnalytics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_referrals_created is None:  # noqa: E501
            raise ValueError("Invalid value for `total_referrals_created`, must not be `None`")  # noqa: E501

        self._total_referrals_created = total_referrals_created

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
        if not isinstance(other, CampaignAnalytics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignAnalytics):
            return True

        return self.to_dict() != other.to_dict()
