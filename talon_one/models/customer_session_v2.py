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


class CustomerSessionV2(object):
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
        'integration_id': 'str',
        'application_id': 'int',
        'profile_id': 'str',
        'evaluable_campaign_ids': 'list[int]',
        'coupon_codes': 'list[str]',
        'referral_code': 'str',
        'loyalty_cards': 'list[str]',
        'state': 'str',
        'cart_items': 'list[CartItem]',
        'additional_costs': 'dict(str, AdditionalCost)',
        'identifiers': 'list[str]',
        'attributes': 'object',
        'first_session': 'bool',
        'total': 'float',
        'cart_item_total': 'float',
        'additional_cost_total': 'float',
        'updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'integration_id': 'integrationId',
        'application_id': 'applicationId',
        'profile_id': 'profileId',
        'evaluable_campaign_ids': 'evaluableCampaignIds',
        'coupon_codes': 'couponCodes',
        'referral_code': 'referralCode',
        'loyalty_cards': 'loyaltyCards',
        'state': 'state',
        'cart_items': 'cartItems',
        'additional_costs': 'additionalCosts',
        'identifiers': 'identifiers',
        'attributes': 'attributes',
        'first_session': 'firstSession',
        'total': 'total',
        'cart_item_total': 'cartItemTotal',
        'additional_cost_total': 'additionalCostTotal',
        'updated': 'updated'
    }

    def __init__(self, id=None, created=None, integration_id=None, application_id=None, profile_id=None, evaluable_campaign_ids=None, coupon_codes=None, referral_code=None, loyalty_cards=None, state='open', cart_items=None, additional_costs=None, identifiers=None, attributes=None, first_session=None, total=None, cart_item_total=None, additional_cost_total=None, updated=None, local_vars_configuration=None):  # noqa: E501
        """CustomerSessionV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._integration_id = None
        self._application_id = None
        self._profile_id = None
        self._evaluable_campaign_ids = None
        self._coupon_codes = None
        self._referral_code = None
        self._loyalty_cards = None
        self._state = None
        self._cart_items = None
        self._additional_costs = None
        self._identifiers = None
        self._attributes = None
        self._first_session = None
        self._total = None
        self._cart_item_total = None
        self._additional_cost_total = None
        self._updated = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.integration_id = integration_id
        self.application_id = application_id
        self.profile_id = profile_id
        if evaluable_campaign_ids is not None:
            self.evaluable_campaign_ids = evaluable_campaign_ids
        if coupon_codes is not None:
            self.coupon_codes = coupon_codes
        if referral_code is not None:
            self.referral_code = referral_code
        if loyalty_cards is not None:
            self.loyalty_cards = loyalty_cards
        self.state = state
        self.cart_items = cart_items
        if additional_costs is not None:
            self.additional_costs = additional_costs
        if identifiers is not None:
            self.identifiers = identifiers
        self.attributes = attributes
        self.first_session = first_session
        self.total = total
        self.cart_item_total = cart_item_total
        self.additional_cost_total = additional_cost_total
        self.updated = updated

    @property
    def id(self):
        """Gets the id of this CustomerSessionV2.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this CustomerSessionV2.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerSessionV2.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this CustomerSessionV2.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this CustomerSessionV2.  # noqa: E501

        The time this entity was created. The time this entity was created.  # noqa: E501

        :return: The created of this CustomerSessionV2.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CustomerSessionV2.

        The time this entity was created. The time this entity was created.  # noqa: E501

        :param created: The created of this CustomerSessionV2.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def integration_id(self):
        """Gets the integration_id of this CustomerSessionV2.  # noqa: E501

        The integration ID set by your integration layer.  # noqa: E501

        :return: The integration_id of this CustomerSessionV2.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this CustomerSessionV2.

        The integration ID set by your integration layer.  # noqa: E501

        :param integration_id: The integration_id of this CustomerSessionV2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                integration_id is not None and len(integration_id) > 1000):
            raise ValueError("Invalid value for `integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._integration_id = integration_id

    @property
    def application_id(self):
        """Gets the application_id of this CustomerSessionV2.  # noqa: E501

        The ID of the application that owns this entity.  # noqa: E501

        :return: The application_id of this CustomerSessionV2.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this CustomerSessionV2.

        The ID of the application that owns this entity.  # noqa: E501

        :param application_id: The application_id of this CustomerSessionV2.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def profile_id(self):
        """Gets the profile_id of this CustomerSessionV2.  # noqa: E501

        ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known `profileId`, we recommend you use a guest `profileId`.   # noqa: E501

        :return: The profile_id of this CustomerSessionV2.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this CustomerSessionV2.

        ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known `profileId`, we recommend you use a guest `profileId`.   # noqa: E501

        :param profile_id: The profile_id of this CustomerSessionV2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and profile_id is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

    @property
    def evaluable_campaign_ids(self):
        """Gets the evaluable_campaign_ids of this CustomerSessionV2.  # noqa: E501

        When using the `dry` query parameter, use this property to list the campaign to be evaluated by the Rule Engine.  These campaigns will be evaluated, even if they are disabled, allowing you to test specific campaigns before activating them.   # noqa: E501

        :return: The evaluable_campaign_ids of this CustomerSessionV2.  # noqa: E501
        :rtype: list[int]
        """
        return self._evaluable_campaign_ids

    @evaluable_campaign_ids.setter
    def evaluable_campaign_ids(self, evaluable_campaign_ids):
        """Sets the evaluable_campaign_ids of this CustomerSessionV2.

        When using the `dry` query parameter, use this property to list the campaign to be evaluated by the Rule Engine.  These campaigns will be evaluated, even if they are disabled, allowing you to test specific campaigns before activating them.   # noqa: E501

        :param evaluable_campaign_ids: The evaluable_campaign_ids of this CustomerSessionV2.  # noqa: E501
        :type: list[int]
        """

        self._evaluable_campaign_ids = evaluable_campaign_ids

    @property
    def coupon_codes(self):
        """Gets the coupon_codes of this CustomerSessionV2.  # noqa: E501

        Any coupon codes entered.  **Important**: If you [create a coupon budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign, ensure the session contains a coupon code by the time you close it.   # noqa: E501

        :return: The coupon_codes of this CustomerSessionV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._coupon_codes

    @coupon_codes.setter
    def coupon_codes(self, coupon_codes):
        """Sets the coupon_codes of this CustomerSessionV2.

        Any coupon codes entered.  **Important**: If you [create a coupon budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign, ensure the session contains a coupon code by the time you close it.   # noqa: E501

        :param coupon_codes: The coupon_codes of this CustomerSessionV2.  # noqa: E501
        :type: list[str]
        """

        self._coupon_codes = coupon_codes

    @property
    def referral_code(self):
        """Gets the referral_code of this CustomerSessionV2.  # noqa: E501

        Any referral code entered.  **Important**: If you [create a referral budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign, ensure the session contains a referral code by the time you close it.   # noqa: E501

        :return: The referral_code of this CustomerSessionV2.  # noqa: E501
        :rtype: str
        """
        return self._referral_code

    @referral_code.setter
    def referral_code(self, referral_code):
        """Sets the referral_code of this CustomerSessionV2.

        Any referral code entered.  **Important**: If you [create a referral budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign, ensure the session contains a referral code by the time you close it.   # noqa: E501

        :param referral_code: The referral_code of this CustomerSessionV2.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                referral_code is not None and len(referral_code) > 100):
            raise ValueError("Invalid value for `referral_code`, length must be less than or equal to `100`")  # noqa: E501

        self._referral_code = referral_code

    @property
    def loyalty_cards(self):
        """Gets the loyalty_cards of this CustomerSessionV2.  # noqa: E501

        Any loyalty cards used.  # noqa: E501

        :return: The loyalty_cards of this CustomerSessionV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._loyalty_cards

    @loyalty_cards.setter
    def loyalty_cards(self, loyalty_cards):
        """Sets the loyalty_cards of this CustomerSessionV2.

        Any loyalty cards used.  # noqa: E501

        :param loyalty_cards: The loyalty_cards of this CustomerSessionV2.  # noqa: E501
        :type: list[str]
        """

        self._loyalty_cards = loyalty_cards

    @property
    def state(self):
        """Gets the state of this CustomerSessionV2.  # noqa: E501

        Indicates the current state of the session. Sessions can be created as `open` or `closed`. The state transitions are:  1. `open` → `closed` 2. `open` → `cancelled` 3. Either:    - `closed` → `cancelled` (**only** via [Update customer session](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/updateCustomerSessionV2)) or    - `closed` → `partially_returned` (**only** via [Return cart items](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/returnCartItems))    - `closed` → `open` (**only** via [Reopen customer session](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/reopenCustomerSession)) 4. `partially_returned` → `cancelled`  For more information, see [Customer session states](https://docs.talon.one/docs/dev/concepts/entities#customer-session).   # noqa: E501

        :return: The state of this CustomerSessionV2.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CustomerSessionV2.

        Indicates the current state of the session. Sessions can be created as `open` or `closed`. The state transitions are:  1. `open` → `closed` 2. `open` → `cancelled` 3. Either:    - `closed` → `cancelled` (**only** via [Update customer session](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/updateCustomerSessionV2)) or    - `closed` → `partially_returned` (**only** via [Return cart items](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/returnCartItems))    - `closed` → `open` (**only** via [Reopen customer session](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/reopenCustomerSession)) 4. `partially_returned` → `cancelled`  For more information, see [Customer session states](https://docs.talon.one/docs/dev/concepts/entities#customer-session).   # noqa: E501

        :param state: The state of this CustomerSessionV2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["open", "closed", "partially_returned", "cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def cart_items(self):
        """Gets the cart_items of this CustomerSessionV2.  # noqa: E501

        The items to add to this sessions. - If cart item flattening is disabled: **Do not exceed 1000 items** (regardless of their `quantity`) per request. - If cart item flattening is enabled: **Do not exceed 1000 items** and ensure the sum of all cart item's `quantity` **does not exceed 10.000** per request.   # noqa: E501

        :return: The cart_items of this CustomerSessionV2.  # noqa: E501
        :rtype: list[CartItem]
        """
        return self._cart_items

    @cart_items.setter
    def cart_items(self, cart_items):
        """Sets the cart_items of this CustomerSessionV2.

        The items to add to this sessions. - If cart item flattening is disabled: **Do not exceed 1000 items** (regardless of their `quantity`) per request. - If cart item flattening is enabled: **Do not exceed 1000 items** and ensure the sum of all cart item's `quantity` **does not exceed 10.000** per request.   # noqa: E501

        :param cart_items: The cart_items of this CustomerSessionV2.  # noqa: E501
        :type: list[CartItem]
        """
        if self.local_vars_configuration.client_side_validation and cart_items is None:  # noqa: E501
            raise ValueError("Invalid value for `cart_items`, must not be `None`")  # noqa: E501

        self._cart_items = cart_items

    @property
    def additional_costs(self):
        """Gets the additional_costs of this CustomerSessionV2.  # noqa: E501

        Use this property to set a value for the additional costs of this session, such as a shipping cost.  They must be created in the Campaign Manager before you set them with this property. See [Managing additional costs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).   # noqa: E501

        :return: The additional_costs of this CustomerSessionV2.  # noqa: E501
        :rtype: dict(str, AdditionalCost)
        """
        return self._additional_costs

    @additional_costs.setter
    def additional_costs(self, additional_costs):
        """Sets the additional_costs of this CustomerSessionV2.

        Use this property to set a value for the additional costs of this session, such as a shipping cost.  They must be created in the Campaign Manager before you set them with this property. See [Managing additional costs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).   # noqa: E501

        :param additional_costs: The additional_costs of this CustomerSessionV2.  # noqa: E501
        :type: dict(str, AdditionalCost)
        """

        self._additional_costs = additional_costs

    @property
    def identifiers(self):
        """Gets the identifiers of this CustomerSessionV2.  # noqa: E501

        Session custom identifiers that you can set limits on or use inside your rules.  For example, you can use IP addresses as identifiers to potentially identify devices and limit discounts abuse in case of customers creating multiple accounts. See the [tutorial](https://docs.talon.one/docs/dev/tutorials/using-identifiers).  **Important**: Ensure the session contains an identifier by the time you close it if: - You [create a unique identifier budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign. - Your campaign has [coupons](https://docs.talon.one/docs/product/campaigns/coupons/coupon-page-overview).   # noqa: E501

        :return: The identifiers of this CustomerSessionV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this CustomerSessionV2.

        Session custom identifiers that you can set limits on or use inside your rules.  For example, you can use IP addresses as identifiers to potentially identify devices and limit discounts abuse in case of customers creating multiple accounts. See the [tutorial](https://docs.talon.one/docs/dev/tutorials/using-identifiers).  **Important**: Ensure the session contains an identifier by the time you close it if: - You [create a unique identifier budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign. - Your campaign has [coupons](https://docs.talon.one/docs/product/campaigns/coupons/coupon-page-overview).   # noqa: E501

        :param identifiers: The identifiers of this CustomerSessionV2.  # noqa: E501
        :type: list[str]
        """

        self._identifiers = identifiers

    @property
    def attributes(self):
        """Gets the attributes of this CustomerSessionV2.  # noqa: E501

        Use this property to set a value for the attributes of your choice. Attributes represent any information to attach to your session, like the shipping city.  You can use [built-in attributes](https://docs.talon.one/docs/dev/concepts/attributes#built-in-attributes) or [custom ones](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes). Custom attributes must be created in the Campaign Manager before you set them with this property.   # noqa: E501

        :return: The attributes of this CustomerSessionV2.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CustomerSessionV2.

        Use this property to set a value for the attributes of your choice. Attributes represent any information to attach to your session, like the shipping city.  You can use [built-in attributes](https://docs.talon.one/docs/dev/concepts/attributes#built-in-attributes) or [custom ones](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes). Custom attributes must be created in the Campaign Manager before you set them with this property.   # noqa: E501

        :param attributes: The attributes of this CustomerSessionV2.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def first_session(self):
        """Gets the first_session of this CustomerSessionV2.  # noqa: E501

        Indicates whether this is the first session for the customer's profile. Will always be true for anonymous sessions.  # noqa: E501

        :return: The first_session of this CustomerSessionV2.  # noqa: E501
        :rtype: bool
        """
        return self._first_session

    @first_session.setter
    def first_session(self, first_session):
        """Sets the first_session of this CustomerSessionV2.

        Indicates whether this is the first session for the customer's profile. Will always be true for anonymous sessions.  # noqa: E501

        :param first_session: The first_session of this CustomerSessionV2.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and first_session is None:  # noqa: E501
            raise ValueError("Invalid value for `first_session`, must not be `None`")  # noqa: E501

        self._first_session = first_session

    @property
    def total(self):
        """Gets the total of this CustomerSessionV2.  # noqa: E501

        The total sum of cart-items, as well as additional costs, before any discounts applied.  # noqa: E501

        :return: The total of this CustomerSessionV2.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CustomerSessionV2.

        The total sum of cart-items, as well as additional costs, before any discounts applied.  # noqa: E501

        :param total: The total of this CustomerSessionV2.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def cart_item_total(self):
        """Gets the cart_item_total of this CustomerSessionV2.  # noqa: E501

        The total sum of cart-items before any discounts applied.  # noqa: E501

        :return: The cart_item_total of this CustomerSessionV2.  # noqa: E501
        :rtype: float
        """
        return self._cart_item_total

    @cart_item_total.setter
    def cart_item_total(self, cart_item_total):
        """Sets the cart_item_total of this CustomerSessionV2.

        The total sum of cart-items before any discounts applied.  # noqa: E501

        :param cart_item_total: The cart_item_total of this CustomerSessionV2.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and cart_item_total is None:  # noqa: E501
            raise ValueError("Invalid value for `cart_item_total`, must not be `None`")  # noqa: E501

        self._cart_item_total = cart_item_total

    @property
    def additional_cost_total(self):
        """Gets the additional_cost_total of this CustomerSessionV2.  # noqa: E501

        The total sum of additional costs before any discounts applied.  # noqa: E501

        :return: The additional_cost_total of this CustomerSessionV2.  # noqa: E501
        :rtype: float
        """
        return self._additional_cost_total

    @additional_cost_total.setter
    def additional_cost_total(self, additional_cost_total):
        """Sets the additional_cost_total of this CustomerSessionV2.

        The total sum of additional costs before any discounts applied.  # noqa: E501

        :param additional_cost_total: The additional_cost_total of this CustomerSessionV2.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and additional_cost_total is None:  # noqa: E501
            raise ValueError("Invalid value for `additional_cost_total`, must not be `None`")  # noqa: E501

        self._additional_cost_total = additional_cost_total

    @property
    def updated(self):
        """Gets the updated of this CustomerSessionV2.  # noqa: E501

        Timestamp of the most recent event received on this session.  # noqa: E501

        :return: The updated of this CustomerSessionV2.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this CustomerSessionV2.

        Timestamp of the most recent event received on this session.  # noqa: E501

        :param updated: The updated of this CustomerSessionV2.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated is None:  # noqa: E501
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

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
        if not isinstance(other, CustomerSessionV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerSessionV2):
            return True

        return self.to_dict() != other.to_dict()
