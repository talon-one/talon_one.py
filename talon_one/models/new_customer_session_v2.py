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


class NewCustomerSessionV2(object):
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
        'profile_id': 'str',
        'store_integration_id': 'str',
        'evaluable_campaign_ids': 'list[int]',
        'coupon_codes': 'list[str]',
        'referral_code': 'str',
        'loyalty_cards': 'list[str]',
        'state': 'str',
        'cart_items': 'list[CartItem]',
        'additional_costs': 'dict(str, AdditionalCost)',
        'identifiers': 'list[str]',
        'attributes': 'object'
    }

    attribute_map = {
        'profile_id': 'profileId',
        'store_integration_id': 'storeIntegrationId',
        'evaluable_campaign_ids': 'evaluableCampaignIds',
        'coupon_codes': 'couponCodes',
        'referral_code': 'referralCode',
        'loyalty_cards': 'loyaltyCards',
        'state': 'state',
        'cart_items': 'cartItems',
        'additional_costs': 'additionalCosts',
        'identifiers': 'identifiers',
        'attributes': 'attributes'
    }

    def __init__(self, profile_id=None, store_integration_id=None, evaluable_campaign_ids=None, coupon_codes=None, referral_code=None, loyalty_cards=None, state='open', cart_items=None, additional_costs=None, identifiers=None, attributes=None, local_vars_configuration=None):  # noqa: E501
        """NewCustomerSessionV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._profile_id = None
        self._store_integration_id = None
        self._evaluable_campaign_ids = None
        self._coupon_codes = None
        self._referral_code = None
        self._loyalty_cards = None
        self._state = None
        self._cart_items = None
        self._additional_costs = None
        self._identifiers = None
        self._attributes = None
        self.discriminator = None

        if profile_id is not None:
            self.profile_id = profile_id
        if store_integration_id is not None:
            self.store_integration_id = store_integration_id
        if evaluable_campaign_ids is not None:
            self.evaluable_campaign_ids = evaluable_campaign_ids
        if coupon_codes is not None:
            self.coupon_codes = coupon_codes
        if referral_code is not None:
            self.referral_code = referral_code
        if loyalty_cards is not None:
            self.loyalty_cards = loyalty_cards
        if state is not None:
            self.state = state
        if cart_items is not None:
            self.cart_items = cart_items
        if additional_costs is not None:
            self.additional_costs = additional_costs
        if identifiers is not None:
            self.identifiers = identifiers
        if attributes is not None:
            self.attributes = attributes

    @property
    def profile_id(self):
        """Gets the profile_id of this NewCustomerSessionV2.  # noqa: E501

        ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known `profileId`, we recommend you use a guest `profileId`.   # noqa: E501

        :return: The profile_id of this NewCustomerSessionV2.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this NewCustomerSessionV2.

        ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known `profileId`, we recommend you use a guest `profileId`.   # noqa: E501

        :param profile_id: The profile_id of this NewCustomerSessionV2.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def store_integration_id(self):
        """Gets the store_integration_id of this NewCustomerSessionV2.  # noqa: E501

        The integration ID of the store. You choose this ID when you create a store.  # noqa: E501

        :return: The store_integration_id of this NewCustomerSessionV2.  # noqa: E501
        :rtype: str
        """
        return self._store_integration_id

    @store_integration_id.setter
    def store_integration_id(self, store_integration_id):
        """Sets the store_integration_id of this NewCustomerSessionV2.

        The integration ID of the store. You choose this ID when you create a store.  # noqa: E501

        :param store_integration_id: The store_integration_id of this NewCustomerSessionV2.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                store_integration_id is not None and len(store_integration_id) > 1000):
            raise ValueError("Invalid value for `store_integration_id`, length must be less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                store_integration_id is not None and len(store_integration_id) < 1):
            raise ValueError("Invalid value for `store_integration_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._store_integration_id = store_integration_id

    @property
    def evaluable_campaign_ids(self):
        """Gets the evaluable_campaign_ids of this NewCustomerSessionV2.  # noqa: E501

        When using the `dry` query parameter, use this property to list the campaign to be evaluated by the Rule Engine.  These campaigns will be evaluated, even if they are disabled, allowing you to test specific campaigns before activating them.   # noqa: E501

        :return: The evaluable_campaign_ids of this NewCustomerSessionV2.  # noqa: E501
        :rtype: list[int]
        """
        return self._evaluable_campaign_ids

    @evaluable_campaign_ids.setter
    def evaluable_campaign_ids(self, evaluable_campaign_ids):
        """Sets the evaluable_campaign_ids of this NewCustomerSessionV2.

        When using the `dry` query parameter, use this property to list the campaign to be evaluated by the Rule Engine.  These campaigns will be evaluated, even if they are disabled, allowing you to test specific campaigns before activating them.   # noqa: E501

        :param evaluable_campaign_ids: The evaluable_campaign_ids of this NewCustomerSessionV2.  # noqa: E501
        :type: list[int]
        """

        self._evaluable_campaign_ids = evaluable_campaign_ids

    @property
    def coupon_codes(self):
        """Gets the coupon_codes of this NewCustomerSessionV2.  # noqa: E501

        Any coupon codes entered.  **Important - for requests only**:  - If you [create a coupon budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign, ensure the session contains a coupon code by the time you close it. - In requests where `dry=false`, providing an empty array discards any previous coupons. To avoid this, omit the parameter entirely.   # noqa: E501

        :return: The coupon_codes of this NewCustomerSessionV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._coupon_codes

    @coupon_codes.setter
    def coupon_codes(self, coupon_codes):
        """Sets the coupon_codes of this NewCustomerSessionV2.

        Any coupon codes entered.  **Important - for requests only**:  - If you [create a coupon budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign, ensure the session contains a coupon code by the time you close it. - In requests where `dry=false`, providing an empty array discards any previous coupons. To avoid this, omit the parameter entirely.   # noqa: E501

        :param coupon_codes: The coupon_codes of this NewCustomerSessionV2.  # noqa: E501
        :type: list[str]
        """

        self._coupon_codes = coupon_codes

    @property
    def referral_code(self):
        """Gets the referral_code of this NewCustomerSessionV2.  # noqa: E501

        Any referral code entered.  **Important - for requests only**:  - If you [create a referral budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign, ensure the session contains a referral code by the time you close it. - In requests where `dry=false`, providing an empty value discards the previous referral code. To avoid this, omit the parameter entirely.   # noqa: E501

        :return: The referral_code of this NewCustomerSessionV2.  # noqa: E501
        :rtype: str
        """
        return self._referral_code

    @referral_code.setter
    def referral_code(self, referral_code):
        """Sets the referral_code of this NewCustomerSessionV2.

        Any referral code entered.  **Important - for requests only**:  - If you [create a referral budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign, ensure the session contains a referral code by the time you close it. - In requests where `dry=false`, providing an empty value discards the previous referral code. To avoid this, omit the parameter entirely.   # noqa: E501

        :param referral_code: The referral_code of this NewCustomerSessionV2.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                referral_code is not None and len(referral_code) > 100):
            raise ValueError("Invalid value for `referral_code`, length must be less than or equal to `100`")  # noqa: E501

        self._referral_code = referral_code

    @property
    def loyalty_cards(self):
        """Gets the loyalty_cards of this NewCustomerSessionV2.  # noqa: E501

        Identifier of a loyalty card.  # noqa: E501

        :return: The loyalty_cards of this NewCustomerSessionV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._loyalty_cards

    @loyalty_cards.setter
    def loyalty_cards(self, loyalty_cards):
        """Sets the loyalty_cards of this NewCustomerSessionV2.

        Identifier of a loyalty card.  # noqa: E501

        :param loyalty_cards: The loyalty_cards of this NewCustomerSessionV2.  # noqa: E501
        :type: list[str]
        """

        self._loyalty_cards = loyalty_cards

    @property
    def state(self):
        """Gets the state of this NewCustomerSessionV2.  # noqa: E501

        Indicates the current state of the session. Sessions can be created as `open` or `closed`. The state transitions are:  1. `open` → `closed` 2. `open` → `cancelled` 3. Either:    - `closed` → `cancelled` (**only** via [Update customer session](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/updateCustomerSessionV2)) or    - `closed` → `partially_returned` (**only** via [Return cart items](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/returnCartItems))    - `closed` → `open` (**only** via [Reopen customer session](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/reopenCustomerSession)) 4. `partially_returned` → `cancelled`  For more information, see [Customer session states](https://docs.talon.one/docs/dev/concepts/entities/customer-sessions).   # noqa: E501

        :return: The state of this NewCustomerSessionV2.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NewCustomerSessionV2.

        Indicates the current state of the session. Sessions can be created as `open` or `closed`. The state transitions are:  1. `open` → `closed` 2. `open` → `cancelled` 3. Either:    - `closed` → `cancelled` (**only** via [Update customer session](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/updateCustomerSessionV2)) or    - `closed` → `partially_returned` (**only** via [Return cart items](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/returnCartItems))    - `closed` → `open` (**only** via [Reopen customer session](https://docs.talon.one/integration-api#tag/Customer-sessions/operation/reopenCustomerSession)) 4. `partially_returned` → `cancelled`  For more information, see [Customer session states](https://docs.talon.one/docs/dev/concepts/entities/customer-sessions).   # noqa: E501

        :param state: The state of this NewCustomerSessionV2.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "closed", "partially_returned", "cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def cart_items(self):
        """Gets the cart_items of this NewCustomerSessionV2.  # noqa: E501

        The items to add to this session. **Do not exceed 1000 items** and ensure the sum of all cart item's `quantity` **does not exceed 10.000** per request.   # noqa: E501

        :return: The cart_items of this NewCustomerSessionV2.  # noqa: E501
        :rtype: list[CartItem]
        """
        return self._cart_items

    @cart_items.setter
    def cart_items(self, cart_items):
        """Sets the cart_items of this NewCustomerSessionV2.

        The items to add to this session. **Do not exceed 1000 items** and ensure the sum of all cart item's `quantity` **does not exceed 10.000** per request.   # noqa: E501

        :param cart_items: The cart_items of this NewCustomerSessionV2.  # noqa: E501
        :type: list[CartItem]
        """

        self._cart_items = cart_items

    @property
    def additional_costs(self):
        """Gets the additional_costs of this NewCustomerSessionV2.  # noqa: E501

        Use this property to set a value for the additional costs of this session, such as a shipping cost.  They must be created in the Campaign Manager before you set them with this property. See [Managing additional costs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).   # noqa: E501

        :return: The additional_costs of this NewCustomerSessionV2.  # noqa: E501
        :rtype: dict(str, AdditionalCost)
        """
        return self._additional_costs

    @additional_costs.setter
    def additional_costs(self, additional_costs):
        """Sets the additional_costs of this NewCustomerSessionV2.

        Use this property to set a value for the additional costs of this session, such as a shipping cost.  They must be created in the Campaign Manager before you set them with this property. See [Managing additional costs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).   # noqa: E501

        :param additional_costs: The additional_costs of this NewCustomerSessionV2.  # noqa: E501
        :type: dict(str, AdditionalCost)
        """

        self._additional_costs = additional_costs

    @property
    def identifiers(self):
        """Gets the identifiers of this NewCustomerSessionV2.  # noqa: E501

        Session custom identifiers that you can set limits on or use inside your rules.  For example, you can use IP addresses as identifiers to potentially identify devices and limit discounts abuse in case of customers creating multiple accounts. See the [tutorial](https://docs.talon.one/docs/dev/tutorials/using-identifiers).  **Important**: Ensure the session contains an identifier by the time you close it if: - You [create a unique identifier budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign. - Your campaign has [coupons](https://docs.talon.one/docs/product/campaigns/coupons/coupon-page-overview). - We recommend passing an anonymized (hashed) version of the identifier value.   # noqa: E501

        :return: The identifiers of this NewCustomerSessionV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this NewCustomerSessionV2.

        Session custom identifiers that you can set limits on or use inside your rules.  For example, you can use IP addresses as identifiers to potentially identify devices and limit discounts abuse in case of customers creating multiple accounts. See the [tutorial](https://docs.talon.one/docs/dev/tutorials/using-identifiers).  **Important**: Ensure the session contains an identifier by the time you close it if: - You [create a unique identifier budget](https://docs.talon.one/docs/product/campaigns/settings/managing-campaign-budgets/#budget-types) for your campaign. - Your campaign has [coupons](https://docs.talon.one/docs/product/campaigns/coupons/coupon-page-overview). - We recommend passing an anonymized (hashed) version of the identifier value.   # noqa: E501

        :param identifiers: The identifiers of this NewCustomerSessionV2.  # noqa: E501
        :type: list[str]
        """

        self._identifiers = identifiers

    @property
    def attributes(self):
        """Gets the attributes of this NewCustomerSessionV2.  # noqa: E501

        Use this property to set a value for the attributes of your choice. Attributes represent any information to attach to your session, like the shipping city.  You can use [built-in attributes](https://docs.talon.one/docs/dev/concepts/attributes#built-in-attributes) or [custom ones](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes). Custom attributes must be created in the Campaign Manager before you set them with this property.   # noqa: E501

        :return: The attributes of this NewCustomerSessionV2.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NewCustomerSessionV2.

        Use this property to set a value for the attributes of your choice. Attributes represent any information to attach to your session, like the shipping city.  You can use [built-in attributes](https://docs.talon.one/docs/dev/concepts/attributes#built-in-attributes) or [custom ones](https://docs.talon.one/docs/dev/concepts/attributes#custom-attributes). Custom attributes must be created in the Campaign Manager before you set them with this property.   # noqa: E501

        :param attributes: The attributes of this NewCustomerSessionV2.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

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
        if not isinstance(other, NewCustomerSessionV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewCustomerSessionV2):
            return True

        return self.to_dict() != other.to_dict()
