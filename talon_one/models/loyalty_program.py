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


class LoyaltyProgram(object):
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
        'title': 'str',
        'description': 'str',
        'subscribed_applications': 'list[int]',
        'default_validity': 'str',
        'default_pending': 'str',
        'allow_subledger': 'bool',
        'users_per_card_limit': 'int',
        'sandbox': 'bool',
        'program_join_policy': 'str',
        'tiers_expiration_policy': 'str',
        'tiers_start_date': 'datetime',
        'tiers_expire_in': 'str',
        'tiers_downgrade_policy': 'str',
        'card_code_settings': 'CodeGeneratorSettings',
        'account_id': 'int',
        'name': 'str',
        'tiers': 'list[LoyaltyTier]',
        'timezone': 'str',
        'card_based': 'bool',
        'can_update_tiers': 'bool',
        'can_update_join_policy': 'bool',
        'can_update_tier_expiration_policy': 'bool',
        'can_upgrade_to_advanced_tiers': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'title': 'title',
        'description': 'description',
        'subscribed_applications': 'subscribedApplications',
        'default_validity': 'defaultValidity',
        'default_pending': 'defaultPending',
        'allow_subledger': 'allowSubledger',
        'users_per_card_limit': 'usersPerCardLimit',
        'sandbox': 'sandbox',
        'program_join_policy': 'programJoinPolicy',
        'tiers_expiration_policy': 'tiersExpirationPolicy',
        'tiers_start_date': 'tiersStartDate',
        'tiers_expire_in': 'tiersExpireIn',
        'tiers_downgrade_policy': 'tiersDowngradePolicy',
        'card_code_settings': 'cardCodeSettings',
        'account_id': 'accountID',
        'name': 'name',
        'tiers': 'tiers',
        'timezone': 'timezone',
        'card_based': 'cardBased',
        'can_update_tiers': 'canUpdateTiers',
        'can_update_join_policy': 'canUpdateJoinPolicy',
        'can_update_tier_expiration_policy': 'canUpdateTierExpirationPolicy',
        'can_upgrade_to_advanced_tiers': 'canUpgradeToAdvancedTiers'
    }

    def __init__(self, id=None, created=None, title=None, description=None, subscribed_applications=None, default_validity=None, default_pending=None, allow_subledger=None, users_per_card_limit=None, sandbox=None, program_join_policy=None, tiers_expiration_policy=None, tiers_start_date=None, tiers_expire_in=None, tiers_downgrade_policy=None, card_code_settings=None, account_id=None, name=None, tiers=None, timezone=None, card_based=False, can_update_tiers=False, can_update_join_policy=None, can_update_tier_expiration_policy=None, can_upgrade_to_advanced_tiers=False, local_vars_configuration=None):  # noqa: E501
        """LoyaltyProgram - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._title = None
        self._description = None
        self._subscribed_applications = None
        self._default_validity = None
        self._default_pending = None
        self._allow_subledger = None
        self._users_per_card_limit = None
        self._sandbox = None
        self._program_join_policy = None
        self._tiers_expiration_policy = None
        self._tiers_start_date = None
        self._tiers_expire_in = None
        self._tiers_downgrade_policy = None
        self._card_code_settings = None
        self._account_id = None
        self._name = None
        self._tiers = None
        self._timezone = None
        self._card_based = None
        self._can_update_tiers = None
        self._can_update_join_policy = None
        self._can_update_tier_expiration_policy = None
        self._can_upgrade_to_advanced_tiers = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.title = title
        self.description = description
        self.subscribed_applications = subscribed_applications
        self.default_validity = default_validity
        self.default_pending = default_pending
        self.allow_subledger = allow_subledger
        if users_per_card_limit is not None:
            self.users_per_card_limit = users_per_card_limit
        self.sandbox = sandbox
        if program_join_policy is not None:
            self.program_join_policy = program_join_policy
        if tiers_expiration_policy is not None:
            self.tiers_expiration_policy = tiers_expiration_policy
        if tiers_start_date is not None:
            self.tiers_start_date = tiers_start_date
        if tiers_expire_in is not None:
            self.tiers_expire_in = tiers_expire_in
        if tiers_downgrade_policy is not None:
            self.tiers_downgrade_policy = tiers_downgrade_policy
        if card_code_settings is not None:
            self.card_code_settings = card_code_settings
        self.account_id = account_id
        self.name = name
        if tiers is not None:
            self.tiers = tiers
        self.timezone = timezone
        self.card_based = card_based
        if can_update_tiers is not None:
            self.can_update_tiers = can_update_tiers
        if can_update_join_policy is not None:
            self.can_update_join_policy = can_update_join_policy
        if can_update_tier_expiration_policy is not None:
            self.can_update_tier_expiration_policy = can_update_tier_expiration_policy
        if can_upgrade_to_advanced_tiers is not None:
            self.can_upgrade_to_advanced_tiers = can_upgrade_to_advanced_tiers

    @property
    def id(self):
        """Gets the id of this LoyaltyProgram.  # noqa: E501

        The ID of loyalty program. Internal ID of this entity.  # noqa: E501

        :return: The id of this LoyaltyProgram.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoyaltyProgram.

        The ID of loyalty program. Internal ID of this entity.  # noqa: E501

        :param id: The id of this LoyaltyProgram.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this LoyaltyProgram.  # noqa: E501

        The time this entity was created.  # noqa: E501

        :return: The created of this LoyaltyProgram.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this LoyaltyProgram.

        The time this entity was created.  # noqa: E501

        :param created: The created of this LoyaltyProgram.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def title(self):
        """Gets the title of this LoyaltyProgram.  # noqa: E501

        The display title for the Loyalty Program.  # noqa: E501

        :return: The title of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LoyaltyProgram.

        The display title for the Loyalty Program.  # noqa: E501

        :param title: The title of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this LoyaltyProgram.  # noqa: E501

        Description of our Loyalty Program.  # noqa: E501

        :return: The description of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoyaltyProgram.

        Description of our Loyalty Program.  # noqa: E501

        :param description: The description of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def subscribed_applications(self):
        """Gets the subscribed_applications of this LoyaltyProgram.  # noqa: E501

        A list containing the IDs of all applications that are subscribed to this Loyalty Program.  # noqa: E501

        :return: The subscribed_applications of this LoyaltyProgram.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscribed_applications

    @subscribed_applications.setter
    def subscribed_applications(self, subscribed_applications):
        """Sets the subscribed_applications of this LoyaltyProgram.

        A list containing the IDs of all applications that are subscribed to this Loyalty Program.  # noqa: E501

        :param subscribed_applications: The subscribed_applications of this LoyaltyProgram.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and subscribed_applications is None:  # noqa: E501
            raise ValueError("Invalid value for `subscribed_applications`, must not be `None`")  # noqa: E501

        self._subscribed_applications = subscribed_applications

    @property
    def default_validity(self):
        """Gets the default_validity of this LoyaltyProgram.  # noqa: E501

        The default duration after which new loyalty points should expire. Can be 'unlimited' or a specific time. The time format is a number followed by one letter indicating the time unit, like '30s', '40m', '1h', '5D', '7W', or 10M'. These rounding suffixes are also supported: - '_D' for rounding down. Can be used as a suffix after 'D', and signifies the start of the day. - '_U' for rounding up. Can be used as a suffix after 'D', 'W', and 'M', and signifies the end of the day, week, and month.   # noqa: E501

        :return: The default_validity of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._default_validity

    @default_validity.setter
    def default_validity(self, default_validity):
        """Sets the default_validity of this LoyaltyProgram.

        The default duration after which new loyalty points should expire. Can be 'unlimited' or a specific time. The time format is a number followed by one letter indicating the time unit, like '30s', '40m', '1h', '5D', '7W', or 10M'. These rounding suffixes are also supported: - '_D' for rounding down. Can be used as a suffix after 'D', and signifies the start of the day. - '_U' for rounding up. Can be used as a suffix after 'D', 'W', and 'M', and signifies the end of the day, week, and month.   # noqa: E501

        :param default_validity: The default_validity of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_validity is None:  # noqa: E501
            raise ValueError("Invalid value for `default_validity`, must not be `None`")  # noqa: E501

        self._default_validity = default_validity

    @property
    def default_pending(self):
        """Gets the default_pending of this LoyaltyProgram.  # noqa: E501

        The default duration of the pending time after which points should be valid. Can be 'immediate' or a specific time. The time format is a number followed by one letter indicating the time unit, like '30s', '40m', '1h', '5D', '7W', or 10M'. These rounding suffixes are also supported: - '_D' for rounding down. Can be used as a suffix after 'D', and signifies the start of the day. - '_U' for rounding up. Can be used as a suffix after 'D', 'W', and 'M', and signifies the end of the day, week, and month.   # noqa: E501

        :return: The default_pending of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._default_pending

    @default_pending.setter
    def default_pending(self, default_pending):
        """Sets the default_pending of this LoyaltyProgram.

        The default duration of the pending time after which points should be valid. Can be 'immediate' or a specific time. The time format is a number followed by one letter indicating the time unit, like '30s', '40m', '1h', '5D', '7W', or 10M'. These rounding suffixes are also supported: - '_D' for rounding down. Can be used as a suffix after 'D', and signifies the start of the day. - '_U' for rounding up. Can be used as a suffix after 'D', 'W', and 'M', and signifies the end of the day, week, and month.   # noqa: E501

        :param default_pending: The default_pending of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_pending is None:  # noqa: E501
            raise ValueError("Invalid value for `default_pending`, must not be `None`")  # noqa: E501

        self._default_pending = default_pending

    @property
    def allow_subledger(self):
        """Gets the allow_subledger of this LoyaltyProgram.  # noqa: E501

        Indicates if this program supports subledgers inside the program.  # noqa: E501

        :return: The allow_subledger of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._allow_subledger

    @allow_subledger.setter
    def allow_subledger(self, allow_subledger):
        """Sets the allow_subledger of this LoyaltyProgram.

        Indicates if this program supports subledgers inside the program.  # noqa: E501

        :param allow_subledger: The allow_subledger of this LoyaltyProgram.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_subledger is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_subledger`, must not be `None`")  # noqa: E501

        self._allow_subledger = allow_subledger

    @property
    def users_per_card_limit(self):
        """Gets the users_per_card_limit of this LoyaltyProgram.  # noqa: E501

        The max amount of user profiles with whom a card can be shared. This can be set to 0 for no limit. This property is only used when `cardBased` is `true`.   # noqa: E501

        :return: The users_per_card_limit of this LoyaltyProgram.  # noqa: E501
        :rtype: int
        """
        return self._users_per_card_limit

    @users_per_card_limit.setter
    def users_per_card_limit(self, users_per_card_limit):
        """Sets the users_per_card_limit of this LoyaltyProgram.

        The max amount of user profiles with whom a card can be shared. This can be set to 0 for no limit. This property is only used when `cardBased` is `true`.   # noqa: E501

        :param users_per_card_limit: The users_per_card_limit of this LoyaltyProgram.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                users_per_card_limit is not None and users_per_card_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `users_per_card_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._users_per_card_limit = users_per_card_limit

    @property
    def sandbox(self):
        """Gets the sandbox of this LoyaltyProgram.  # noqa: E501

        Indicates if this program is a live or sandbox program. Programs of a given type can only be connected to Applications of the same type.  # noqa: E501

        :return: The sandbox of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._sandbox

    @sandbox.setter
    def sandbox(self, sandbox):
        """Sets the sandbox of this LoyaltyProgram.

        Indicates if this program is a live or sandbox program. Programs of a given type can only be connected to Applications of the same type.  # noqa: E501

        :param sandbox: The sandbox of this LoyaltyProgram.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and sandbox is None:  # noqa: E501
            raise ValueError("Invalid value for `sandbox`, must not be `None`")  # noqa: E501

        self._sandbox = sandbox

    @property
    def program_join_policy(self):
        """Gets the program_join_policy of this LoyaltyProgram.  # noqa: E501

        The policy that defines when the customer joins the loyalty program.   - `not_join`: The customer does not join the loyalty program but can still earn and spend loyalty points.       **Note**: The customer does not have a program join date.   - `points_activated`: The customer joins the loyalty program only when their earned loyalty points become active for the first time.   - `points_earned`: The customer joins the loyalty program when they earn loyalty points for the first time.   # noqa: E501

        :return: The program_join_policy of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._program_join_policy

    @program_join_policy.setter
    def program_join_policy(self, program_join_policy):
        """Sets the program_join_policy of this LoyaltyProgram.

        The policy that defines when the customer joins the loyalty program.   - `not_join`: The customer does not join the loyalty program but can still earn and spend loyalty points.       **Note**: The customer does not have a program join date.   - `points_activated`: The customer joins the loyalty program only when their earned loyalty points become active for the first time.   - `points_earned`: The customer joins the loyalty program when they earn loyalty points for the first time.   # noqa: E501

        :param program_join_policy: The program_join_policy of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_join", "points_activated", "points_earned"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and program_join_policy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `program_join_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(program_join_policy, allowed_values)
            )

        self._program_join_policy = program_join_policy

    @property
    def tiers_expiration_policy(self):
        """Gets the tiers_expiration_policy of this LoyaltyProgram.  # noqa: E501

        The policy that defines which date is used to calculate the expiration date of a customer's current tier.  - `tier_start_date`: The tier expiration date is calculated based on when the customer joined the current tier.  - `program_join_date`: The tier expiration date is calculated based on when the customer joined the loyalty program.  - `customer_attribute`: The tier expiration date is calculated based on a custom customer attribute.  - `absolute_expiration`: The tier expires on a specified date and time. **Note**: For absolute expiration, it is required to provide a `tiersStartDate.`   # noqa: E501

        :return: The tiers_expiration_policy of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._tiers_expiration_policy

    @tiers_expiration_policy.setter
    def tiers_expiration_policy(self, tiers_expiration_policy):
        """Sets the tiers_expiration_policy of this LoyaltyProgram.

        The policy that defines which date is used to calculate the expiration date of a customer's current tier.  - `tier_start_date`: The tier expiration date is calculated based on when the customer joined the current tier.  - `program_join_date`: The tier expiration date is calculated based on when the customer joined the loyalty program.  - `customer_attribute`: The tier expiration date is calculated based on a custom customer attribute.  - `absolute_expiration`: The tier expires on a specified date and time. **Note**: For absolute expiration, it is required to provide a `tiersStartDate.`   # noqa: E501

        :param tiers_expiration_policy: The tiers_expiration_policy of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        allowed_values = ["tier_start_date", "program_join_date", "customer_attribute", "absolute_expiration"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tiers_expiration_policy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tiers_expiration_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(tiers_expiration_policy, allowed_values)
            )

        self._tiers_expiration_policy = tiers_expiration_policy

    @property
    def tiers_start_date(self):
        """Gets the tiers_start_date of this LoyaltyProgram.  # noqa: E501

        Timestamp at which the tier starts for all customers.  **Note**: This is only required when the tier expiration policy is set to `absolute_expiration`.   # noqa: E501

        :return: The tiers_start_date of this LoyaltyProgram.  # noqa: E501
        :rtype: datetime
        """
        return self._tiers_start_date

    @tiers_start_date.setter
    def tiers_start_date(self, tiers_start_date):
        """Sets the tiers_start_date of this LoyaltyProgram.

        Timestamp at which the tier starts for all customers.  **Note**: This is only required when the tier expiration policy is set to `absolute_expiration`.   # noqa: E501

        :param tiers_start_date: The tiers_start_date of this LoyaltyProgram.  # noqa: E501
        :type: datetime
        """

        self._tiers_start_date = tiers_start_date

    @property
    def tiers_expire_in(self):
        """Gets the tiers_expire_in of this LoyaltyProgram.  # noqa: E501

        The amount of time after which the tier expires.  The time format is an **integer** followed by one letter indicating the time unit. Examples: `30s`, `40m`, `1h`, `5D`, `7W`, `10M`, `15Y`.  Available units:  - `s`: seconds - `m`: minutes - `h`: hours - `D`: days - `W`: weeks - `M`: months - `Y`: years  You can round certain units up or down: - `_D` for rounding down days only. Signifies the start of the day. - `_U` for rounding up days, weeks, months and years. Signifies the end of the day, week, month or year.   # noqa: E501

        :return: The tiers_expire_in of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._tiers_expire_in

    @tiers_expire_in.setter
    def tiers_expire_in(self, tiers_expire_in):
        """Sets the tiers_expire_in of this LoyaltyProgram.

        The amount of time after which the tier expires.  The time format is an **integer** followed by one letter indicating the time unit. Examples: `30s`, `40m`, `1h`, `5D`, `7W`, `10M`, `15Y`.  Available units:  - `s`: seconds - `m`: minutes - `h`: hours - `D`: days - `W`: weeks - `M`: months - `Y`: years  You can round certain units up or down: - `_D` for rounding down days only. Signifies the start of the day. - `_U` for rounding up days, weeks, months and years. Signifies the end of the day, week, month or year.   # noqa: E501

        :param tiers_expire_in: The tiers_expire_in of this LoyaltyProgram.  # noqa: E501
        :type: str
        """

        self._tiers_expire_in = tiers_expire_in

    @property
    def tiers_downgrade_policy(self):
        """Gets the tiers_downgrade_policy of this LoyaltyProgram.  # noqa: E501

        Customers's tier downgrade policy.  - `one_down`: Once the tier expires and if the user doesn't have enough points to stay in the tier, the user is downgraded one tier down.  - `balance_based`: Once the tier expires, the user's tier is evaluated based on the amount of active points the user has at this instant.   # noqa: E501

        :return: The tiers_downgrade_policy of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._tiers_downgrade_policy

    @tiers_downgrade_policy.setter
    def tiers_downgrade_policy(self, tiers_downgrade_policy):
        """Sets the tiers_downgrade_policy of this LoyaltyProgram.

        Customers's tier downgrade policy.  - `one_down`: Once the tier expires and if the user doesn't have enough points to stay in the tier, the user is downgraded one tier down.  - `balance_based`: Once the tier expires, the user's tier is evaluated based on the amount of active points the user has at this instant.   # noqa: E501

        :param tiers_downgrade_policy: The tiers_downgrade_policy of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        allowed_values = ["one_down", "balance_based"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tiers_downgrade_policy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tiers_downgrade_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(tiers_downgrade_policy, allowed_values)
            )

        self._tiers_downgrade_policy = tiers_downgrade_policy

    @property
    def card_code_settings(self):
        """Gets the card_code_settings of this LoyaltyProgram.  # noqa: E501


        :return: The card_code_settings of this LoyaltyProgram.  # noqa: E501
        :rtype: CodeGeneratorSettings
        """
        return self._card_code_settings

    @card_code_settings.setter
    def card_code_settings(self, card_code_settings):
        """Sets the card_code_settings of this LoyaltyProgram.


        :param card_code_settings: The card_code_settings of this LoyaltyProgram.  # noqa: E501
        :type: CodeGeneratorSettings
        """

        self._card_code_settings = card_code_settings

    @property
    def account_id(self):
        """Gets the account_id of this LoyaltyProgram.  # noqa: E501

        The ID of the Talon.One account that owns this program.  # noqa: E501

        :return: The account_id of this LoyaltyProgram.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this LoyaltyProgram.

        The ID of the Talon.One account that owns this program.  # noqa: E501

        :param account_id: The account_id of this LoyaltyProgram.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this LoyaltyProgram.  # noqa: E501

        The internal name for the Loyalty Program. This is an immutable value.  # noqa: E501

        :return: The name of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoyaltyProgram.

        The internal name for the Loyalty Program. This is an immutable value.  # noqa: E501

        :param name: The name of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tiers(self):
        """Gets the tiers of this LoyaltyProgram.  # noqa: E501

        The tiers in this loyalty program.  # noqa: E501

        :return: The tiers of this LoyaltyProgram.  # noqa: E501
        :rtype: list[LoyaltyTier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this LoyaltyProgram.

        The tiers in this loyalty program.  # noqa: E501

        :param tiers: The tiers of this LoyaltyProgram.  # noqa: E501
        :type: list[LoyaltyTier]
        """

        self._tiers = tiers

    @property
    def timezone(self):
        """Gets the timezone of this LoyaltyProgram.  # noqa: E501

        A string containing an IANA timezone descriptor.  # noqa: E501

        :return: The timezone of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this LoyaltyProgram.

        A string containing an IANA timezone descriptor.  # noqa: E501

        :param timezone: The timezone of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and timezone is None:  # noqa: E501
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                timezone is not None and len(timezone) < 1):
            raise ValueError("Invalid value for `timezone`, length must be greater than or equal to `1`")  # noqa: E501

        self._timezone = timezone

    @property
    def card_based(self):
        """Gets the card_based of this LoyaltyProgram.  # noqa: E501

        Defines the type of loyalty program: - `true`: the program is a card-based. - `false`: the program is profile-based.   # noqa: E501

        :return: The card_based of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._card_based

    @card_based.setter
    def card_based(self, card_based):
        """Sets the card_based of this LoyaltyProgram.

        Defines the type of loyalty program: - `true`: the program is a card-based. - `false`: the program is profile-based.   # noqa: E501

        :param card_based: The card_based of this LoyaltyProgram.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and card_based is None:  # noqa: E501
            raise ValueError("Invalid value for `card_based`, must not be `None`")  # noqa: E501

        self._card_based = card_based

    @property
    def can_update_tiers(self):
        """Gets the can_update_tiers of this LoyaltyProgram.  # noqa: E501

        `True` if the tier definitions can be updated.   # noqa: E501

        :return: The can_update_tiers of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._can_update_tiers

    @can_update_tiers.setter
    def can_update_tiers(self, can_update_tiers):
        """Sets the can_update_tiers of this LoyaltyProgram.

        `True` if the tier definitions can be updated.   # noqa: E501

        :param can_update_tiers: The can_update_tiers of this LoyaltyProgram.  # noqa: E501
        :type: bool
        """

        self._can_update_tiers = can_update_tiers

    @property
    def can_update_join_policy(self):
        """Gets the can_update_join_policy of this LoyaltyProgram.  # noqa: E501

        `True` if the program join policy can be updated.   # noqa: E501

        :return: The can_update_join_policy of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._can_update_join_policy

    @can_update_join_policy.setter
    def can_update_join_policy(self, can_update_join_policy):
        """Sets the can_update_join_policy of this LoyaltyProgram.

        `True` if the program join policy can be updated.   # noqa: E501

        :param can_update_join_policy: The can_update_join_policy of this LoyaltyProgram.  # noqa: E501
        :type: bool
        """

        self._can_update_join_policy = can_update_join_policy

    @property
    def can_update_tier_expiration_policy(self):
        """Gets the can_update_tier_expiration_policy of this LoyaltyProgram.  # noqa: E501

        `True` if the tier expiration policy can be updated.   # noqa: E501

        :return: The can_update_tier_expiration_policy of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._can_update_tier_expiration_policy

    @can_update_tier_expiration_policy.setter
    def can_update_tier_expiration_policy(self, can_update_tier_expiration_policy):
        """Sets the can_update_tier_expiration_policy of this LoyaltyProgram.

        `True` if the tier expiration policy can be updated.   # noqa: E501

        :param can_update_tier_expiration_policy: The can_update_tier_expiration_policy of this LoyaltyProgram.  # noqa: E501
        :type: bool
        """

        self._can_update_tier_expiration_policy = can_update_tier_expiration_policy

    @property
    def can_upgrade_to_advanced_tiers(self):
        """Gets the can_upgrade_to_advanced_tiers of this LoyaltyProgram.  # noqa: E501

        `True` if the program can be upgraded to use the `tiersExpireIn` and `tiersDowngradePolicy` properties.   # noqa: E501

        :return: The can_upgrade_to_advanced_tiers of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._can_upgrade_to_advanced_tiers

    @can_upgrade_to_advanced_tiers.setter
    def can_upgrade_to_advanced_tiers(self, can_upgrade_to_advanced_tiers):
        """Sets the can_upgrade_to_advanced_tiers of this LoyaltyProgram.

        `True` if the program can be upgraded to use the `tiersExpireIn` and `tiersDowngradePolicy` properties.   # noqa: E501

        :param can_upgrade_to_advanced_tiers: The can_upgrade_to_advanced_tiers of this LoyaltyProgram.  # noqa: E501
        :type: bool
        """

        self._can_upgrade_to_advanced_tiers = can_upgrade_to_advanced_tiers

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
        if not isinstance(other, LoyaltyProgram):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyProgram):
            return True

        return self.to_dict() != other.to_dict()
