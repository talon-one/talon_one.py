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


class Campaign(object):
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
        'id': 'int',
        'created': 'datetime',
        'application_id': 'int',
        'user_id': 'int',
        'name': 'str',
        'description': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'attributes': 'object',
        'state': 'str',
        'active_ruleset_id': 'int',
        'tags': 'list[str]',
        'features': 'list[str]',
        'coupon_settings': 'CodeGeneratorSettings',
        'referral_settings': 'CodeGeneratorSettings',
        'limits': 'list[LimitConfig]',
        'campaign_groups': 'list[int]',
        'coupon_redemption_count': 'int',
        'referral_redemption_count': 'int',
        'discount_count': 'float',
        'discount_effect_count': 'int',
        'coupon_creation_count': 'int',
        'referral_creation_count': 'int',
        'awarded_giveaways_count': 'int',
        'created_loyalty_points_count': 'float',
        'created_loyalty_points_effect_count': 'int',
        'redeemed_loyalty_points_count': 'float',
        'redeemed_loyalty_points_effect_count': 'int',
        'last_activity': 'datetime',
        'updated': 'datetime',
        'created_by': 'str',
        'updated_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'application_id': 'applicationId',
        'user_id': 'userId',
        'name': 'name',
        'description': 'description',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'attributes': 'attributes',
        'state': 'state',
        'active_ruleset_id': 'activeRulesetId',
        'tags': 'tags',
        'features': 'features',
        'coupon_settings': 'couponSettings',
        'referral_settings': 'referralSettings',
        'limits': 'limits',
        'campaign_groups': 'campaignGroups',
        'coupon_redemption_count': 'couponRedemptionCount',
        'referral_redemption_count': 'referralRedemptionCount',
        'discount_count': 'discountCount',
        'discount_effect_count': 'discountEffectCount',
        'coupon_creation_count': 'couponCreationCount',
        'referral_creation_count': 'referralCreationCount',
        'awarded_giveaways_count': 'awardedGiveawaysCount',
        'created_loyalty_points_count': 'createdLoyaltyPointsCount',
        'created_loyalty_points_effect_count': 'createdLoyaltyPointsEffectCount',
        'redeemed_loyalty_points_count': 'redeemedLoyaltyPointsCount',
        'redeemed_loyalty_points_effect_count': 'redeemedLoyaltyPointsEffectCount',
        'last_activity': 'lastActivity',
        'updated': 'updated',
        'created_by': 'createdBy',
        'updated_by': 'updatedBy'
    }

    def __init__(self, id=None, created=None, application_id=None, user_id=None, name=None, description=None, start_time=None, end_time=None, attributes=None, state='enabled', active_ruleset_id=None, tags=None, features=None, coupon_settings=None, referral_settings=None, limits=None, campaign_groups=None, coupon_redemption_count=None, referral_redemption_count=None, discount_count=None, discount_effect_count=None, coupon_creation_count=None, referral_creation_count=None, awarded_giveaways_count=None, created_loyalty_points_count=None, created_loyalty_points_effect_count=None, redeemed_loyalty_points_count=None, redeemed_loyalty_points_effect_count=None, last_activity=None, updated=None, created_by=None, updated_by=None, local_vars_configuration=None):  # noqa: E501
        """Campaign - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._application_id = None
        self._user_id = None
        self._name = None
        self._description = None
        self._start_time = None
        self._end_time = None
        self._attributes = None
        self._state = None
        self._active_ruleset_id = None
        self._tags = None
        self._features = None
        self._coupon_settings = None
        self._referral_settings = None
        self._limits = None
        self._campaign_groups = None
        self._coupon_redemption_count = None
        self._referral_redemption_count = None
        self._discount_count = None
        self._discount_effect_count = None
        self._coupon_creation_count = None
        self._referral_creation_count = None
        self._awarded_giveaways_count = None
        self._created_loyalty_points_count = None
        self._created_loyalty_points_effect_count = None
        self._redeemed_loyalty_points_count = None
        self._redeemed_loyalty_points_effect_count = None
        self._last_activity = None
        self._updated = None
        self._created_by = None
        self._updated_by = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.application_id = application_id
        self.user_id = user_id
        self.name = name
        self.description = description
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if attributes is not None:
            self.attributes = attributes
        self.state = state
        if active_ruleset_id is not None:
            self.active_ruleset_id = active_ruleset_id
        self.tags = tags
        self.features = features
        if coupon_settings is not None:
            self.coupon_settings = coupon_settings
        if referral_settings is not None:
            self.referral_settings = referral_settings
        self.limits = limits
        if campaign_groups is not None:
            self.campaign_groups = campaign_groups
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
        if referral_creation_count is not None:
            self.referral_creation_count = referral_creation_count
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
        if last_activity is not None:
            self.last_activity = last_activity
        if updated is not None:
            self.updated = updated
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by

    @property
    def id(self):
        """Gets the id of this Campaign.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Campaign.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this Campaign.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Campaign.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this Campaign.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Campaign.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this Campaign.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def application_id(self):
        """Gets the application_id of this Campaign.  # noqa: E501

        The ID of the application that owns this entity.  # noqa: E501

        :return: The application_id of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this Campaign.

        The ID of the application that owns this entity.  # noqa: E501

        :param application_id: The application_id of this Campaign.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def user_id(self):
        """Gets the user_id of this Campaign.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The user_id of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Campaign.

        The ID of the account that owns this entity.  # noqa: E501

        :param user_id: The user_id of this Campaign.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this Campaign.  # noqa: E501

        A friendly name for this campaign.  # noqa: E501

        :return: The name of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Campaign.

        A friendly name for this campaign.  # noqa: E501

        :param name: The name of this Campaign.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Campaign.  # noqa: E501

        A detailed description of the campaign.  # noqa: E501

        :return: The description of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Campaign.

        A detailed description of the campaign.  # noqa: E501

        :param description: The description of this Campaign.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def start_time(self):
        """Gets the start_time of this Campaign.  # noqa: E501

        Datetime when the campaign will become active.  # noqa: E501

        :return: The start_time of this Campaign.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Campaign.

        Datetime when the campaign will become active.  # noqa: E501

        :param start_time: The start_time of this Campaign.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Campaign.  # noqa: E501

        Datetime when the campaign will become in-active.  # noqa: E501

        :return: The end_time of this Campaign.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Campaign.

        Datetime when the campaign will become in-active.  # noqa: E501

        :param end_time: The end_time of this Campaign.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def attributes(self):
        """Gets the attributes of this Campaign.  # noqa: E501

        Arbitrary properties associated with this campaign  # noqa: E501

        :return: The attributes of this Campaign.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Campaign.

        Arbitrary properties associated with this campaign  # noqa: E501

        :param attributes: The attributes of this Campaign.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def state(self):
        """Gets the state of this Campaign.  # noqa: E501

        A disabled or archived campaign is not evaluated for rules or coupons.   # noqa: E501

        :return: The state of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Campaign.

        A disabled or archived campaign is not evaluated for rules or coupons.   # noqa: E501

        :param state: The state of this Campaign.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["enabled", "disabled", "archived"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def active_ruleset_id(self):
        """Gets the active_ruleset_id of this Campaign.  # noqa: E501

        ID of Ruleset this campaign applies on customer session evaluation.  # noqa: E501

        :return: The active_ruleset_id of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._active_ruleset_id

    @active_ruleset_id.setter
    def active_ruleset_id(self, active_ruleset_id):
        """Sets the active_ruleset_id of this Campaign.

        ID of Ruleset this campaign applies on customer session evaluation.  # noqa: E501

        :param active_ruleset_id: The active_ruleset_id of this Campaign.  # noqa: E501
        :type: int
        """

        self._active_ruleset_id = active_ruleset_id

    @property
    def tags(self):
        """Gets the tags of this Campaign.  # noqa: E501

        A list of tags for the campaign.  # noqa: E501

        :return: The tags of this Campaign.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Campaign.

        A list of tags for the campaign.  # noqa: E501

        :param tags: The tags of this Campaign.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def features(self):
        """Gets the features of this Campaign.  # noqa: E501

        A list of features for the campaign.  # noqa: E501

        :return: The features of this Campaign.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this Campaign.

        A list of features for the campaign.  # noqa: E501

        :param features: The features of this Campaign.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and features is None:  # noqa: E501
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501
        allowed_values = ["coupons", "referrals", "loyalty", "giveaways"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(features).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `features` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(features) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._features = features

    @property
    def coupon_settings(self):
        """Gets the coupon_settings of this Campaign.  # noqa: E501


        :return: The coupon_settings of this Campaign.  # noqa: E501
        :rtype: CodeGeneratorSettings
        """
        return self._coupon_settings

    @coupon_settings.setter
    def coupon_settings(self, coupon_settings):
        """Sets the coupon_settings of this Campaign.


        :param coupon_settings: The coupon_settings of this Campaign.  # noqa: E501
        :type: CodeGeneratorSettings
        """

        self._coupon_settings = coupon_settings

    @property
    def referral_settings(self):
        """Gets the referral_settings of this Campaign.  # noqa: E501


        :return: The referral_settings of this Campaign.  # noqa: E501
        :rtype: CodeGeneratorSettings
        """
        return self._referral_settings

    @referral_settings.setter
    def referral_settings(self, referral_settings):
        """Sets the referral_settings of this Campaign.


        :param referral_settings: The referral_settings of this Campaign.  # noqa: E501
        :type: CodeGeneratorSettings
        """

        self._referral_settings = referral_settings

    @property
    def limits(self):
        """Gets the limits of this Campaign.  # noqa: E501

        The set of limits that will operate for this campaign  # noqa: E501

        :return: The limits of this Campaign.  # noqa: E501
        :rtype: list[LimitConfig]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this Campaign.

        The set of limits that will operate for this campaign  # noqa: E501

        :param limits: The limits of this Campaign.  # noqa: E501
        :type: list[LimitConfig]
        """
        if self.local_vars_configuration.client_side_validation and limits is None:  # noqa: E501
            raise ValueError("Invalid value for `limits`, must not be `None`")  # noqa: E501

        self._limits = limits

    @property
    def campaign_groups(self):
        """Gets the campaign_groups of this Campaign.  # noqa: E501

        The IDs of the campaign groups that own this entity.  # noqa: E501

        :return: The campaign_groups of this Campaign.  # noqa: E501
        :rtype: list[int]
        """
        return self._campaign_groups

    @campaign_groups.setter
    def campaign_groups(self, campaign_groups):
        """Sets the campaign_groups of this Campaign.

        The IDs of the campaign groups that own this entity.  # noqa: E501

        :param campaign_groups: The campaign_groups of this Campaign.  # noqa: E501
        :type: list[int]
        """

        self._campaign_groups = campaign_groups

    @property
    def coupon_redemption_count(self):
        """Gets the coupon_redemption_count of this Campaign.  # noqa: E501

        Number of coupons redeemed in the campaign.  # noqa: E501

        :return: The coupon_redemption_count of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._coupon_redemption_count

    @coupon_redemption_count.setter
    def coupon_redemption_count(self, coupon_redemption_count):
        """Sets the coupon_redemption_count of this Campaign.

        Number of coupons redeemed in the campaign.  # noqa: E501

        :param coupon_redemption_count: The coupon_redemption_count of this Campaign.  # noqa: E501
        :type: int
        """

        self._coupon_redemption_count = coupon_redemption_count

    @property
    def referral_redemption_count(self):
        """Gets the referral_redemption_count of this Campaign.  # noqa: E501

        Number of referral codes redeemed in the campaign.  # noqa: E501

        :return: The referral_redemption_count of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._referral_redemption_count

    @referral_redemption_count.setter
    def referral_redemption_count(self, referral_redemption_count):
        """Sets the referral_redemption_count of this Campaign.

        Number of referral codes redeemed in the campaign.  # noqa: E501

        :param referral_redemption_count: The referral_redemption_count of this Campaign.  # noqa: E501
        :type: int
        """

        self._referral_redemption_count = referral_redemption_count

    @property
    def discount_count(self):
        """Gets the discount_count of this Campaign.  # noqa: E501

        Total amount of discounts redeemed in the campaign.  # noqa: E501

        :return: The discount_count of this Campaign.  # noqa: E501
        :rtype: float
        """
        return self._discount_count

    @discount_count.setter
    def discount_count(self, discount_count):
        """Sets the discount_count of this Campaign.

        Total amount of discounts redeemed in the campaign.  # noqa: E501

        :param discount_count: The discount_count of this Campaign.  # noqa: E501
        :type: float
        """

        self._discount_count = discount_count

    @property
    def discount_effect_count(self):
        """Gets the discount_effect_count of this Campaign.  # noqa: E501

        Total number of times discounts were redeemed in this campaign.  # noqa: E501

        :return: The discount_effect_count of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._discount_effect_count

    @discount_effect_count.setter
    def discount_effect_count(self, discount_effect_count):
        """Sets the discount_effect_count of this Campaign.

        Total number of times discounts were redeemed in this campaign.  # noqa: E501

        :param discount_effect_count: The discount_effect_count of this Campaign.  # noqa: E501
        :type: int
        """

        self._discount_effect_count = discount_effect_count

    @property
    def coupon_creation_count(self):
        """Gets the coupon_creation_count of this Campaign.  # noqa: E501

        Total number of coupons created by rules in this campaign.  # noqa: E501

        :return: The coupon_creation_count of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._coupon_creation_count

    @coupon_creation_count.setter
    def coupon_creation_count(self, coupon_creation_count):
        """Sets the coupon_creation_count of this Campaign.

        Total number of coupons created by rules in this campaign.  # noqa: E501

        :param coupon_creation_count: The coupon_creation_count of this Campaign.  # noqa: E501
        :type: int
        """

        self._coupon_creation_count = coupon_creation_count

    @property
    def referral_creation_count(self):
        """Gets the referral_creation_count of this Campaign.  # noqa: E501

        Total number of referrals created by rules in this campaign.  # noqa: E501

        :return: The referral_creation_count of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._referral_creation_count

    @referral_creation_count.setter
    def referral_creation_count(self, referral_creation_count):
        """Sets the referral_creation_count of this Campaign.

        Total number of referrals created by rules in this campaign.  # noqa: E501

        :param referral_creation_count: The referral_creation_count of this Campaign.  # noqa: E501
        :type: int
        """

        self._referral_creation_count = referral_creation_count

    @property
    def awarded_giveaways_count(self):
        """Gets the awarded_giveaways_count of this Campaign.  # noqa: E501

        Total number of giveaways awarded by rules in this campaign.  # noqa: E501

        :return: The awarded_giveaways_count of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._awarded_giveaways_count

    @awarded_giveaways_count.setter
    def awarded_giveaways_count(self, awarded_giveaways_count):
        """Sets the awarded_giveaways_count of this Campaign.

        Total number of giveaways awarded by rules in this campaign.  # noqa: E501

        :param awarded_giveaways_count: The awarded_giveaways_count of this Campaign.  # noqa: E501
        :type: int
        """

        self._awarded_giveaways_count = awarded_giveaways_count

    @property
    def created_loyalty_points_count(self):
        """Gets the created_loyalty_points_count of this Campaign.  # noqa: E501

        Total number of loyalty points created by rules in this campaign.  # noqa: E501

        :return: The created_loyalty_points_count of this Campaign.  # noqa: E501
        :rtype: float
        """
        return self._created_loyalty_points_count

    @created_loyalty_points_count.setter
    def created_loyalty_points_count(self, created_loyalty_points_count):
        """Sets the created_loyalty_points_count of this Campaign.

        Total number of loyalty points created by rules in this campaign.  # noqa: E501

        :param created_loyalty_points_count: The created_loyalty_points_count of this Campaign.  # noqa: E501
        :type: float
        """

        self._created_loyalty_points_count = created_loyalty_points_count

    @property
    def created_loyalty_points_effect_count(self):
        """Gets the created_loyalty_points_effect_count of this Campaign.  # noqa: E501

        Total number of loyalty point creation effects triggered by rules in this campaign.  # noqa: E501

        :return: The created_loyalty_points_effect_count of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._created_loyalty_points_effect_count

    @created_loyalty_points_effect_count.setter
    def created_loyalty_points_effect_count(self, created_loyalty_points_effect_count):
        """Sets the created_loyalty_points_effect_count of this Campaign.

        Total number of loyalty point creation effects triggered by rules in this campaign.  # noqa: E501

        :param created_loyalty_points_effect_count: The created_loyalty_points_effect_count of this Campaign.  # noqa: E501
        :type: int
        """

        self._created_loyalty_points_effect_count = created_loyalty_points_effect_count

    @property
    def redeemed_loyalty_points_count(self):
        """Gets the redeemed_loyalty_points_count of this Campaign.  # noqa: E501

        Total number of loyalty points redeemed by rules in this campaign.  # noqa: E501

        :return: The redeemed_loyalty_points_count of this Campaign.  # noqa: E501
        :rtype: float
        """
        return self._redeemed_loyalty_points_count

    @redeemed_loyalty_points_count.setter
    def redeemed_loyalty_points_count(self, redeemed_loyalty_points_count):
        """Sets the redeemed_loyalty_points_count of this Campaign.

        Total number of loyalty points redeemed by rules in this campaign.  # noqa: E501

        :param redeemed_loyalty_points_count: The redeemed_loyalty_points_count of this Campaign.  # noqa: E501
        :type: float
        """

        self._redeemed_loyalty_points_count = redeemed_loyalty_points_count

    @property
    def redeemed_loyalty_points_effect_count(self):
        """Gets the redeemed_loyalty_points_effect_count of this Campaign.  # noqa: E501

        Total number of loyalty point redemption effects triggered by rules in this campaign.  # noqa: E501

        :return: The redeemed_loyalty_points_effect_count of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._redeemed_loyalty_points_effect_count

    @redeemed_loyalty_points_effect_count.setter
    def redeemed_loyalty_points_effect_count(self, redeemed_loyalty_points_effect_count):
        """Sets the redeemed_loyalty_points_effect_count of this Campaign.

        Total number of loyalty point redemption effects triggered by rules in this campaign.  # noqa: E501

        :param redeemed_loyalty_points_effect_count: The redeemed_loyalty_points_effect_count of this Campaign.  # noqa: E501
        :type: int
        """

        self._redeemed_loyalty_points_effect_count = redeemed_loyalty_points_effect_count

    @property
    def last_activity(self):
        """Gets the last_activity of this Campaign.  # noqa: E501

        Timestamp of the most recent event received by this campaign.  # noqa: E501

        :return: The last_activity of this Campaign.  # noqa: E501
        :rtype: datetime
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """Sets the last_activity of this Campaign.

        Timestamp of the most recent event received by this campaign.  # noqa: E501

        :param last_activity: The last_activity of this Campaign.  # noqa: E501
        :type: datetime
        """

        self._last_activity = last_activity

    @property
    def updated(self):
        """Gets the updated of this Campaign.  # noqa: E501

        Timestamp of the most recent update to the campaign or any of its elements.  # noqa: E501

        :return: The updated of this Campaign.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Campaign.

        Timestamp of the most recent update to the campaign or any of its elements.  # noqa: E501

        :param updated: The updated of this Campaign.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created_by(self):
        """Gets the created_by of this Campaign.  # noqa: E501

        Name of the user who created this campaign if available.  # noqa: E501

        :return: The created_by of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Campaign.

        Name of the user who created this campaign if available.  # noqa: E501

        :param created_by: The created_by of this Campaign.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this Campaign.  # noqa: E501

        Name of the user who last updated this campaign if available.  # noqa: E501

        :return: The updated_by of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Campaign.

        Name of the user who last updated this campaign if available.  # noqa: E501

        :param updated_by: The updated_by of this Campaign.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

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
        if not isinstance(other, Campaign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Campaign):
            return True

        return self.to_dict() != other.to_dict()
