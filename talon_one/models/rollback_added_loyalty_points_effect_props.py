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


class RollbackAddedLoyaltyPointsEffectProps(object):
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
        'program_id': 'int',
        'sub_ledger_id': 'str',
        'value': 'float',
        'recipient_integration_id': 'str',
        'transaction_uuid': 'str',
        'cart_item_position': 'float',
        'cart_item_sub_position': 'float',
        'card_identifier': 'str'
    }

    attribute_map = {
        'program_id': 'programId',
        'sub_ledger_id': 'subLedgerId',
        'value': 'value',
        'recipient_integration_id': 'recipientIntegrationId',
        'transaction_uuid': 'transactionUUID',
        'cart_item_position': 'cartItemPosition',
        'cart_item_sub_position': 'cartItemSubPosition',
        'card_identifier': 'cardIdentifier'
    }

    def __init__(self, program_id=None, sub_ledger_id=None, value=None, recipient_integration_id=None, transaction_uuid=None, cart_item_position=None, cart_item_sub_position=None, card_identifier=None, local_vars_configuration=None):  # noqa: E501
        """RollbackAddedLoyaltyPointsEffectProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._program_id = None
        self._sub_ledger_id = None
        self._value = None
        self._recipient_integration_id = None
        self._transaction_uuid = None
        self._cart_item_position = None
        self._cart_item_sub_position = None
        self._card_identifier = None
        self.discriminator = None

        self.program_id = program_id
        self.sub_ledger_id = sub_ledger_id
        self.value = value
        self.recipient_integration_id = recipient_integration_id
        self.transaction_uuid = transaction_uuid
        if cart_item_position is not None:
            self.cart_item_position = cart_item_position
        if cart_item_sub_position is not None:
            self.cart_item_sub_position = cart_item_sub_position
        if card_identifier is not None:
            self.card_identifier = card_identifier

    @property
    def program_id(self):
        """Gets the program_id of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501

        The ID of the loyalty program where the points were originally added.  # noqa: E501

        :return: The program_id of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this RollbackAddedLoyaltyPointsEffectProps.

        The ID of the loyalty program where the points were originally added.  # noqa: E501

        :param program_id: The program_id of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and program_id is None:  # noqa: E501
            raise ValueError("Invalid value for `program_id`, must not be `None`")  # noqa: E501

        self._program_id = program_id

    @property
    def sub_ledger_id(self):
        """Gets the sub_ledger_id of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501

        The ID of the subledger within the loyalty program where these points were originally added.  # noqa: E501

        :return: The sub_ledger_id of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._sub_ledger_id

    @sub_ledger_id.setter
    def sub_ledger_id(self, sub_ledger_id):
        """Sets the sub_ledger_id of this RollbackAddedLoyaltyPointsEffectProps.

        The ID of the subledger within the loyalty program where these points were originally added.  # noqa: E501

        :param sub_ledger_id: The sub_ledger_id of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_ledger_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_ledger_id`, must not be `None`")  # noqa: E501

        self._sub_ledger_id = sub_ledger_id

    @property
    def value(self):
        """Gets the value of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501

        The amount of points that were rolled back.  # noqa: E501

        :return: The value of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RollbackAddedLoyaltyPointsEffectProps.

        The amount of points that were rolled back.  # noqa: E501

        :param value: The value of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def recipient_integration_id(self):
        """Gets the recipient_integration_id of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501

        The user for whom these points were originally added.  # noqa: E501

        :return: The recipient_integration_id of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._recipient_integration_id

    @recipient_integration_id.setter
    def recipient_integration_id(self, recipient_integration_id):
        """Sets the recipient_integration_id of this RollbackAddedLoyaltyPointsEffectProps.

        The user for whom these points were originally added.  # noqa: E501

        :param recipient_integration_id: The recipient_integration_id of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and recipient_integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `recipient_integration_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                recipient_integration_id is not None and len(recipient_integration_id) > 1000):
            raise ValueError("Invalid value for `recipient_integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._recipient_integration_id = recipient_integration_id

    @property
    def transaction_uuid(self):
        """Gets the transaction_uuid of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501

        The identifier of 'deduction' entry added to the ledger as the `addLoyaltyPoints` effect is rolled back.  # noqa: E501

        :return: The transaction_uuid of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._transaction_uuid

    @transaction_uuid.setter
    def transaction_uuid(self, transaction_uuid):
        """Sets the transaction_uuid of this RollbackAddedLoyaltyPointsEffectProps.

        The identifier of 'deduction' entry added to the ledger as the `addLoyaltyPoints` effect is rolled back.  # noqa: E501

        :param transaction_uuid: The transaction_uuid of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_uuid`, must not be `None`")  # noqa: E501

        self._transaction_uuid = transaction_uuid

    @property
    def cart_item_position(self):
        """Gets the cart_item_position of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501

        The index of the item in the cart items for which the loyalty points were rolled back.  # noqa: E501

        :return: The cart_item_position of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._cart_item_position

    @cart_item_position.setter
    def cart_item_position(self, cart_item_position):
        """Sets the cart_item_position of this RollbackAddedLoyaltyPointsEffectProps.

        The index of the item in the cart items for which the loyalty points were rolled back.  # noqa: E501

        :param cart_item_position: The cart_item_position of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :type: float
        """

        self._cart_item_position = cart_item_position

    @property
    def cart_item_sub_position(self):
        """Gets the cart_item_sub_position of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501

        For cart items with `quantity` > 1, the sub-position indicates to which item the loyalty points were rolled back.   # noqa: E501

        :return: The cart_item_sub_position of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._cart_item_sub_position

    @cart_item_sub_position.setter
    def cart_item_sub_position(self, cart_item_sub_position):
        """Sets the cart_item_sub_position of this RollbackAddedLoyaltyPointsEffectProps.

        For cart items with `quantity` > 1, the sub-position indicates to which item the loyalty points were rolled back.   # noqa: E501

        :param cart_item_sub_position: The cart_item_sub_position of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :type: float
        """

        self._cart_item_sub_position = cart_item_sub_position

    @property
    def card_identifier(self):
        """Gets the card_identifier of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501

        The alphanumeric identifier of the loyalty card.   # noqa: E501

        :return: The card_identifier of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._card_identifier

    @card_identifier.setter
    def card_identifier(self, card_identifier):
        """Sets the card_identifier of this RollbackAddedLoyaltyPointsEffectProps.

        The alphanumeric identifier of the loyalty card.   # noqa: E501

        :param card_identifier: The card_identifier of this RollbackAddedLoyaltyPointsEffectProps.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                card_identifier is not None and len(card_identifier) > 108):
            raise ValueError("Invalid value for `card_identifier`, length must be less than or equal to `108`")  # noqa: E501

        self._card_identifier = card_identifier

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
        if not isinstance(other, RollbackAddedLoyaltyPointsEffectProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RollbackAddedLoyaltyPointsEffectProps):
            return True

        return self.to_dict() != other.to_dict()
