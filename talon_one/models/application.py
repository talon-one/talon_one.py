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


class Application(object):
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
        'modified': 'datetime',
        'account_id': 'int',
        'name': 'str',
        'description': 'str',
        'timezone': 'str',
        'currency': 'str',
        'case_sensitivity': 'str',
        'attributes': 'object',
        'limits': 'list[LimitConfig]',
        'default_discount_scope': 'str',
        'enable_cascading_discounts': 'bool',
        'enable_flattened_cart_items': 'bool',
        'attributes_settings': 'AttributesSettings',
        'sandbox': 'bool',
        'enable_partial_discounts': 'bool',
        'default_discount_additional_cost_per_item_scope': 'str',
        'default_evaluation_group_id': 'int',
        'default_cart_item_filter_id': 'int',
        'enable_campaign_state_management': 'bool',
        'loyalty_programs': 'list[LoyaltyProgram]'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'account_id': 'accountId',
        'name': 'name',
        'description': 'description',
        'timezone': 'timezone',
        'currency': 'currency',
        'case_sensitivity': 'caseSensitivity',
        'attributes': 'attributes',
        'limits': 'limits',
        'default_discount_scope': 'defaultDiscountScope',
        'enable_cascading_discounts': 'enableCascadingDiscounts',
        'enable_flattened_cart_items': 'enableFlattenedCartItems',
        'attributes_settings': 'attributesSettings',
        'sandbox': 'sandbox',
        'enable_partial_discounts': 'enablePartialDiscounts',
        'default_discount_additional_cost_per_item_scope': 'defaultDiscountAdditionalCostPerItemScope',
        'default_evaluation_group_id': 'defaultEvaluationGroupId',
        'default_cart_item_filter_id': 'defaultCartItemFilterId',
        'enable_campaign_state_management': 'enableCampaignStateManagement',
        'loyalty_programs': 'loyaltyPrograms'
    }

    def __init__(self, id=None, created=None, modified=None, account_id=None, name=None, description=None, timezone=None, currency=None, case_sensitivity=None, attributes=None, limits=None, default_discount_scope=None, enable_cascading_discounts=None, enable_flattened_cart_items=None, attributes_settings=None, sandbox=None, enable_partial_discounts=None, default_discount_additional_cost_per_item_scope=None, default_evaluation_group_id=None, default_cart_item_filter_id=None, enable_campaign_state_management=None, loyalty_programs=None, local_vars_configuration=None):  # noqa: E501
        """Application - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._modified = None
        self._account_id = None
        self._name = None
        self._description = None
        self._timezone = None
        self._currency = None
        self._case_sensitivity = None
        self._attributes = None
        self._limits = None
        self._default_discount_scope = None
        self._enable_cascading_discounts = None
        self._enable_flattened_cart_items = None
        self._attributes_settings = None
        self._sandbox = None
        self._enable_partial_discounts = None
        self._default_discount_additional_cost_per_item_scope = None
        self._default_evaluation_group_id = None
        self._default_cart_item_filter_id = None
        self._enable_campaign_state_management = None
        self._loyalty_programs = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.modified = modified
        self.account_id = account_id
        self.name = name
        if description is not None:
            self.description = description
        self.timezone = timezone
        self.currency = currency
        if case_sensitivity is not None:
            self.case_sensitivity = case_sensitivity
        if attributes is not None:
            self.attributes = attributes
        if limits is not None:
            self.limits = limits
        if default_discount_scope is not None:
            self.default_discount_scope = default_discount_scope
        if enable_cascading_discounts is not None:
            self.enable_cascading_discounts = enable_cascading_discounts
        if enable_flattened_cart_items is not None:
            self.enable_flattened_cart_items = enable_flattened_cart_items
        if attributes_settings is not None:
            self.attributes_settings = attributes_settings
        if sandbox is not None:
            self.sandbox = sandbox
        if enable_partial_discounts is not None:
            self.enable_partial_discounts = enable_partial_discounts
        if default_discount_additional_cost_per_item_scope is not None:
            self.default_discount_additional_cost_per_item_scope = default_discount_additional_cost_per_item_scope
        if default_evaluation_group_id is not None:
            self.default_evaluation_group_id = default_evaluation_group_id
        if default_cart_item_filter_id is not None:
            self.default_cart_item_filter_id = default_cart_item_filter_id
        if enable_campaign_state_management is not None:
            self.enable_campaign_state_management = enable_campaign_state_management
        self.loyalty_programs = loyalty_programs

    @property
    def id(self):
        """Gets the id of this Application.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this Application.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this Application.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Application.  # noqa: E501

        The time this entity was created.  # noqa: E501

        :return: The created of this Application.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Application.

        The time this entity was created.  # noqa: E501

        :param created: The created of this Application.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Application.  # noqa: E501

        The time this entity was last modified.  # noqa: E501

        :return: The modified of this Application.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Application.

        The time this entity was last modified.  # noqa: E501

        :param modified: The modified of this Application.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified is None:  # noqa: E501
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def account_id(self):
        """Gets the account_id of this Application.  # noqa: E501

        The ID of the account that owns this entity.  # noqa: E501

        :return: The account_id of this Application.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Application.

        The ID of the account that owns this entity.  # noqa: E501

        :param account_id: The account_id of this Application.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this Application.  # noqa: E501

        The name of this application.  # noqa: E501

        :return: The name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.

        The name of this application.  # noqa: E501

        :param name: The name of this Application.  # noqa: E501
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
        """Gets the description of this Application.  # noqa: E501

        A longer description of the application.  # noqa: E501

        :return: The description of this Application.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Application.

        A longer description of the application.  # noqa: E501

        :param description: The description of this Application.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def timezone(self):
        """Gets the timezone of this Application.  # noqa: E501

        A string containing an IANA timezone descriptor.  # noqa: E501

        :return: The timezone of this Application.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Application.

        A string containing an IANA timezone descriptor.  # noqa: E501

        :param timezone: The timezone of this Application.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and timezone is None:  # noqa: E501
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                timezone is not None and len(timezone) < 1):
            raise ValueError("Invalid value for `timezone`, length must be greater than or equal to `1`")  # noqa: E501

        self._timezone = timezone

    @property
    def currency(self):
        """Gets the currency of this Application.  # noqa: E501

        The default currency for new customer sessions.  # noqa: E501

        :return: The currency of this Application.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Application.

        The default currency for new customer sessions.  # noqa: E501

        :param currency: The currency of this Application.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and len(currency) < 1):
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `1`")  # noqa: E501

        self._currency = currency

    @property
    def case_sensitivity(self):
        """Gets the case_sensitivity of this Application.  # noqa: E501

        The case sensitivity behavior to check coupon codes in the campaigns of this Application.  # noqa: E501

        :return: The case_sensitivity of this Application.  # noqa: E501
        :rtype: str
        """
        return self._case_sensitivity

    @case_sensitivity.setter
    def case_sensitivity(self, case_sensitivity):
        """Sets the case_sensitivity of this Application.

        The case sensitivity behavior to check coupon codes in the campaigns of this Application.  # noqa: E501

        :param case_sensitivity: The case_sensitivity of this Application.  # noqa: E501
        :type: str
        """
        allowed_values = ["sensitive", "insensitive-uppercase", "insensitive-lowercase"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and case_sensitivity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `case_sensitivity` ({0}), must be one of {1}"  # noqa: E501
                .format(case_sensitivity, allowed_values)
            )

        self._case_sensitivity = case_sensitivity

    @property
    def attributes(self):
        """Gets the attributes of this Application.  # noqa: E501

        Arbitrary properties associated with this campaign.  # noqa: E501

        :return: The attributes of this Application.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Application.

        Arbitrary properties associated with this campaign.  # noqa: E501

        :param attributes: The attributes of this Application.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def limits(self):
        """Gets the limits of this Application.  # noqa: E501

        Default limits for campaigns created in this application.  # noqa: E501

        :return: The limits of this Application.  # noqa: E501
        :rtype: list[LimitConfig]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this Application.

        Default limits for campaigns created in this application.  # noqa: E501

        :param limits: The limits of this Application.  # noqa: E501
        :type: list[LimitConfig]
        """

        self._limits = limits

    @property
    def default_discount_scope(self):
        """Gets the default_discount_scope of this Application.  # noqa: E501

        The default scope to apply `setDiscount` effects on if no scope was provided with the effect.   # noqa: E501

        :return: The default_discount_scope of this Application.  # noqa: E501
        :rtype: str
        """
        return self._default_discount_scope

    @default_discount_scope.setter
    def default_discount_scope(self, default_discount_scope):
        """Sets the default_discount_scope of this Application.

        The default scope to apply `setDiscount` effects on if no scope was provided with the effect.   # noqa: E501

        :param default_discount_scope: The default_discount_scope of this Application.  # noqa: E501
        :type: str
        """
        allowed_values = ["sessionTotal", "cartItems", "additionalCosts"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and default_discount_scope not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `default_discount_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(default_discount_scope, allowed_values)
            )

        self._default_discount_scope = default_discount_scope

    @property
    def enable_cascading_discounts(self):
        """Gets the enable_cascading_discounts of this Application.  # noqa: E501

        Indicates if discounts should cascade for this Application.  # noqa: E501

        :return: The enable_cascading_discounts of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cascading_discounts

    @enable_cascading_discounts.setter
    def enable_cascading_discounts(self, enable_cascading_discounts):
        """Sets the enable_cascading_discounts of this Application.

        Indicates if discounts should cascade for this Application.  # noqa: E501

        :param enable_cascading_discounts: The enable_cascading_discounts of this Application.  # noqa: E501
        :type: bool
        """

        self._enable_cascading_discounts = enable_cascading_discounts

    @property
    def enable_flattened_cart_items(self):
        """Gets the enable_flattened_cart_items of this Application.  # noqa: E501

        Indicates if cart items of quantity larger than one should be separated into different items of quantity one.   # noqa: E501

        :return: The enable_flattened_cart_items of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._enable_flattened_cart_items

    @enable_flattened_cart_items.setter
    def enable_flattened_cart_items(self, enable_flattened_cart_items):
        """Sets the enable_flattened_cart_items of this Application.

        Indicates if cart items of quantity larger than one should be separated into different items of quantity one.   # noqa: E501

        :param enable_flattened_cart_items: The enable_flattened_cart_items of this Application.  # noqa: E501
        :type: bool
        """

        self._enable_flattened_cart_items = enable_flattened_cart_items

    @property
    def attributes_settings(self):
        """Gets the attributes_settings of this Application.  # noqa: E501


        :return: The attributes_settings of this Application.  # noqa: E501
        :rtype: AttributesSettings
        """
        return self._attributes_settings

    @attributes_settings.setter
    def attributes_settings(self, attributes_settings):
        """Sets the attributes_settings of this Application.


        :param attributes_settings: The attributes_settings of this Application.  # noqa: E501
        :type: AttributesSettings
        """

        self._attributes_settings = attributes_settings

    @property
    def sandbox(self):
        """Gets the sandbox of this Application.  # noqa: E501

        Indicates if this is a live or sandbox Application.  # noqa: E501

        :return: The sandbox of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._sandbox

    @sandbox.setter
    def sandbox(self, sandbox):
        """Sets the sandbox of this Application.

        Indicates if this is a live or sandbox Application.  # noqa: E501

        :param sandbox: The sandbox of this Application.  # noqa: E501
        :type: bool
        """

        self._sandbox = sandbox

    @property
    def enable_partial_discounts(self):
        """Gets the enable_partial_discounts of this Application.  # noqa: E501

        Indicates if this Application supports partial discounts.  # noqa: E501

        :return: The enable_partial_discounts of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._enable_partial_discounts

    @enable_partial_discounts.setter
    def enable_partial_discounts(self, enable_partial_discounts):
        """Sets the enable_partial_discounts of this Application.

        Indicates if this Application supports partial discounts.  # noqa: E501

        :param enable_partial_discounts: The enable_partial_discounts of this Application.  # noqa: E501
        :type: bool
        """

        self._enable_partial_discounts = enable_partial_discounts

    @property
    def default_discount_additional_cost_per_item_scope(self):
        """Gets the default_discount_additional_cost_per_item_scope of this Application.  # noqa: E501

        The default scope to apply `setDiscountPerItem` effects on if no scope was provided with the effect.   # noqa: E501

        :return: The default_discount_additional_cost_per_item_scope of this Application.  # noqa: E501
        :rtype: str
        """
        return self._default_discount_additional_cost_per_item_scope

    @default_discount_additional_cost_per_item_scope.setter
    def default_discount_additional_cost_per_item_scope(self, default_discount_additional_cost_per_item_scope):
        """Sets the default_discount_additional_cost_per_item_scope of this Application.

        The default scope to apply `setDiscountPerItem` effects on if no scope was provided with the effect.   # noqa: E501

        :param default_discount_additional_cost_per_item_scope: The default_discount_additional_cost_per_item_scope of this Application.  # noqa: E501
        :type: str
        """
        allowed_values = ["price", "itemTotal", "additionalCosts"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and default_discount_additional_cost_per_item_scope not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `default_discount_additional_cost_per_item_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(default_discount_additional_cost_per_item_scope, allowed_values)
            )

        self._default_discount_additional_cost_per_item_scope = default_discount_additional_cost_per_item_scope

    @property
    def default_evaluation_group_id(self):
        """Gets the default_evaluation_group_id of this Application.  # noqa: E501

        The ID of the default campaign evaluation group to which new campaigns will be added unless a different group is selected when creating the campaign.  # noqa: E501

        :return: The default_evaluation_group_id of this Application.  # noqa: E501
        :rtype: int
        """
        return self._default_evaluation_group_id

    @default_evaluation_group_id.setter
    def default_evaluation_group_id(self, default_evaluation_group_id):
        """Sets the default_evaluation_group_id of this Application.

        The ID of the default campaign evaluation group to which new campaigns will be added unless a different group is selected when creating the campaign.  # noqa: E501

        :param default_evaluation_group_id: The default_evaluation_group_id of this Application.  # noqa: E501
        :type: int
        """

        self._default_evaluation_group_id = default_evaluation_group_id

    @property
    def default_cart_item_filter_id(self):
        """Gets the default_cart_item_filter_id of this Application.  # noqa: E501

        The ID of the default Cart-Item-Filter for this application.  # noqa: E501

        :return: The default_cart_item_filter_id of this Application.  # noqa: E501
        :rtype: int
        """
        return self._default_cart_item_filter_id

    @default_cart_item_filter_id.setter
    def default_cart_item_filter_id(self, default_cart_item_filter_id):
        """Sets the default_cart_item_filter_id of this Application.

        The ID of the default Cart-Item-Filter for this application.  # noqa: E501

        :param default_cart_item_filter_id: The default_cart_item_filter_id of this Application.  # noqa: E501
        :type: int
        """

        self._default_cart_item_filter_id = default_cart_item_filter_id

    @property
    def enable_campaign_state_management(self):
        """Gets the enable_campaign_state_management of this Application.  # noqa: E501

        Indicates whether the campaign staging and revisions feature is enabled for the Application.  **Important:** After this feature is enabled, it cannot be disabled.   # noqa: E501

        :return: The enable_campaign_state_management of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._enable_campaign_state_management

    @enable_campaign_state_management.setter
    def enable_campaign_state_management(self, enable_campaign_state_management):
        """Sets the enable_campaign_state_management of this Application.

        Indicates whether the campaign staging and revisions feature is enabled for the Application.  **Important:** After this feature is enabled, it cannot be disabled.   # noqa: E501

        :param enable_campaign_state_management: The enable_campaign_state_management of this Application.  # noqa: E501
        :type: bool
        """

        self._enable_campaign_state_management = enable_campaign_state_management

    @property
    def loyalty_programs(self):
        """Gets the loyalty_programs of this Application.  # noqa: E501

        An array containing all the loyalty programs to which this application is subscribed.  # noqa: E501

        :return: The loyalty_programs of this Application.  # noqa: E501
        :rtype: list[LoyaltyProgram]
        """
        return self._loyalty_programs

    @loyalty_programs.setter
    def loyalty_programs(self, loyalty_programs):
        """Sets the loyalty_programs of this Application.

        An array containing all the loyalty programs to which this application is subscribed.  # noqa: E501

        :param loyalty_programs: The loyalty_programs of this Application.  # noqa: E501
        :type: list[LoyaltyProgram]
        """
        if self.local_vars_configuration.client_side_validation and loyalty_programs is None:  # noqa: E501
            raise ValueError("Invalid value for `loyalty_programs`, must not be `None`")  # noqa: E501

        self._loyalty_programs = loyalty_programs

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
        if not isinstance(other, Application):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Application):
            return True

        return self.to_dict() != other.to_dict()
