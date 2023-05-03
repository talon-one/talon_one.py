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


class LedgerTransactionLogEntryIntegrationAPI(object):
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
        'created': 'datetime',
        'program_id': 'int',
        'customer_session_id': 'str',
        'type': 'str',
        'name': 'str',
        'start_date': 'str',
        'expiry_date': 'str',
        'subledger_id': 'str',
        'amount': 'float',
        'id': 'int',
        'ruleset_id': 'int',
        'rule_name': 'str'
    }

    attribute_map = {
        'created': 'created',
        'program_id': 'programId',
        'customer_session_id': 'customerSessionId',
        'type': 'type',
        'name': 'name',
        'start_date': 'startDate',
        'expiry_date': 'expiryDate',
        'subledger_id': 'subledgerId',
        'amount': 'amount',
        'id': 'id',
        'ruleset_id': 'rulesetId',
        'rule_name': 'ruleName'
    }

    def __init__(self, created=None, program_id=None, customer_session_id=None, type=None, name=None, start_date=None, expiry_date=None, subledger_id=None, amount=None, id=None, ruleset_id=None, rule_name=None, local_vars_configuration=None):  # noqa: E501
        """LedgerTransactionLogEntryIntegrationAPI - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created = None
        self._program_id = None
        self._customer_session_id = None
        self._type = None
        self._name = None
        self._start_date = None
        self._expiry_date = None
        self._subledger_id = None
        self._amount = None
        self._id = None
        self._ruleset_id = None
        self._rule_name = None
        self.discriminator = None

        self.created = created
        self.program_id = program_id
        if customer_session_id is not None:
            self.customer_session_id = customer_session_id
        self.type = type
        self.name = name
        self.start_date = start_date
        self.expiry_date = expiry_date
        self.subledger_id = subledger_id
        self.amount = amount
        self.id = id
        if ruleset_id is not None:
            self.ruleset_id = ruleset_id
        if rule_name is not None:
            self.rule_name = rule_name

    @property
    def created(self):
        """Gets the created of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        Date and time the loyalty transaction occurred.  # noqa: E501

        :return: The created of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this LedgerTransactionLogEntryIntegrationAPI.

        Date and time the loyalty transaction occurred.  # noqa: E501

        :param created: The created of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def program_id(self):
        """Gets the program_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        ID of the loyalty program.  # noqa: E501

        :return: The program_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this LedgerTransactionLogEntryIntegrationAPI.

        ID of the loyalty program.  # noqa: E501

        :param program_id: The program_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and program_id is None:  # noqa: E501
            raise ValueError("Invalid value for `program_id`, must not be `None`")  # noqa: E501

        self._program_id = program_id

    @property
    def customer_session_id(self):
        """Gets the customer_session_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        ID of the customer session where the transaction occurred.  # noqa: E501

        :return: The customer_session_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: str
        """
        return self._customer_session_id

    @customer_session_id.setter
    def customer_session_id(self, customer_session_id):
        """Sets the customer_session_id of this LedgerTransactionLogEntryIntegrationAPI.

        ID of the customer session where the transaction occurred.  # noqa: E501

        :param customer_session_id: The customer_session_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                customer_session_id is not None and len(customer_session_id) > 255):
            raise ValueError("Invalid value for `customer_session_id`, length must be less than or equal to `255`")  # noqa: E501

        self._customer_session_id = customer_session_id

    @property
    def type(self):
        """Gets the type of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        Type of transaction. Possible values:   - `addition`: Signifies added points.   - `subtraction`: Signifies deducted points.   # noqa: E501

        :return: The type of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LedgerTransactionLogEntryIntegrationAPI.

        Type of transaction. Possible values:   - `addition`: Signifies added points.   - `subtraction`: Signifies deducted points.   # noqa: E501

        :param type: The type of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["addition", "subtraction"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        Name or reason of the loyalty ledger transaction.  # noqa: E501

        :return: The name of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LedgerTransactionLogEntryIntegrationAPI.

        Name or reason of the loyalty ledger transaction.  # noqa: E501

        :param name: The name of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def start_date(self):
        """Gets the start_date of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        When points become active. Possible values:   - `immediate`: Points are immediately active.   - a timestamp value: Points become active at a given date and time.   # noqa: E501

        :return: The start_date of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this LedgerTransactionLogEntryIntegrationAPI.

        When points become active. Possible values:   - `immediate`: Points are immediately active.   - a timestamp value: Points become active at a given date and time.   # noqa: E501

        :param start_date: The start_date of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                start_date is not None and len(start_date) > 64):
            raise ValueError("Invalid value for `start_date`, length must be less than or equal to `64`")  # noqa: E501

        self._start_date = start_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        Date when points expire. Possible values are:   - `unlimited`: Points have no expiration date.   - `timestamp value`: Points expire on the given date.   # noqa: E501

        :return: The expiry_date of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this LedgerTransactionLogEntryIntegrationAPI.

        Date when points expire. Possible values are:   - `unlimited`: Points have no expiration date.   - `timestamp value`: Points expire on the given date.   # noqa: E501

        :param expiry_date: The expiry_date of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and expiry_date is None:  # noqa: E501
            raise ValueError("Invalid value for `expiry_date`, must not be `None`")  # noqa: E501

        self._expiry_date = expiry_date

    @property
    def subledger_id(self):
        """Gets the subledger_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        ID of the subledger.  # noqa: E501

        :return: The subledger_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: str
        """
        return self._subledger_id

    @subledger_id.setter
    def subledger_id(self, subledger_id):
        """Sets the subledger_id of this LedgerTransactionLogEntryIntegrationAPI.

        ID of the subledger.  # noqa: E501

        :param subledger_id: The subledger_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subledger_id is None:  # noqa: E501
            raise ValueError("Invalid value for `subledger_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                subledger_id is not None and len(subledger_id) > 64):
            raise ValueError("Invalid value for `subledger_id`, length must be less than or equal to `64`")  # noqa: E501

        self._subledger_id = subledger_id

    @property
    def amount(self):
        """Gets the amount of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        Amount of loyalty points added or deducted in the transaction.  # noqa: E501

        :return: The amount of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LedgerTransactionLogEntryIntegrationAPI.

        Amount of loyalty points added or deducted in the transaction.  # noqa: E501

        :param amount: The amount of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def id(self):
        """Gets the id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        ID of the loyalty ledger transaction.  # noqa: E501

        :return: The id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LedgerTransactionLogEntryIntegrationAPI.

        ID of the loyalty ledger transaction.  # noqa: E501

        :param id: The id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ruleset_id(self):
        """Gets the ruleset_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        The ID of the ruleset containing the rule that triggered this effect.  # noqa: E501

        :return: The ruleset_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: int
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        """Sets the ruleset_id of this LedgerTransactionLogEntryIntegrationAPI.

        The ID of the ruleset containing the rule that triggered this effect.  # noqa: E501

        :param ruleset_id: The ruleset_id of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: int
        """

        self._ruleset_id = ruleset_id

    @property
    def rule_name(self):
        """Gets the rule_name of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501

        The name of the rule that triggered this effect.  # noqa: E501

        :return: The rule_name of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this LedgerTransactionLogEntryIntegrationAPI.

        The name of the rule that triggered this effect.  # noqa: E501

        :param rule_name: The rule_name of this LedgerTransactionLogEntryIntegrationAPI.  # noqa: E501
        :type: str
        """

        self._rule_name = rule_name

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
        if not isinstance(other, LedgerTransactionLogEntryIntegrationAPI):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LedgerTransactionLogEntryIntegrationAPI):
            return True

        return self.to_dict() != other.to_dict()
