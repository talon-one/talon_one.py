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


class Event(object):
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
        'profile_id': 'str',
        'type': 'str',
        'attributes': 'object',
        'session_id': 'str',
        'effects': 'list[object]',
        'ledger_entries': 'list[LedgerEntry]',
        'meta': 'Meta'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'application_id': 'applicationId',
        'profile_id': 'profileId',
        'type': 'type',
        'attributes': 'attributes',
        'session_id': 'sessionId',
        'effects': 'effects',
        'ledger_entries': 'ledgerEntries',
        'meta': 'meta'
    }

    def __init__(self, id=None, created=None, application_id=None, profile_id=None, type=None, attributes=None, session_id=None, effects=None, ledger_entries=None, meta=None, local_vars_configuration=None):  # noqa: E501
        """Event - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._application_id = None
        self._profile_id = None
        self._type = None
        self._attributes = None
        self._session_id = None
        self._effects = None
        self._ledger_entries = None
        self._meta = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.application_id = application_id
        if profile_id is not None:
            self.profile_id = profile_id
        self.type = type
        self.attributes = attributes
        if session_id is not None:
            self.session_id = session_id
        self.effects = effects
        self.ledger_entries = ledger_entries
        if meta is not None:
            self.meta = meta

    @property
    def id(self):
        """Gets the id of this Event.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this Event.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this Event.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Event.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this Event.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Event.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this Event.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def application_id(self):
        """Gets the application_id of this Event.  # noqa: E501

        The ID of the application that owns this entity.  # noqa: E501

        :return: The application_id of this Event.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this Event.

        The ID of the application that owns this entity.  # noqa: E501

        :param application_id: The application_id of this Event.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def profile_id(self):
        """Gets the profile_id of this Event.  # noqa: E501

        ID of the customers profile as used within this Talon.One account. May be omitted or set to the empty string if the customer does not yet have a known profile ID.  # noqa: E501

        :return: The profile_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this Event.

        ID of the customers profile as used within this Talon.One account. May be omitted or set to the empty string if the customer does not yet have a known profile ID.  # noqa: E501

        :param profile_id: The profile_id of this Event.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def type(self):
        """Gets the type of this Event.  # noqa: E501

        A string representing the event. Must not be a reserved event name.  # noqa: E501

        :return: The type of this Event.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Event.

        A string representing the event. Must not be a reserved event name.  # noqa: E501

        :param type: The type of this Event.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this Event.  # noqa: E501

        Arbitrary additional JSON data associated with the event.  # noqa: E501

        :return: The attributes of this Event.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Event.

        Arbitrary additional JSON data associated with the event.  # noqa: E501

        :param attributes: The attributes of this Event.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def session_id(self):
        """Gets the session_id of this Event.  # noqa: E501

        The ID of the session that this event occurred in.  # noqa: E501

        :return: The session_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this Event.

        The ID of the session that this event occurred in.  # noqa: E501

        :param session_id: The session_id of this Event.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def effects(self):
        """Gets the effects of this Event.  # noqa: E501

        An array of \"effects\" that must be applied in response to this event. Example effects include `addItemToCart` or `setDiscount`.   # noqa: E501

        :return: The effects of this Event.  # noqa: E501
        :rtype: list[object]
        """
        return self._effects

    @effects.setter
    def effects(self, effects):
        """Sets the effects of this Event.

        An array of \"effects\" that must be applied in response to this event. Example effects include `addItemToCart` or `setDiscount`.   # noqa: E501

        :param effects: The effects of this Event.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and effects is None:  # noqa: E501
            raise ValueError("Invalid value for `effects`, must not be `None`")  # noqa: E501

        self._effects = effects

    @property
    def ledger_entries(self):
        """Gets the ledger_entries of this Event.  # noqa: E501

        Ledger entries for the event.  # noqa: E501

        :return: The ledger_entries of this Event.  # noqa: E501
        :rtype: list[LedgerEntry]
        """
        return self._ledger_entries

    @ledger_entries.setter
    def ledger_entries(self, ledger_entries):
        """Sets the ledger_entries of this Event.

        Ledger entries for the event.  # noqa: E501

        :param ledger_entries: The ledger_entries of this Event.  # noqa: E501
        :type: list[LedgerEntry]
        """
        if self.local_vars_configuration.client_side_validation and ledger_entries is None:  # noqa: E501
            raise ValueError("Invalid value for `ledger_entries`, must not be `None`")  # noqa: E501

        self._ledger_entries = ledger_entries

    @property
    def meta(self):
        """Gets the meta of this Event.  # noqa: E501


        :return: The meta of this Event.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Event.


        :param meta: The meta of this Event.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

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
        if not isinstance(other, Event):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Event):
            return True

        return self.to_dict() != other.to_dict()
