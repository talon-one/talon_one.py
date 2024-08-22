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


class AdditionalCampaignProperties(object):
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
        'budgets': 'list[CampaignBudget]',
        'coupon_redemption_count': 'int',
        'referral_redemption_count': 'int',
        'discount_count': 'float',
        'discount_effect_count': 'int',
        'coupon_creation_count': 'int',
        'custom_effect_count': 'int',
        'referral_creation_count': 'int',
        'add_free_item_effect_count': 'int',
        'awarded_giveaways_count': 'int',
        'created_loyalty_points_count': 'float',
        'created_loyalty_points_effect_count': 'int',
        'redeemed_loyalty_points_count': 'float',
        'redeemed_loyalty_points_effect_count': 'int',
        'call_api_effect_count': 'int',
        'reservecoupon_effect_count': 'int',
        'last_activity': 'datetime',
        'updated': 'datetime',
        'created_by': 'str',
        'updated_by': 'str',
        'template_id': 'int',
        'frontend_state': 'str',
        'stores_imported': 'bool'
    }

    attribute_map = {
        'budgets': 'budgets',
        'coupon_redemption_count': 'couponRedemptionCount',
        'referral_redemption_count': 'referralRedemptionCount',
        'discount_count': 'discountCount',
        'discount_effect_count': 'discountEffectCount',
        'coupon_creation_count': 'couponCreationCount',
        'custom_effect_count': 'customEffectCount',
        'referral_creation_count': 'referralCreationCount',
        'add_free_item_effect_count': 'addFreeItemEffectCount',
        'awarded_giveaways_count': 'awardedGiveawaysCount',
        'created_loyalty_points_count': 'createdLoyaltyPointsCount',
        'created_loyalty_points_effect_count': 'createdLoyaltyPointsEffectCount',
        'redeemed_loyalty_points_count': 'redeemedLoyaltyPointsCount',
        'redeemed_loyalty_points_effect_count': 'redeemedLoyaltyPointsEffectCount',
        'call_api_effect_count': 'callApiEffectCount',
        'reservecoupon_effect_count': 'reservecouponEffectCount',
        'last_activity': 'lastActivity',
        'updated': 'updated',
        'created_by': 'createdBy',
        'updated_by': 'updatedBy',
        'template_id': 'templateId',
        'frontend_state': 'frontendState',
        'stores_imported': 'storesImported'
    }

    def __init__(self, budgets=None, coupon_redemption_count=None, referral_redemption_count=None, discount_count=None, discount_effect_count=None, coupon_creation_count=None, custom_effect_count=None, referral_creation_count=None, add_free_item_effect_count=None, awarded_giveaways_count=None, created_loyalty_points_count=None, created_loyalty_points_effect_count=None, redeemed_loyalty_points_count=None, redeemed_loyalty_points_effect_count=None, call_api_effect_count=None, reservecoupon_effect_count=None, last_activity=None, updated=None, created_by=None, updated_by=None, template_id=None, frontend_state=None, stores_imported=None, local_vars_configuration=None):  # noqa: E501
        """AdditionalCampaignProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._budgets = None
        self._coupon_redemption_count = None
        self._referral_redemption_count = None
        self._discount_count = None
        self._discount_effect_count = None
        self._coupon_creation_count = None
        self._custom_effect_count = None
        self._referral_creation_count = None
        self._add_free_item_effect_count = None
        self._awarded_giveaways_count = None
        self._created_loyalty_points_count = None
        self._created_loyalty_points_effect_count = None
        self._redeemed_loyalty_points_count = None
        self._redeemed_loyalty_points_effect_count = None
        self._call_api_effect_count = None
        self._reservecoupon_effect_count = None
        self._last_activity = None
        self._updated = None
        self._created_by = None
        self._updated_by = None
        self._template_id = None
        self._frontend_state = None
        self._stores_imported = None
        self.discriminator = None

        self.budgets = budgets
        if coupon_redemption_count is not None:
            self.coupon_redemption_count = coupon_redemption_count
        if referral_redemption_count is not None:
            self.referral_redemption_count = referral_redemption_count
        if discount_count is not None:
            self.discount_count = discount_count
        if discount_effect_count is not None:
            self.discount_effect_count = discount_effect_count
        if coupon_creation_count is not None:
            self.coupon_creation_count = coupon_creation_count
        if custom_effect_count is not None:
            self.custom_effect_count = custom_effect_count
        if referral_creation_count is not None:
            self.referral_creation_count = referral_creation_count
        if add_free_item_effect_count is not None:
            self.add_free_item_effect_count = add_free_item_effect_count
        if awarded_giveaways_count is not None:
            self.awarded_giveaways_count = awarded_giveaways_count
        if created_loyalty_points_count is not None:
            self.created_loyalty_points_count = created_loyalty_points_count
        if created_loyalty_points_effect_count is not None:
            self.created_loyalty_points_effect_count = created_loyalty_points_effect_count
        if redeemed_loyalty_points_count is not None:
            self.redeemed_loyalty_points_count = redeemed_loyalty_points_count
        if redeemed_loyalty_points_effect_count is not None:
            self.redeemed_loyalty_points_effect_count = redeemed_loyalty_points_effect_count
        if call_api_effect_count is not None:
            self.call_api_effect_count = call_api_effect_count
        if reservecoupon_effect_count is not None:
            self.reservecoupon_effect_count = reservecoupon_effect_count
        if last_activity is not None:
            self.last_activity = last_activity
        if updated is not None:
            self.updated = updated
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if template_id is not None:
            self.template_id = template_id
        self.frontend_state = frontend_state
        self.stores_imported = stores_imported

    @property
    def budgets(self):
        """Gets the budgets of this AdditionalCampaignProperties.  # noqa: E501

        A list of all the budgets that are defined by this campaign and their usage.  **Note:** Budgets that are not defined do not appear in this list and their usage is not counted until they are defined.   # noqa: E501

        :return: The budgets of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: list[CampaignBudget]
        """
        return self._budgets

    @budgets.setter
    def budgets(self, budgets):
        """Sets the budgets of this AdditionalCampaignProperties.

        A list of all the budgets that are defined by this campaign and their usage.  **Note:** Budgets that are not defined do not appear in this list and their usage is not counted until they are defined.   # noqa: E501

        :param budgets: The budgets of this AdditionalCampaignProperties.  # noqa: E501
        :type: list[CampaignBudget]
        """
        if self.local_vars_configuration.client_side_validation and budgets is None:  # noqa: E501
            raise ValueError("Invalid value for `budgets`, must not be `None`")  # noqa: E501

        self._budgets = budgets

    @property
    def coupon_redemption_count(self):
        """Gets the coupon_redemption_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Number of coupons redeemed in the campaign.   # noqa: E501

        :return: The coupon_redemption_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._coupon_redemption_count

    @coupon_redemption_count.setter
    def coupon_redemption_count(self, coupon_redemption_count):
        """Sets the coupon_redemption_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Number of coupons redeemed in the campaign.   # noqa: E501

        :param coupon_redemption_count: The coupon_redemption_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._coupon_redemption_count = coupon_redemption_count

    @property
    def referral_redemption_count(self):
        """Gets the referral_redemption_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Number of referral codes redeemed in the campaign.   # noqa: E501

        :return: The referral_redemption_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._referral_redemption_count

    @referral_redemption_count.setter
    def referral_redemption_count(self, referral_redemption_count):
        """Sets the referral_redemption_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Number of referral codes redeemed in the campaign.   # noqa: E501

        :param referral_redemption_count: The referral_redemption_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._referral_redemption_count = referral_redemption_count

    @property
    def discount_count(self):
        """Gets the discount_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total amount of discounts redeemed in the campaign.   # noqa: E501

        :return: The discount_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: float
        """
        return self._discount_count

    @discount_count.setter
    def discount_count(self, discount_count):
        """Sets the discount_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total amount of discounts redeemed in the campaign.   # noqa: E501

        :param discount_count: The discount_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: float
        """

        self._discount_count = discount_count

    @property
    def discount_effect_count(self):
        """Gets the discount_effect_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of times discounts were redeemed in this campaign.   # noqa: E501

        :return: The discount_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._discount_effect_count

    @discount_effect_count.setter
    def discount_effect_count(self, discount_effect_count):
        """Sets the discount_effect_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of times discounts were redeemed in this campaign.   # noqa: E501

        :param discount_effect_count: The discount_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._discount_effect_count = discount_effect_count

    @property
    def coupon_creation_count(self):
        """Gets the coupon_creation_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of coupons created by rules in this campaign.   # noqa: E501

        :return: The coupon_creation_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._coupon_creation_count

    @coupon_creation_count.setter
    def coupon_creation_count(self, coupon_creation_count):
        """Sets the coupon_creation_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of coupons created by rules in this campaign.   # noqa: E501

        :param coupon_creation_count: The coupon_creation_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._coupon_creation_count = coupon_creation_count

    @property
    def custom_effect_count(self):
        """Gets the custom_effect_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of custom effects triggered by rules in this campaign.   # noqa: E501

        :return: The custom_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._custom_effect_count

    @custom_effect_count.setter
    def custom_effect_count(self, custom_effect_count):
        """Sets the custom_effect_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of custom effects triggered by rules in this campaign.   # noqa: E501

        :param custom_effect_count: The custom_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._custom_effect_count = custom_effect_count

    @property
    def referral_creation_count(self):
        """Gets the referral_creation_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of referrals created by rules in this campaign.   # noqa: E501

        :return: The referral_creation_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._referral_creation_count

    @referral_creation_count.setter
    def referral_creation_count(self, referral_creation_count):
        """Sets the referral_creation_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of referrals created by rules in this campaign.   # noqa: E501

        :param referral_creation_count: The referral_creation_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._referral_creation_count = referral_creation_count

    @property
    def add_free_item_effect_count(self):
        """Gets the add_free_item_effect_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of times the [add free item effect](https://docs.talon.one/docs/dev/integration-api/api-effects#addfreeitem) can be triggered in this campaign.   # noqa: E501

        :return: The add_free_item_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._add_free_item_effect_count

    @add_free_item_effect_count.setter
    def add_free_item_effect_count(self, add_free_item_effect_count):
        """Sets the add_free_item_effect_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of times the [add free item effect](https://docs.talon.one/docs/dev/integration-api/api-effects#addfreeitem) can be triggered in this campaign.   # noqa: E501

        :param add_free_item_effect_count: The add_free_item_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._add_free_item_effect_count = add_free_item_effect_count

    @property
    def awarded_giveaways_count(self):
        """Gets the awarded_giveaways_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of giveaways awarded by rules in this campaign.   # noqa: E501

        :return: The awarded_giveaways_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._awarded_giveaways_count

    @awarded_giveaways_count.setter
    def awarded_giveaways_count(self, awarded_giveaways_count):
        """Sets the awarded_giveaways_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of giveaways awarded by rules in this campaign.   # noqa: E501

        :param awarded_giveaways_count: The awarded_giveaways_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._awarded_giveaways_count = awarded_giveaways_count

    @property
    def created_loyalty_points_count(self):
        """Gets the created_loyalty_points_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty points created by rules in this campaign.   # noqa: E501

        :return: The created_loyalty_points_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: float
        """
        return self._created_loyalty_points_count

    @created_loyalty_points_count.setter
    def created_loyalty_points_count(self, created_loyalty_points_count):
        """Sets the created_loyalty_points_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty points created by rules in this campaign.   # noqa: E501

        :param created_loyalty_points_count: The created_loyalty_points_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: float
        """

        self._created_loyalty_points_count = created_loyalty_points_count

    @property
    def created_loyalty_points_effect_count(self):
        """Gets the created_loyalty_points_effect_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty point creation effects triggered by rules in this campaign.   # noqa: E501

        :return: The created_loyalty_points_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._created_loyalty_points_effect_count

    @created_loyalty_points_effect_count.setter
    def created_loyalty_points_effect_count(self, created_loyalty_points_effect_count):
        """Sets the created_loyalty_points_effect_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty point creation effects triggered by rules in this campaign.   # noqa: E501

        :param created_loyalty_points_effect_count: The created_loyalty_points_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._created_loyalty_points_effect_count = created_loyalty_points_effect_count

    @property
    def redeemed_loyalty_points_count(self):
        """Gets the redeemed_loyalty_points_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty points redeemed by rules in this campaign.   # noqa: E501

        :return: The redeemed_loyalty_points_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: float
        """
        return self._redeemed_loyalty_points_count

    @redeemed_loyalty_points_count.setter
    def redeemed_loyalty_points_count(self, redeemed_loyalty_points_count):
        """Sets the redeemed_loyalty_points_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty points redeemed by rules in this campaign.   # noqa: E501

        :param redeemed_loyalty_points_count: The redeemed_loyalty_points_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: float
        """

        self._redeemed_loyalty_points_count = redeemed_loyalty_points_count

    @property
    def redeemed_loyalty_points_effect_count(self):
        """Gets the redeemed_loyalty_points_effect_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty point redemption effects triggered by rules in this campaign.   # noqa: E501

        :return: The redeemed_loyalty_points_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._redeemed_loyalty_points_effect_count

    @redeemed_loyalty_points_effect_count.setter
    def redeemed_loyalty_points_effect_count(self, redeemed_loyalty_points_effect_count):
        """Sets the redeemed_loyalty_points_effect_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of loyalty point redemption effects triggered by rules in this campaign.   # noqa: E501

        :param redeemed_loyalty_points_effect_count: The redeemed_loyalty_points_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._redeemed_loyalty_points_effect_count = redeemed_loyalty_points_effect_count

    @property
    def call_api_effect_count(self):
        """Gets the call_api_effect_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of webhooks triggered by rules in this campaign.   # noqa: E501

        :return: The call_api_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._call_api_effect_count

    @call_api_effect_count.setter
    def call_api_effect_count(self, call_api_effect_count):
        """Sets the call_api_effect_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of webhooks triggered by rules in this campaign.   # noqa: E501

        :param call_api_effect_count: The call_api_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._call_api_effect_count = call_api_effect_count

    @property
    def reservecoupon_effect_count(self):
        """Gets the reservecoupon_effect_count of this AdditionalCampaignProperties.  # noqa: E501

        This property is **deprecated**. The count should be available under *budgets* property. Total number of reserve coupon effects triggered by rules in this campaign.   # noqa: E501

        :return: The reservecoupon_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._reservecoupon_effect_count

    @reservecoupon_effect_count.setter
    def reservecoupon_effect_count(self, reservecoupon_effect_count):
        """Sets the reservecoupon_effect_count of this AdditionalCampaignProperties.

        This property is **deprecated**. The count should be available under *budgets* property. Total number of reserve coupon effects triggered by rules in this campaign.   # noqa: E501

        :param reservecoupon_effect_count: The reservecoupon_effect_count of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._reservecoupon_effect_count = reservecoupon_effect_count

    @property
    def last_activity(self):
        """Gets the last_activity of this AdditionalCampaignProperties.  # noqa: E501

        Timestamp of the most recent event received by this campaign.  # noqa: E501

        :return: The last_activity of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """Sets the last_activity of this AdditionalCampaignProperties.

        Timestamp of the most recent event received by this campaign.  # noqa: E501

        :param last_activity: The last_activity of this AdditionalCampaignProperties.  # noqa: E501
        :type: datetime
        """

        self._last_activity = last_activity

    @property
    def updated(self):
        """Gets the updated of this AdditionalCampaignProperties.  # noqa: E501

        Timestamp of the most recent update to the campaign's property. Updates to external entities used in this campaign are **not** registered by this property, such as collection or coupon updates.   # noqa: E501

        :return: The updated of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this AdditionalCampaignProperties.

        Timestamp of the most recent update to the campaign's property. Updates to external entities used in this campaign are **not** registered by this property, such as collection or coupon updates.   # noqa: E501

        :param updated: The updated of this AdditionalCampaignProperties.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created_by(self):
        """Gets the created_by of this AdditionalCampaignProperties.  # noqa: E501

        Name of the user who created this campaign if available.  # noqa: E501

        :return: The created_by of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AdditionalCampaignProperties.

        Name of the user who created this campaign if available.  # noqa: E501

        :param created_by: The created_by of this AdditionalCampaignProperties.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this AdditionalCampaignProperties.  # noqa: E501

        Name of the user who last updated this campaign if available.  # noqa: E501

        :return: The updated_by of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this AdditionalCampaignProperties.

        Name of the user who last updated this campaign if available.  # noqa: E501

        :param updated_by: The updated_by of this AdditionalCampaignProperties.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def template_id(self):
        """Gets the template_id of this AdditionalCampaignProperties.  # noqa: E501

        The ID of the Campaign Template this Campaign was created from.  # noqa: E501

        :return: The template_id of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this AdditionalCampaignProperties.

        The ID of the Campaign Template this Campaign was created from.  # noqa: E501

        :param template_id: The template_id of this AdditionalCampaignProperties.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def frontend_state(self):
        """Gets the frontend_state of this AdditionalCampaignProperties.  # noqa: E501

        A campaign state described exactly as in the Campaign Manager.  # noqa: E501

        :return: The frontend_state of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: str
        """
        return self._frontend_state

    @frontend_state.setter
    def frontend_state(self, frontend_state):
        """Sets the frontend_state of this AdditionalCampaignProperties.

        A campaign state described exactly as in the Campaign Manager.  # noqa: E501

        :param frontend_state: The frontend_state of this AdditionalCampaignProperties.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and frontend_state is None:  # noqa: E501
            raise ValueError("Invalid value for `frontend_state`, must not be `None`")  # noqa: E501
        allowed_values = ["expired", "scheduled", "running", "disabled", "archived"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and frontend_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `frontend_state` ({0}), must be one of {1}"  # noqa: E501
                .format(frontend_state, allowed_values)
            )

        self._frontend_state = frontend_state

    @property
    def stores_imported(self):
        """Gets the stores_imported of this AdditionalCampaignProperties.  # noqa: E501

        Indicates whether the linked stores were imported via a CSV file.  # noqa: E501

        :return: The stores_imported of this AdditionalCampaignProperties.  # noqa: E501
        :rtype: bool
        """
        return self._stores_imported

    @stores_imported.setter
    def stores_imported(self, stores_imported):
        """Sets the stores_imported of this AdditionalCampaignProperties.

        Indicates whether the linked stores were imported via a CSV file.  # noqa: E501

        :param stores_imported: The stores_imported of this AdditionalCampaignProperties.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and stores_imported is None:  # noqa: E501
            raise ValueError("Invalid value for `stores_imported`, must not be `None`")  # noqa: E501

        self._stores_imported = stores_imported

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
        if not isinstance(other, AdditionalCampaignProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdditionalCampaignProperties):
            return True

        return self.to_dict() != other.to_dict()
