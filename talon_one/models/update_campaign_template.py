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


class UpdateCampaignTemplate(object):
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
        'name': 'str',
        'description': 'str',
        'instructions': 'str',
        'campaign_attributes': 'object',
        'coupon_attributes': 'object',
        'state': 'str',
        'active_ruleset_id': 'int',
        'tags': 'list[str]',
        'features': 'list[str]',
        'coupon_settings': 'CodeGeneratorSettings',
        'coupon_reservation_settings': 'CampaignTemplateCouponReservationSettings',
        'referral_settings': 'CodeGeneratorSettings',
        'limits': 'list[TemplateLimitConfig]',
        'template_params': 'list[CampaignTemplateParams]',
        'applications_ids': 'list[int]',
        'campaign_collections': 'list[CampaignTemplateCollection]',
        'default_campaign_group_id': 'int',
        'campaign_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'instructions': 'instructions',
        'campaign_attributes': 'campaignAttributes',
        'coupon_attributes': 'couponAttributes',
        'state': 'state',
        'active_ruleset_id': 'activeRulesetId',
        'tags': 'tags',
        'features': 'features',
        'coupon_settings': 'couponSettings',
        'coupon_reservation_settings': 'couponReservationSettings',
        'referral_settings': 'referralSettings',
        'limits': 'limits',
        'template_params': 'templateParams',
        'applications_ids': 'applicationsIds',
        'campaign_collections': 'campaignCollections',
        'default_campaign_group_id': 'defaultCampaignGroupId',
        'campaign_type': 'campaignType'
    }

    def __init__(self, name=None, description=None, instructions=None, campaign_attributes=None, coupon_attributes=None, state=None, active_ruleset_id=None, tags=None, features=None, coupon_settings=None, coupon_reservation_settings=None, referral_settings=None, limits=None, template_params=None, applications_ids=None, campaign_collections=None, default_campaign_group_id=None, campaign_type='advanced', local_vars_configuration=None):  # noqa: E501
        """UpdateCampaignTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._instructions = None
        self._campaign_attributes = None
        self._coupon_attributes = None
        self._state = None
        self._active_ruleset_id = None
        self._tags = None
        self._features = None
        self._coupon_settings = None
        self._coupon_reservation_settings = None
        self._referral_settings = None
        self._limits = None
        self._template_params = None
        self._applications_ids = None
        self._campaign_collections = None
        self._default_campaign_group_id = None
        self._campaign_type = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.instructions = instructions
        if campaign_attributes is not None:
            self.campaign_attributes = campaign_attributes
        if coupon_attributes is not None:
            self.coupon_attributes = coupon_attributes
        self.state = state
        if active_ruleset_id is not None:
            self.active_ruleset_id = active_ruleset_id
        if tags is not None:
            self.tags = tags
        if features is not None:
            self.features = features
        if coupon_settings is not None:
            self.coupon_settings = coupon_settings
        if coupon_reservation_settings is not None:
            self.coupon_reservation_settings = coupon_reservation_settings
        if referral_settings is not None:
            self.referral_settings = referral_settings
        if limits is not None:
            self.limits = limits
        if template_params is not None:
            self.template_params = template_params
        self.applications_ids = applications_ids
        if campaign_collections is not None:
            self.campaign_collections = campaign_collections
        if default_campaign_group_id is not None:
            self.default_campaign_group_id = default_campaign_group_id
        if campaign_type is not None:
            self.campaign_type = campaign_type

    @property
    def name(self):
        """Gets the name of this UpdateCampaignTemplate.  # noqa: E501

        The campaign template name.  # noqa: E501

        :return: The name of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCampaignTemplate.

        The campaign template name.  # noqa: E501

        :param name: The name of this UpdateCampaignTemplate.  # noqa: E501
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
        """Gets the description of this UpdateCampaignTemplate.  # noqa: E501

        Customer-facing text that explains the objective of the template.  # noqa: E501

        :return: The description of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCampaignTemplate.

        Customer-facing text that explains the objective of the template.  # noqa: E501

        :param description: The description of this UpdateCampaignTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def instructions(self):
        """Gets the instructions of this UpdateCampaignTemplate.  # noqa: E501

        Customer-facing text that explains how to use the template. For example, you can use this property to explain the available attributes of this template, and how they can be modified when a user uses this template to create a new campaign.  # noqa: E501

        :return: The instructions of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this UpdateCampaignTemplate.

        Customer-facing text that explains how to use the template. For example, you can use this property to explain the available attributes of this template, and how they can be modified when a user uses this template to create a new campaign.  # noqa: E501

        :param instructions: The instructions of this UpdateCampaignTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instructions is None:  # noqa: E501
            raise ValueError("Invalid value for `instructions`, must not be `None`")  # noqa: E501

        self._instructions = instructions

    @property
    def campaign_attributes(self):
        """Gets the campaign_attributes of this UpdateCampaignTemplate.  # noqa: E501

        The campaign attributes that campaigns created from this template will have by default.  # noqa: E501

        :return: The campaign_attributes of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: object
        """
        return self._campaign_attributes

    @campaign_attributes.setter
    def campaign_attributes(self, campaign_attributes):
        """Sets the campaign_attributes of this UpdateCampaignTemplate.

        The campaign attributes that campaigns created from this template will have by default.  # noqa: E501

        :param campaign_attributes: The campaign_attributes of this UpdateCampaignTemplate.  # noqa: E501
        :type: object
        """

        self._campaign_attributes = campaign_attributes

    @property
    def coupon_attributes(self):
        """Gets the coupon_attributes of this UpdateCampaignTemplate.  # noqa: E501

        The campaign attributes that coupons created from this template will have by default.  # noqa: E501

        :return: The coupon_attributes of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: object
        """
        return self._coupon_attributes

    @coupon_attributes.setter
    def coupon_attributes(self, coupon_attributes):
        """Sets the coupon_attributes of this UpdateCampaignTemplate.

        The campaign attributes that coupons created from this template will have by default.  # noqa: E501

        :param coupon_attributes: The coupon_attributes of this UpdateCampaignTemplate.  # noqa: E501
        :type: object
        """

        self._coupon_attributes = coupon_attributes

    @property
    def state(self):
        """Gets the state of this UpdateCampaignTemplate.  # noqa: E501

        Only campaign templates in 'available' state may be used to create campaigns.  # noqa: E501

        :return: The state of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateCampaignTemplate.

        Only campaign templates in 'available' state may be used to create campaigns.  # noqa: E501

        :param state: The state of this UpdateCampaignTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["draft", "enabled", "disabled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def active_ruleset_id(self):
        """Gets the active_ruleset_id of this UpdateCampaignTemplate.  # noqa: E501

        The ID of the ruleset this campaign template will use.  # noqa: E501

        :return: The active_ruleset_id of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: int
        """
        return self._active_ruleset_id

    @active_ruleset_id.setter
    def active_ruleset_id(self, active_ruleset_id):
        """Sets the active_ruleset_id of this UpdateCampaignTemplate.

        The ID of the ruleset this campaign template will use.  # noqa: E501

        :param active_ruleset_id: The active_ruleset_id of this UpdateCampaignTemplate.  # noqa: E501
        :type: int
        """

        self._active_ruleset_id = active_ruleset_id

    @property
    def tags(self):
        """Gets the tags of this UpdateCampaignTemplate.  # noqa: E501

        A list of tags for the campaign template.  # noqa: E501

        :return: The tags of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateCampaignTemplate.

        A list of tags for the campaign template.  # noqa: E501

        :param tags: The tags of this UpdateCampaignTemplate.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def features(self):
        """Gets the features of this UpdateCampaignTemplate.  # noqa: E501

        A list of features for the campaign template.  # noqa: E501

        :return: The features of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this UpdateCampaignTemplate.

        A list of features for the campaign template.  # noqa: E501

        :param features: The features of this UpdateCampaignTemplate.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["coupons", "referrals", "loyalty", "giveaways", "strikethrough", "achievements"]  # noqa: E501
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
        """Gets the coupon_settings of this UpdateCampaignTemplate.  # noqa: E501


        :return: The coupon_settings of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: CodeGeneratorSettings
        """
        return self._coupon_settings

    @coupon_settings.setter
    def coupon_settings(self, coupon_settings):
        """Sets the coupon_settings of this UpdateCampaignTemplate.


        :param coupon_settings: The coupon_settings of this UpdateCampaignTemplate.  # noqa: E501
        :type: CodeGeneratorSettings
        """

        self._coupon_settings = coupon_settings

    @property
    def coupon_reservation_settings(self):
        """Gets the coupon_reservation_settings of this UpdateCampaignTemplate.  # noqa: E501


        :return: The coupon_reservation_settings of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: CampaignTemplateCouponReservationSettings
        """
        return self._coupon_reservation_settings

    @coupon_reservation_settings.setter
    def coupon_reservation_settings(self, coupon_reservation_settings):
        """Sets the coupon_reservation_settings of this UpdateCampaignTemplate.


        :param coupon_reservation_settings: The coupon_reservation_settings of this UpdateCampaignTemplate.  # noqa: E501
        :type: CampaignTemplateCouponReservationSettings
        """

        self._coupon_reservation_settings = coupon_reservation_settings

    @property
    def referral_settings(self):
        """Gets the referral_settings of this UpdateCampaignTemplate.  # noqa: E501


        :return: The referral_settings of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: CodeGeneratorSettings
        """
        return self._referral_settings

    @referral_settings.setter
    def referral_settings(self, referral_settings):
        """Sets the referral_settings of this UpdateCampaignTemplate.


        :param referral_settings: The referral_settings of this UpdateCampaignTemplate.  # noqa: E501
        :type: CodeGeneratorSettings
        """

        self._referral_settings = referral_settings

    @property
    def limits(self):
        """Gets the limits of this UpdateCampaignTemplate.  # noqa: E501

        The set of limits that operate for this campaign template.  # noqa: E501

        :return: The limits of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: list[TemplateLimitConfig]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this UpdateCampaignTemplate.

        The set of limits that operate for this campaign template.  # noqa: E501

        :param limits: The limits of this UpdateCampaignTemplate.  # noqa: E501
        :type: list[TemplateLimitConfig]
        """

        self._limits = limits

    @property
    def template_params(self):
        """Gets the template_params of this UpdateCampaignTemplate.  # noqa: E501

        Fields which can be used to replace values in a rule.  # noqa: E501

        :return: The template_params of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: list[CampaignTemplateParams]
        """
        return self._template_params

    @template_params.setter
    def template_params(self, template_params):
        """Sets the template_params of this UpdateCampaignTemplate.

        Fields which can be used to replace values in a rule.  # noqa: E501

        :param template_params: The template_params of this UpdateCampaignTemplate.  # noqa: E501
        :type: list[CampaignTemplateParams]
        """

        self._template_params = template_params

    @property
    def applications_ids(self):
        """Gets the applications_ids of this UpdateCampaignTemplate.  # noqa: E501

        A list of IDs of the Applications that are subscribed to this campaign template.  # noqa: E501

        :return: The applications_ids of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: list[int]
        """
        return self._applications_ids

    @applications_ids.setter
    def applications_ids(self, applications_ids):
        """Sets the applications_ids of this UpdateCampaignTemplate.

        A list of IDs of the Applications that are subscribed to this campaign template.  # noqa: E501

        :param applications_ids: The applications_ids of this UpdateCampaignTemplate.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and applications_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `applications_ids`, must not be `None`")  # noqa: E501

        self._applications_ids = applications_ids

    @property
    def campaign_collections(self):
        """Gets the campaign_collections of this UpdateCampaignTemplate.  # noqa: E501

        The campaign collections from the blueprint campaign for the template.  # noqa: E501

        :return: The campaign_collections of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: list[CampaignTemplateCollection]
        """
        return self._campaign_collections

    @campaign_collections.setter
    def campaign_collections(self, campaign_collections):
        """Sets the campaign_collections of this UpdateCampaignTemplate.

        The campaign collections from the blueprint campaign for the template.  # noqa: E501

        :param campaign_collections: The campaign_collections of this UpdateCampaignTemplate.  # noqa: E501
        :type: list[CampaignTemplateCollection]
        """

        self._campaign_collections = campaign_collections

    @property
    def default_campaign_group_id(self):
        """Gets the default_campaign_group_id of this UpdateCampaignTemplate.  # noqa: E501

        The default campaign group ID.  # noqa: E501

        :return: The default_campaign_group_id of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: int
        """
        return self._default_campaign_group_id

    @default_campaign_group_id.setter
    def default_campaign_group_id(self, default_campaign_group_id):
        """Sets the default_campaign_group_id of this UpdateCampaignTemplate.

        The default campaign group ID.  # noqa: E501

        :param default_campaign_group_id: The default_campaign_group_id of this UpdateCampaignTemplate.  # noqa: E501
        :type: int
        """

        self._default_campaign_group_id = default_campaign_group_id

    @property
    def campaign_type(self):
        """Gets the campaign_type of this UpdateCampaignTemplate.  # noqa: E501

        The campaign type. Possible type values:   - `cartItem`: Type of campaign that can apply effects only to cart items.   - `advanced`: Type of campaign that can apply effects to customer sessions and cart items.   # noqa: E501

        :return: The campaign_type of this UpdateCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._campaign_type

    @campaign_type.setter
    def campaign_type(self, campaign_type):
        """Sets the campaign_type of this UpdateCampaignTemplate.

        The campaign type. Possible type values:   - `cartItem`: Type of campaign that can apply effects only to cart items.   - `advanced`: Type of campaign that can apply effects to customer sessions and cart items.   # noqa: E501

        :param campaign_type: The campaign_type of this UpdateCampaignTemplate.  # noqa: E501
        :type: str
        """
        allowed_values = ["cartItem", "advanced"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and campaign_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `campaign_type` ({0}), must be one of {1}"  # noqa: E501
                .format(campaign_type, allowed_values)
            )

        self._campaign_type = campaign_type

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
        if not isinstance(other, UpdateCampaignTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateCampaignTemplate):
            return True

        return self.to_dict() != other.to_dict()
